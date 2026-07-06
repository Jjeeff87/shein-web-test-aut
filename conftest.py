import os
from datetime import datetime

import pytest
from selenium import webdriver

SCREENSHOTS_DIR = "screenshots"


@pytest.fixture(scope="class", autouse=True)
def chrome_driver(request):
    """Sobe um Chrome para a classe de teste inteira e injeta em `self.driver`.

    Usa o Selenium Manager (nativo desde o Selenium 4.6), então não é mais
    preciso baixar/gerenciar o chromedriver manualmente no PATH.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Salva um screenshot automaticamente quando um teste falha."""
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
