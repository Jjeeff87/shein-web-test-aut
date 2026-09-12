from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import human_pause, human_type


class BasePage:
    """Base class for the Page Objects.

    Concentrates the common operations (waiting for an element, clicking, humanized
    typing) to reduce duplication between the Page Objects of each site
    (Shein, Continente, IKEA, ...). Each specific Page Object inherits from this
    class and only defines its own locators and flows.
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
        """Clicks the field and types in a humanized way (character by character, with pauses)."""
        field = self.find_clickable(locator)
        field.click()
        human_pause(0.2, 0.6)
        human_type(field, text)
        human_pause()
        return field
