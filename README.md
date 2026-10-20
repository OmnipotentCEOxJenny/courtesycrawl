# CourtesyCrawl

![CourtesyCrawl logo](assets/logo.png)

CourtesyCrawl is a free helper for doing web research and scraping the legitimate way. It checks for an official API first, reads robots.txt under RFC 9309, reads the site's terms, identifies itself with a contact, goes slowly, and backs off on HTTP 429 and Retry-After. It never bypasses logins, paywalls or CAPTCHAs and never harvests personal data. A small free Python helper script with pinned dependencies is included.

## Project status: done, pending, uncertain
**Done**
- 2026-10-20: v1.0.0 built and tested: manifest valid JSON, frontmatter valid, every documented command run, real robots.txt checks (Wikipedia disallowed path, example.com 404 = allowed), real polite fetch of RFC 9309, and a local 429/Retry-After test (waits, then stops with exit 3).

**Pending**
- Marketplace submission: not submitted yet.
- Translated summaries below are machine-made and not reviewed by native speakers.
- The helper fetches pages only; it does not render JavaScript or parse HTML (by design, to stay small).

**Uncertain**
- Site terms vary and change; CourtesyCrawl reminds the user to read them but cannot read every site's terms for them. Not legal advice.
- `Crawl-delay` is honored but is not part of RFC 9309; sites interpret it differently.
- How the listing works on the Grok Bot and Grok side: not described in the publisher terms.

## Quick start
1. Install (see Installation).
2. Ask: "Can I scrape the product pages on example.com? Do it politely."
3. Get: official-route check, robots.txt result, terms reminder, a slow identified fetch plan, and a report.

## Installation
1. Install from this repository: https://github.com/OmnipotentCEOxJenny/courtesycrawl (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`).
2. Optional helper: `pip install -r scripts/requirements.txt` (`requests==2.32.3`, `protego==0.3.1`; tested on Python 3.13). Free and open source.

## Testing
```
pip install -r scripts/requirements.txt
python scripts/courtesy_fetch.py --version
python scripts/courtesy_fetch.py check https://en.wikipedia.org/wiki/Special:Random
python scripts/courtesy_fetch.py check https://example.com/
python scripts/local_test_server.py &
python scripts/courtesy_fetch.py fetch http://127.0.0.1:8765/page http://127.0.0.1:8765/private/x --contact you@example.com --delay 0.5
python scripts/courtesy_fetch.py fetch http://127.0.0.1:8765/always429 --contact you@example.com --delay 0.5
```
Expected: `1.0.0`; Wikipedia Special pages `allowed: no` (exit 1); example.com `allowed: yes` (robots 404); local fetch waits once on 429 then saves `/page` and skips `/private/x` (exit 1); `/always429` waits twice then STOPs (exit 3).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Standards: RFC 9309, RFC 6585, RFC 9110. robots.txt parsing by protego (BSD-3-Clause).

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never invent; anything unchecked is marked UNVERIFIED.
2. Use only legitimate means: legitimate, proven sources and methods; unreliable sources rejected.
3. Double-check everything: every finding is confirmed by two independent checks, and the report shows both.
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/courtesy-crawl`: the polite research workflow.
- `skills/check-robots`: robots.txt explained under RFC 9309.
- `scripts/courtesy_fetch.py`, `scripts/requirements.txt`, `scripts/local_test_server.py`: the helper, pinned deps and a local 429 test server.
- `rules/pillars-and-scope.mdc`: the pillars and scope.
- `examples/sample-check.md`: real output.

## Languages
These summaries are machine-made translations and have not been reviewed by native speakers. The English text is authoritative.

- **Español:** CourtesyCrawl es un plugin gratuito para investigar y extraer datos web de forma legítima: respeta robots.txt, los límites 429/Retry-After y los términos del sitio, y se identifica.
- **Français:** CourtesyCrawl est un plugin gratuit pour la recherche et l'extraction web légitimes : il respecte robots.txt, les limites 429/Retry-After et les conditions du site, et s'identifie.
- **Deutsch:** CourtesyCrawl ist ein kostenloses Plugin für legitime Webrecherche und Scraping: Es beachtet robots.txt, 429/Retry-After und Nutzungsbedingungen und gibt sich zu erkennen.
- **Português:** CourtesyCrawl é um plugin gratuito para pesquisa e coleta web legítimas: respeita robots.txt, limites 429/Retry-After e os termos do site, e se identifica.
- **Italiano:** CourtesyCrawl è un plugin gratuito per ricerca e scraping web legittimi: rispetta robots.txt, i limiti 429/Retry-After e i termini del sito, e si identifica.
- **Nederlands:** CourtesyCrawl is een gratis plug-in voor legitiem webonderzoek en scrapen: respecteert robots.txt, 429/Retry-After en de sitevoorwaarden, en maakt zich bekend.
- **Polski:** CourtesyCrawl to darmowa wtyczka do legalnego badania i pobierania stron: przestrzega robots.txt, limitów 429/Retry-After i regulaminów oraz przedstawia się.
- **Русский:** CourtesyCrawl — бесплатный плагин для законного веб-исследования и сбора данных: соблюдает robots.txt, 429/Retry-After и правила сайта и представляется.
- **Українська:** CourtesyCrawl — безкоштовний плагін для законного веб-дослідження та збору даних: дотримується robots.txt, 429/Retry-After і правил сайту та представляється.
- **Türkçe:** CourtesyCrawl, meşru web araştırması ve veri toplama için ücretsiz bir eklentidir: robots.txt, 429/Retry-After ve site şartlarına uyar, kendini tanıtır.
- **العربية:** CourtesyCrawl إضافة مجانية للبحث وجمع البيانات من الويب بطرق مشروعة: تحترم robots.txt وحدود 429/Retry-After وشروط الموقع وتعرّف بنفسها.
- **עברית:** CourtesyCrawl הוא תוסף חינמי למחקר ואיסוף נתונים מהרשת בדרך לגיטימית: מכבד את robots.txt, את 429/Retry-After ואת תנאי האתר ומזדהה.
- **فارسی:** CourtesyCrawl افزونه‌ای رایگان برای پژوهش و جمع‌آوری مشروع داده از وب است: به robots.txt، محدودیت 429/Retry-After و شرایط سایت احترام می‌گذارد و خود را معرفی می‌کند.
- **हिन्दी:** CourtesyCrawl वैध वेब शोध और स्क्रैपिंग के लिए मुफ़्त प्लगइन है: यह robots.txt, 429/Retry-After और साइट की शर्तों का पालन करता है और अपनी पहचान बताता है।
- **বাংলা:** CourtesyCrawl বৈধ ওয়েব গবেষণা ও স্ক্র্যাপিংয়ের জন্য বিনামূল্যের প্লাগইন: robots.txt, 429/Retry-After ও সাইটের শর্ত মানে এবং নিজের পরিচয় দেয়।
- **اردو:** CourtesyCrawl جائز ویب تحقیق اور اسکریپنگ کے لیے مفت پلگ اِن ہے: یہ robots.txt، 429/Retry-After اور سائٹ کی شرائط کا احترام کرتا ہے اور اپنی شناخت کراتا ہے۔
- **中文（简体）:** CourtesyCrawl 是一款免费插件，帮助合法地进行网络研究与抓取：遵守 robots.txt、429/Retry-After 限制和网站条款，并表明身份。
- **日本語:** CourtesyCrawl は正当なウェブ調査・スクレイピングのための無料プラグインです。robots.txt、429/Retry-After、サイト規約を守り、身元を明示します。
- **한국어:** CourtesyCrawl은 합법적인 웹 조사와 스크래핑을 위한 무료 플러그인으로, robots.txt, 429/Retry-After, 사이트 약관을 지키고 자신을 밝힙니다.
- **Bahasa Indonesia:** CourtesyCrawl adalah plugin gratis untuk riset dan scraping web yang sah: mematuhi robots.txt, batas 429/Retry-After, dan ketentuan situs, serta mengidentifikasi diri.
- **Tiếng Việt:** CourtesyCrawl là plugin miễn phí để nghiên cứu và thu thập web hợp pháp: tuân thủ robots.txt, giới hạn 429/Retry-After và điều khoản trang, đồng thời tự giới thiệu.
- **Kiswahili:** CourtesyCrawl ni programu-jalizi ya bure kwa utafiti na ukusanyaji halali wa data mtandaoni: inaheshimu robots.txt, 429/Retry-After na masharti ya tovuti, na inajitambulisha.

## License
MIT. See `LICENSE`.
