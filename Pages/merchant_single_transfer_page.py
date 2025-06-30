from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Base.utilities import Utilities


class MerchantSingleTransfer(Utilities):
    # locators
    single_transfer_payment_loc = (By.XPATH, "(//span[contains(@class,'text-sm font-medium scale-1 w-auto flex flex-1 items-center justify-between')][normalize-space()='Single Transfer'])[1]")
    single_transfer_report_loc = (By.XPATH, "(//span[contains(@class,'text-sm font-medium scale-1 w-auto flex flex-1 items-center justify-between')][normalize-space()='Single Transfer'])[1]")
    own_account_loc = (By.XPATH, "//span[normalize-space()='To Your Own Account']")
    from_own_acc_loc = (By.XPATH, "(//div[contains(@class,'css-19bb58m')])[1]")
    select_acc_loc = (By.XPATH, "(// div[@class ='css-15l1327-control'])[1]")
    to_own_acc_loc = (By.XPATH, "(//div[contains(@class,'css-19bb58m')])[2]")
    amount = (By.XPATH, "//input[@id='amount']")


    def __init__(self, driver):
        # Call constructor of parent class
        super().__init__(driver)

    # single transfer to my own account
    def my_own_account(self):
        self.click_something(self.single_transfer_payment_loc)
        self.click_something(self.own_account_loc)
        self.click_something(self.from_own_acc_loc)
        sleep(10)
        # self.click_something(self.from_own_acc_loc)
        self.hit_tab()
        # self.click_something(self.select_acc_loc)
        # self.hit_spacebar(self.from_own_acc_loc)
        # self.hit_tab(self.select_acc_loc)
        sleep(5)

        # self.type_something(self.from_own_acc_loc," ")
        # self.hit_spacebar(self.from_own_acc_loc)



    # check successful login
    def get_welcome_msg(self):
        # self.contains_text(self.welcome_loc,self.welcome_msg)
        return self.is_visible(self.welcome_loc)
















