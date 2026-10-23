---
name: check-robots
description: Read and explain a site's robots.txt for a given URL and crawler name under RFC 9309, including Crawl-delay. Use when a user asks whether they may crawl or scrape a page, or what a robots.txt allows.
---

# Check robots.txt

Follow `rules/scope.mdc`. Answer in the user's language.

1. Run `python scripts/courtesy_fetch.py check <URL> --agent <Token>` and show the output.
2. Explain the RFC 9309 rules it applied:
   - The most specific (longest) matching rule wins; Allow wins a tie.
   - robots.txt answering 4xx (for example 404) means no rules: crawling allowed (section 2.3.1.3).
   - 5xx or unreachable means assume everything is disallowed (section 2.3.1.4).
   - `Crawl-delay` is not part of RFC 9309 but many sites use it; honor it.
3. Remind the user: robots.txt is a request, not access control and not the only rule. Also read the site's terms of use. A disallowed path is not an invitation to try another route.
