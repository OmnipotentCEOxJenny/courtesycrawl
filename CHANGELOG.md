# Changelog

## 1.0.8 (2026-10-23)
- README: new "Testing status" section. Local automated tests pass; in-app testing is not yet completed. Records that the marketplace submit form's "tested locally and in-app" confirmation (2026-10-20) was checked in error before any in-app test; in-app testing is pending.
- Docs only; no behavior changes. Local tests re-run and passed. Not tested in-app. Not resubmitted.

## 1.0.7 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.6 (2026-10-23)
- Search keywords: 33 to 40 (added CrawlDelay, OfficialApiFirst, SiteTerms, PoliteFetch, BotIdentity, ScrapingChecklist, AllowedPaths), all CourtesyCrawl-specific, per Rob's keyword rules.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.5 (2026-10-22)
- README Testing line now says `Expected: 1.0.5` (it still said 1.0.0).
- `scripts/courtesy_fetch.py --version` reports 1.0.5. Docs-only; no behavior changes.

## 1.0.4 (2026-10-22)
- `.gitignore` added: ignores Python cache folders (`__pycache__/`, `*.pyc`).
- `scripts/courtesy_fetch.py --version` reports 1.0.4. No behavior changes.

## 1.0.3 (2026-10-21)
- Added `tests/check_frontmatter.py`: a strict YAML front-matter check (PyYAML `safe_load`) for every SKILL.md and rules .mdc file, plus a plugin.json JSON check. Run `python3 tests/check_frontmatter.py` from the repo root; it catches the unquoted-colon bug fixed in PluginPulse 1.0.2.
- `scripts/courtesy_fetch.py` now reports `--version` 1.0.3, matching the plugin version (it said 1.0.0 since the 1.0.1/1.0.2 docs-only releases).
- No behavior changes to skills or rules.

## 1.0.2 (2026-10-20)
- TRANSLATIONS.md: each of the 23 languages now includes this plugin's specific limits list (from the README's "Honest assessment: what this plugin cannot do" section) plus the marketplace status. Machine translations, not reviewed by native speakers.
- Docs only; no behavior changes.

## 1.0.1 (2026-10-20)
- README follows the shared template: title, plain description, logo, existing content (Rob Domaine's four pillars unchanged), and a new final section "Honest assessment: what this plugin cannot do" listing real limits and the compliance statement.
- TRANSLATIONS.md now covers the same 23 languages as every Omnipotent plugin (title, description and honest-assessment summary for each), all marked as machine translations not reviewed by native speakers.
- Docs only; no behavior changes.
- Status corrected: marketplace submission made 2026-10-20 (pending review).

## 1.0.0 (2026-10-20)
- First release: courtesy-crawl and check-robots skills, pillars rule, `scripts/courtesy_fetch.py` helper (RFC 9309 robots.txt via protego, 429/503 Retry-After, rate limit, required contact), pinned `requirements.txt`, local 429 test server, real example, logo, translated summaries in 22 languages (machine-made, not native-reviewed).
