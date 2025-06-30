from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utilities:

    def __init__(self, driver):
        self.actions = ActionChains(driver)
        self.driver = driver
        # actions = ActionChains(driver)

    def type_something(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def hit_spacebar(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(Keys.SPACE)

    def hit_tab(self):
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(Keys.TAB)
        self.actions.send_keys(Keys.TAB).perform()

    def click_something(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    def contains_text(self, locator, text):
        message = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return text in message.text

    def is_visible(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
