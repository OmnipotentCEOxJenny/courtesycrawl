# Example: real CourtesyCrawl run (2026-10-20, America/New_York)

```
$ python scripts/courtesy_fetch.py check https://en.wikipedia.org/wiki/Special:Random
robots: robots.txt 200
user-agent token: CourtesyCrawl
url: https://en.wikipedia.org/wiki/Special:Random
allowed: no
crawl-delay: none set
note: robots.txt is not the only rule; also read the site's terms of use.
```
Exit code 1. Wikipedia's robots.txt disallows `/wiki/Special:` for all crawlers. For bulk Wikipedia content, the official route is the database dumps (https://dumps.wikimedia.org/) or the API, not crawling.

```
$ python scripts/courtesy_fetch.py check https://example.com/
robots: robots.txt 404: no rules, crawling allowed (RFC 9309 2.3.1.3)
allowed: yes
```

Local 429 test (`python scripts/local_test_server.py`, then):
```
$ python scripts/courtesy_fetch.py fetch http://127.0.0.1:8765/always429 --contact you@example.com --delay 0.5
WAIT http://127.0.0.1:8765/always429: HTTP 429, sleeping 1s
WAIT http://127.0.0.1:8765/always429: HTTP 429, sleeping 1s
STOP http://127.0.0.1:8765/always429: HTTP 429, Retry-After=1; stopping, do not retry in a loop
```
Exit code 3.
