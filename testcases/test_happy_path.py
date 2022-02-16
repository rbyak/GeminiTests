import pytest

from constants.company_type import Company_Type
from constants.countries import country_name
from pages.sandbox_landing_page import SandboxLandingPage
from utilities.random_alphanumeric import RandomAlphaNumeric


@pytest.mark.usefixtures("setup")
class TestHappyPath:

    def test_can_view_sandbox_landing_page(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        try:
            assert sandbox_landing_page.get_title().__eq__("[Sandbox] Gemini - Sign In")
        except AssertionError as e:
            raise (AssertionError("Page has not loaded"))

    def test_can_navigate_to_registration_page_from_sandbox_page(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        try:
            assert create_new_account_page.get_title().__eq__("[Sandbox] Gemini - Register")
        except AssertionError as e:
            raise (AssertionError("Page has not loaded"))

    def test_can_navigate_to_business_registration_page_from_registration_page(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        try:
            assert create_business_account_page.get_title().__eq__("[Sandbox] Gemini - Institutional Client "
                                                                   "Registration")
        except AssertionError as e:
            raise (AssertionError("Page has not loaded"))

    def test_can_sign_up_for_business_account(self):
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
        # unfortunately I was not able to set create_business_account_page.set_agreement_checkbox()et checkbox css selector correctly so this test will fail
        thanks_page = create_business_account_page.click_submit()
        try:
            assert thanks_page.get_thanks().__eq__("Thanks for Registering!")
        except AssertionError as e:
            raise (AssertionError("Page has not loaded"))

    def test_can_view_user_agreement__for_business_page(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        url = create_business_account_page.click_User_agreement_and_return_url(
            "https://www.gemini.com/legal/user-agreement")
        try:
            assert url.__eq__("")
        except AssertionError as e:
            raise (AssertionError("User agreement page has not loaded"))

    def test_can_view_privacy_policy_for_business_page(self):
        sandbox_landing_page = SandboxLandingPage(self.driver)
        create_new_account_page = sandbox_landing_page.click_create_new_account()
        create_business_account_page = create_new_account_page.click_create_business_account()
        url = create_business_account_page.click_User_agreement_and_return_url(
            "https://www.gemini.com/legal/privacy-policy")
        try:
            assert url.__eq__("")
        except AssertionError as e:
            raise (AssertionError("privacy policy] page has not loaded"))
