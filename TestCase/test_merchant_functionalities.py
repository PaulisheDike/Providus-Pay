import unittest
import pytest
from time import sleep  # If needed
from Pages.merchant_home_page import MerchantHome
from Pages.merchant_login_page import MerchantLogin
from Pages.merchant_single_transfer_page import MerchantSingleTransfer
from configTest import *

@pytest.mark.usefixtures("browser_setup")
class TestMerchantPortal(unittest.TestCase):
    expected_token_err = "Invalid Token"
    expected_invalid_credential_err = "Invalid Username/Password! Make sure username/password is correct."

    def setUp(self):
        self.driver.get(baseUrl)  # Navigate to base URL in setUp
        self.merchantLogin = MerchantLogin(self.driver)
        self.merchantHome = MerchantHome(self.driver)
        self.singleTransfer = MerchantSingleTransfer(self.driver)

    def tearDown(self):
        # DO NOT call driver.quit() here. The fixture handles it.
        pass

    def test_valid_login(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.assertTrue(self.merchantLogin.first_level_auth())

    def test_invalid_login(self):
        self.merchantLogin.login(invalid_m_username, invalid_m_password)
        actual_result = self.merchantLogin.check_invalid_credentials
        sleep(5)
        print(str(actual_result))

    def test_valid_2FA(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(valid_token)
        sleep(5)
        self.assertTrue(self.merchantHome.get_welcome_msg())
        self.merchantHome.logout()

    def test_invalid_2FA(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(invalid_token)
        actual_result = self.merchantLogin.get_token_err_msg()
        assert actual_result == self.expected_token_err

    def test_valid_combined_authentication(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(valid_token)
        sleep(5)
        self.assertTrue(self.merchantHome.get_welcome_msg())
        self.merchantHome.logout()

    def test_invalid_combined_authentication(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(invalid_token)
        actual_result = self.merchantLogin.get_token_err_msg()
        assert actual_result == self.expected_token_err

    def test_logout(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(valid_token)
        sleep(5)
        self.merchantHome.logout()
        self.assertTrue(self.merchantLogin.get_logout_flag())

    def test_single_to_own_account(self):
        self.merchantLogin.login(valid_m_username0, valid_m_password0)
        self.merchantLogin.enter2FA(valid_token)
        self.singleTransfer.my_own_account()
        self.merchantHome.logout()