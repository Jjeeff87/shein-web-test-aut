from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import human_pause, human_type


class BasePage:
    """Classe base para os Page Objects.

    Concentra as operações comuns (esperar elemento, clicar, digitar de forma
    humanizada) para reduzir duplicação entre os Page Objects de cada site
    (Shein, Continente, IKEA, ...). Cada Page Object específico herda desta
    classe e só define seus próprios locators e fluxos.
    """

    DEFAULT_TIMEOUT = 15

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or self.DEFAULT_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def click(self, locator):
        self.find_clickable(locator).click()
        human_pause()

    def type_human(self, locator, text):
        """Clica no campo e digita de forma humanizada (caractere por caractere, com pausas)."""
        field = self.find_clickable(locator)
        field.click()
        human_pause(0.2, 0.6)
        human_type(field, text)
        human_pause()
        return field
