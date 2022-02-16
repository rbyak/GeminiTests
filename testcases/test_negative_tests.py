import pytest

from constants.company_type import Company_Type
from constants.countries import country_name
from pages.sandbox_landing_page import SandboxLandingPage
from utilities.random_alphanumeric import RandomAlphaNumeric


@pytest.mark.usefixtures("setup")
class TestNegative:

    def test_cannot_create_account_with_empty_company_name(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        create_business_account_page.choose_company_type(Company_Type.PUBLICLY_TRADING_COMPANY)
        create_business_account_page.choose_country_type(country_name.USA)
        create_business_account_page.set_legal_first_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_middle_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_last_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_email_address(
            RandomAlphaNumeric.random_str(5) + '@' + RandomAlphaNumeric.random_str(5) + '.com')
        create_business_account_page.set_agreement_checkbox()
        create_business_account_page.click_submit_expecting_error()
        try:
            assert create_business_account_page.is_alert_present("Legal Business Name is required.")
        except AssertionError as e:
            raise (AssertionError("Alert was not detected"))

    def test_cannot_create_account_with_empty_first_name(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        create_business_account_page.set_company_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.choose_company_type(Company_Type.PUBLICLY_TRADING_COMPANY)
        create_business_account_page.choose_country_type(country_name.USA)
        create_business_account_page.set_legal_middle_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_last_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_email_address(
            RandomAlphaNumeric.random_str(5) + '@' + RandomAlphaNumeric.random_str(5) + '.com')
        create_business_account_page.set_agreement_checkbox()
        create_business_account_page.click_submit_expecting_error()
        try:
            assert create_business_account_page.is_alert_present("Legal First Name is required.")
        except AssertionError as e:
            raise (AssertionError("Alert was not detected"))

    def test_cannot_create_account_with_empty_last_name(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        create_business_account_page.set_company_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.choose_company_type(Company_Type.PUBLICLY_TRADING_COMPANY)
        create_business_account_page.choose_country_type(country_name.USA)
        create_business_account_page.set_legal_first_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_middle_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_email_address(
            RandomAlphaNumeric.random_str(5) + '@' + RandomAlphaNumeric.random_str(5) + '.com')
        create_business_account_page.set_agreement_checkbox()
        create_business_account_page.click_submit_expecting_error()
        try:
            assert create_business_account_page.is_alert_present("Legal Last Name is required.")
        except AssertionError as e:
            raise (AssertionError("Alert was not detected"))

    def test_cannot_create_account_without_email(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        create_business_account_page.set_company_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.choose_company_type(Company_Type.PUBLICLY_TRADING_COMPANY)
        create_business_account_page.choose_country_type(country_name.USA)
        create_business_account_page.set_legal_first_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_middle_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_agreement_checkbox()
        create_business_account_page.click_submit_expecting_error()
        try:
            assert create_business_account_page.is_alert_present("Email is required.")
        except AssertionError as e:
            raise (AssertionError("Alert was not detected"))

    def test_cannot_create_account_without_checkbox(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        create_business_account_page.set_company_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.choose_company_type(Company_Type.PUBLICLY_TRADING_COMPANY)
        create_business_account_page.choose_country_type(country_name.USA)
        create_business_account_page.set_legal_first_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_middle_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_legal_last_name(RandomAlphaNumeric.random_str(10))
        create_business_account_page.set_email_address(
            RandomAlphaNumeric.random_str(5) + '@' + RandomAlphaNumeric.random_str(5) + '.com')
        create_business_account_page.click_submit_expecting_error()
        try:
            assert create_business_account_page.is_alert_present("User Agreement is required.")
        except AssertionError as e:
            raise (AssertionError("Alert was not detected"))
