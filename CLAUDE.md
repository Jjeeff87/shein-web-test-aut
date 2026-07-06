# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Selenium/pytest automated tests for the product search flow on shein.com/pt.

## Commands

```bash
pip install -r requirements.txt        # selenium, requests, pytest, python-dotenv
cp .env.example .env                   # adjust SHEIN_URL / SEARCH_TERM if needed
pytest -v                              # run all tests
pytest TestersiteShein.py::TestSheinSearch::test_search_returns_results -v  # single test
```

Uses Selenium Manager (built into Selenium 4.6+), so no manual chromedriver setup is needed as long as Chrome is installed locally. Tests drive a real Chrome browser against the live shein.com/pt site (no mocking), so they are network-dependent and can break if Shein changes markup, redirects by region, or serves anti-bot challenges.

## Architecture

Page Object Model, same shape as the other projects in this line (IKEA-WEB_TEST_AUT, Trotiurban):

- `data.py` — site URL and search terms, read from `.env` via `helpers.get_env` with sane defaults.
- `helpers.py` — `is_url_reachable` (pre-flight check), `human_type`/`human_pause` (see below), `get_env`.
- `common/base_page.py` — shared `BasePage` (find/find_clickable/click/type_human) reused by every Page Object here and meant to also be reused across the sibling projects.
- `SHEIN.py` — Page Objects: `SheinHomePage`, `SheinSearchResultsPage`, `SheinProductPage`, all extending `BasePage`.
- `conftest.py` — `chrome_driver` fixture (class-scoped, injects `self.driver`) replacing the old `setup_class`/`teardown_class` pattern, plus a `pytest_runtest_makereport` hook that saves a screenshot to `screenshots/` on any test failure.
- `TestersiteShein.py` — pytest test class `TestSheinSearch`; each test navigates fresh from the home page (`setup_method`) and flows through the page objects.
- `.github/workflows/tests.yml` — runs the suite on push/PR via GitHub Actions.

### Humanized typing

Same as the other projects: `helpers.human_type` types character-by-character with small random delays, and `helpers.human_pause` adds short randomized pauses between actions, so the automation doesn't look like an obviously scripted fill-and-submit.

### Known caveat

Locators in `SHEIN.py` are best-effort placeholders (marked with TODO) — Shein is a heavily JS-rendered, anti-bot-protected site whose DOM couldn't be inspected via a plain HTTP fetch while scaffolding this project. Verify/adjust selectors against the live site (or via browser devtools) before relying on these tests.
