from time import sleep

from selenium.webdriver.common.by import By

from Base.utilities import Utilities


class MerchantHome(Utilities):
    # locators
    logout_loc = (By.XPATH, "//span[@class='text-base scale-1 w-auto']")
    welcome_loc = (By.CSS_SELECTOR, "p:nth-child(1)")
    welcome_msg = "Welcome"

    def __init__(self, driver):
        # Call constructor of parent class
        super().__init__(driver)

    # create logout function
    def logout(self):
        self.click_something(self.logout_loc)

    # check successful login
    def get_welcome_msg(self):
        # self.contains_text(self.welcome_loc,self.welcome_msg)
        return self.is_visible(self.welcome_loc)
















