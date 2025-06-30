from time import sleep

from selenium.webdriver.common.by import By

from Base.utilities import Utilities


class MerchantLogin(Utilities):
    # locators
    username_loc = (By.XPATH, "//input[@id='username']")
    password_loc = (By.XPATH, "//input[@id='password']")
    # logout_flag_loc = (By.CSS_SELECTOR, "//p[@class='mt-2 text-center text-sm font-light']")
    logout_flag_loc = (By.XPATH, "//div[contains(text(),'Logout successful...')]")
    logout_flag_msg = "Login"
    invalid_login_flag_loc = (By.XPATH, "(//p[@class='my-1.5 min-h-1 text-[10px] text-red-500'])[1]")
    submit_btn_loc = (By.XPATH, "//button[normalize-space()='Submit']")
    submit_2FA_btn_loc = (By.XPATH, "(//button[normalize-space()='Submit'])[1]")
    token_loc_1 = (By.XPATH, "// input[@ type='text'][1]")
    token_loc_2 = (By.XPATH, "// input[@ type='text'][2]")
    token_loc_3 = (By.XPATH, "// input[@ type='text'][3]")
    token_loc_4 = (By.XPATH, "// input[@ type='text'][4]")
    token_loc_5 = (By.XPATH, "// input[@ type='text'][5]")
    token_loc_6 = (By.XPATH, "// input[@ type='text'][6]")
    token_loc_7 = (By.XPATH, "// input[@ type='text'][7]")
    token_loc_8 = (By.XPATH, "// input[@ type='text'][8]")
    token_err_loc = (By.CSS_SELECTOR, "p[class='mb-3 mt-1.5 min-h-1 text-[10px] text-red-500']")
    twoFA_loc = (By.XPATH, "//div[contains(text(),'Credentials validated')]")


    def __init__(self, driver):
        # Call constructor of parent class
        super().__init__(driver)

    # create login function
    def login(self, username, password):
        self.type_something(self.username_loc, username)
        self.type_something(self.password_loc, password)
        self.click_something(self.submit_btn_loc)
        # sleep(10)
        # self.type_something(self.token_loc)

    # create 2FA function
    def enter2FA(self,valid_token):
        # type digits of the token
        digit = list(valid_token)
        self.type_something(self.token_loc_1,digit[0])
        self.type_something(self.token_loc_2, digit[1])
        self.type_something(self.token_loc_3, digit[2])
        self.type_something(self.token_loc_4, digit[3])
        self.type_something(self.token_loc_5, digit[4])
        self.type_something(self.token_loc_6, digit[5])
        self.type_something(self.token_loc_7, digit[6])
        self.type_something(self.token_loc_8, digit[7])

        # submit 2FA
        self.click_something(self.submit_2FA_btn_loc)

    def get_token_err_msg(self):
        return self.get_text(self.token_err_loc)

    def get_logout_flag(self):
        return self.is_visible(self.logout_flag_loc)

    def first_level_auth(self):
        return self.is_visible(self.twoFA_loc)

    def check_invalid_credentials(self):
        # return str(self.get_text(self.invalid_login_flag_loc))
        contenter = self.get_text(self.invalid_login_flag_loc)
        print(contenter)
        # return self.is_visible(self.invalid_login_flag_loc)




















