#!/usr/bin/env python3
"""CourtesyCrawl helper (free, MIT). Reads robots.txt per RFC 9309, identifies
itself, rate-limits, and honors 429/503 Retry-After. No login, no paywall bypass.

Usage:
  python courtesy_fetch.py check URL [--agent NAME]
  python courtesy_fetch.py fetch URL [URL ...] --contact EMAIL_OR_URL [--delay SECONDS] [--out DIR]

Tested with Python 3.13, requests==2.32.3, protego==0.3.1.
"""
import argparse, email.utils, hashlib, os, sys, time, urllib.parse
import requests
from protego import Protego

VERSION = "1.0.3"
MAX_ROBOTS_BYTES = 500 * 1024  # RFC 9309 sec. 2.5: parse at least 500 KiB
MAX_RETRY_AFTER = 600          # stop rather than wait more than 10 minutes
_robots_cache = {}             # RFC 9309 sec. 2.4: do not cache beyond 24 h (one run only here)


def user_agent(agent, contact):
    ua = f"{agent}/{VERSION}"
    return f"{ua} (+{contact})" if contact else ua


def load_robots(url, ua):
    """Return (policy, status_note). policy: Protego object, 'allow_all' or 'disallow_all'."""
    p = urllib.parse.urlsplit(url)
    root = f"{p.scheme}://{p.netloc}"
    if root in _robots_cache:
        return _robots_cache[root]
    robots_url = root + "/robots.txt"
    try:
        r = requests.get(robots_url, headers={"User-Agent": ua}, timeout=20, allow_redirects=True)
    except requests.RequestException as e:
        res = ("disallow_all", f"robots.txt unreachable ({e.__class__.__name__}): treat all as disallowed (RFC 9309 2.3.1.4)")
    else:
        if 200 <= r.status_code < 300:
            res = (Protego.parse(r.content[:MAX_ROBOTS_BYTES].decode("utf-8", "replace")), f"robots.txt {r.status_code}")
        elif 400 <= r.status_code < 500:
            res = ("allow_all", f"robots.txt {r.status_code}: no rules, crawling allowed (RFC 9309 2.3.1.3)")
        else:
            res = ("disallow_all", f"robots.txt {r.status_code}: treat all as disallowed (RFC 9309 2.3.1.4)")
    _robots_cache[root] = res
    return res


def allowed(url, agent, ua):
    policy, note = load_robots(url, ua)
    if policy == "allow_all":
        return True, None, note
    if policy == "disallow_all":
        return False, None, note
    return policy.can_fetch(url, agent), policy.crawl_delay(agent), note


def parse_retry_after(value):
    if not value:
        return None
    value = value.strip()
    if value.isdigit():
        return int(value)
    try:
        dt = email.utils.parsedate_to_datetime(value)
        return max(0, int(dt.timestamp() - time.time()))
    except (TypeError, ValueError):
        return None


def cmd_check(a):
    ua = user_agent(a.agent, a.contact)
    ok, delay, note = allowed(a.url, a.agent, ua)
    print(f"robots: {note}")
    print(f"user-agent token: {a.agent}")
    print(f"url: {a.url}")
    print(f"allowed: {'yes' if ok else 'no'}")
    print(f"crawl-delay: {delay if delay is not None else 'none set'}")
    print("note: robots.txt is not the only rule; also read the site's terms of use.")
    return 0 if ok else 1


def cmd_fetch(a):
    if not a.contact:
        print("error: --contact is required so site owners can reach you", file=sys.stderr)
        return 2
    ua = user_agent(a.agent, a.contact)
    os.makedirs(a.out, exist_ok=True)
    sess = requests.Session()
    sess.headers["User-Agent"] = ua
    rc, last = 0, 0.0
    for url in a.urls:
        ok, crawl_delay, note = allowed(url, a.agent, ua)
        if not ok:
            print(f"SKIP {url}: disallowed by robots.txt ({note})")
            rc = 1
            continue
        delay = max(a.delay, float(crawl_delay or 0))
        wait = last + delay - time.time()
        if wait > 0:
            time.sleep(wait)
        for attempt in range(a.max_retries + 1):
            last = time.time()
            try:
                r = sess.get(url, timeout=30)
            except requests.RequestException as e:
                print(f"ERROR {url}: {e.__class__.__name__}")
                rc = 1
                break
            if r.status_code in (429, 503):
                ra = parse_retry_after(r.headers.get("Retry-After"))
                if attempt >= a.max_retries or (ra is not None and ra > MAX_RETRY_AFTER):
                    print(f"STOP {url}: HTTP {r.status_code}, Retry-After={r.headers.get('Retry-After')}; stopping, do not retry in a loop")
                    return 3
                pause = ra if ra is not None else delay * (2 ** (attempt + 1))
                print(f"WAIT {url}: HTTP {r.status_code}, sleeping {pause}s")
                time.sleep(pause)
                continue
            if r.status_code in (401, 402, 403):
                print(f"SKIP {url}: HTTP {r.status_code} (login, payment or access denied; not bypassing)")
                rc = 1
                break
            name = hashlib.sha256(url.encode()).hexdigest()[:16] + ".html"
            with open(os.path.join(a.out, name), "wb") as f:
                f.write(r.content)
            print(f"OK {url}: HTTP {r.status_code}, {len(r.content)} bytes -> {os.path.join(a.out, name)}")
            if r.status_code >= 400:
                rc = 1
            break
    return rc


def main(argv=None):
    ap = argparse.ArgumentParser(description="CourtesyCrawl helper: robots.txt (RFC 9309), rate limits, 429/Retry-After.")
    ap.add_argument("--version", action="version", version=VERSION)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="check one URL against robots.txt")
    c.add_argument("url")
    f = sub.add_parser("fetch", help="politely fetch allowed URLs")
    f.add_argument("urls", nargs="+")
    f.add_argument("--delay", type=float, default=5.0, help="minimum seconds between requests (default 5)")
    f.add_argument("--max-retries", type=int, default=2)
    f.add_argument("--out", default="courtesy_out")
    for p in (c, f):
        p.add_argument("--agent", default="CourtesyCrawl", help="product token matched against robots.txt groups")
        p.add_argument("--contact", default=None, help="email or URL put in the User-Agent")
    a = ap.parse_args(argv)
    return cmd_check(a) if a.cmd == "check" else cmd_fetch(a)


if __name__ == "__main__":
    sys.exit(main())
