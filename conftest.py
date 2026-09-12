import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCREENSHOTS_DIR = "screenshots"


@pytest.fixture(scope="class", autouse=True)
def chrome_driver(request):
    """Starts a Chrome instance for the whole test class and injects it into `self.driver`.

    Uses Selenium Manager (built in since Selenium 4.6), so there's no longer
    a need to manually download/manage chromedriver on the PATH.
    """
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically saves a screenshot when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver is not None:
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"{SCREENSHOTS_DIR}/{item.name}_{timestamp}.png"
            driver.save_screenshot(path)
            print(f"Screenshot salvo em: {path}")
