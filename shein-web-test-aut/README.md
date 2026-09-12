# Shein: test automation (product search on shein.com/pt)

Another automation practice project I put together: this time I applied
Selenium/Pytest to the **product search** flow on
[shein.com/pt](https://www.shein.com/pt/), following the same approach as the
other projects I'd already done (IKEA-WEB_TEST_AUT, Trotiurban), but with
a few improvements I picked up along the way.

## Structure

| File/Folder            | Role                                                                          |
| ---------------------- | ------------------------------------------------------------------------------- |
| `data.py`               | Site URL and search terms, read from `.env` with fallback                    |
| `helpers.py`            | Utilities: check if the site is up, "humanized" typing/pauses, `.env` reading |
| `common/base_page.py`   | `BasePage` with common operations (find, click, humanized typing)            |
| `SHEIN.py`              | Page Objects: `SheinHomePage`, `SheinSearchResultsPage`, `SheinProductPage`     |
| `conftest.py`           | Driver fixture (Chrome) plus automatic screenshot on failure                    |
| `TestersiteShein.py`    | Pytest tests                                                                    |
| `.github/workflows/`    | CI: runs the tests on every push/PR                                               |

## What's new compared to the previous baseline (IKEA)

- Driver via **Selenium Manager**, no need to manually download/configure chromedriver.
- `chrome_driver` fixture in `conftest.py` instead of `setup_class`/`teardown_class`.
- Config via `.env` (`python-dotenv`) instead of hardcoded values in `data.py`.
- Shared `BasePage`, reusable across projects (Shein, Continente, IKEA...).
- Automatic screenshot when a test fails (saved to `screenshots/`).
- CI workflow (GitHub Actions) running the suite on every push/PR.

## About "humanized" typing

Instead of filling the search field instantly, `helpers.human_type` types
character by character with small random pauses, and `helpers.human_pause` adds
short pauses between actions, giving the automation a rhythm closer to a real
person interacting with the site.

## Test cases

- Searching for a valid term ("vestido") returns results.
- Searching for a nonexistent term shows a "no results" message.
- Opening the first product in the list displays its title and price.
- Adding the first product to the cart.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env   # adjust SHEIN_URL / SEARCH_TERM if needed
```

Requires Chrome installed locally (Selenium Manager handles the driver automatically).

## Running the tests

```bash
pytest -v
```

## Important note

The locators in `SHEIN.py` are a starting point (marked with `TODO`). Shein
is a very dynamic site (heavy JS, anti-bot protection, region-based redirects),
and it wasn't possible to inspect the real DOM via a simple fetch while putting this project together.
**Confirm/adjust the selectors against the live site before relying on this for real.**

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Product search test automation - shein.com/pt"
git remote add origin <URL_OF_YOUR_GITHUB_REPOSITORY>
git push -u origin main
```
