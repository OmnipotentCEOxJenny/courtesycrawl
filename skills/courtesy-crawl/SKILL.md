---
name: courtesy-crawl
description: Plan and run legitimate, polite web research or scraping. Checks for an official API first, reads robots.txt (RFC 9309) and site terms, rate-limits, identifies the crawler, and honors 429/Retry-After. Use when a user wants to scrape, crawl, download or collect data from websites.
---

# CourtesyCrawl

Follow `rules/scope.mdc`. Required. Answer in the user's language.

## Workflow
1. **Purpose and data.** What is being collected and why? If it includes personal data (names with contact details, profiles), stop and explain the privacy limits; suggest aggregate or official sources.
2. **Official route first.** Look for an official API, bulk download, open-data portal, RSS/Atom feed or sitemap. Prefer it.
3. **Read the rules.**
   - robots.txt: `python scripts/courtesy_fetch.py check <URL> --agent <Token>` (see `skills/check-robots`).
   - Site terms of use: read them; if they forbid automated access or scraping, stop and tell the user.
4. **Identify yourself.** Use a product token and a contact in the User-Agent (`--agent`, `--contact`).
5. **Go slow.** Default 5 s between requests (`--delay`), or the site's Crawl-delay if larger. One connection at a time. Fetch only what is needed.
6. **Back off.** On HTTP 429 or 503, wait for `Retry-After` (seconds or HTTP date). The script retries at most twice and stops if the wait is over 10 minutes. Never retry in a loop.
7. **Never bypass.** 401/402/403, logins, paywalls and CAPTCHAs mean stop. No IP rotation, no faked browser user agents.
8. **Report:** URLs fetched, skipped (with reason), any 429s, files saved, and the robots.txt and terms findings.

## Helper script
- Install (free, pinned, tested on Python 3.13): `pip install -r scripts/requirements.txt` (`requests==2.32.3`, `protego==0.3.1`).
- Check: `python scripts/courtesy_fetch.py check https://example.com/page`
- Fetch: `python scripts/courtesy_fetch.py fetch URL [URL ...] --contact you@example.com [--delay 5] [--out courtesy_out]`
- Exit codes: 0 all fine; 1 something skipped, disallowed or failed; 2 missing --contact; 3 stopped on 429/503.

Sources: RFC 9309 (Robots Exclusion Protocol, 2022) https://www.rfc-editor.org/rfc/rfc9309.html ; RFC 6585 section 4 (429 Too Many Requests) https://www.rfc-editor.org/rfc/rfc6585.html ; RFC 9110 section 10.2.3 (Retry-After) https://www.rfc-editor.org/rfc/rfc9110.html
