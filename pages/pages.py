from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import (
    CommonLocators,
    MainPageLocators,
    AuthFormLocators,
    RegisterPageLocators,
    LoginPageLocators,
    ForgotPasswordPageLocators,
    AccountPageLocators,
)

BASE_URL = "https://stellarburgers.education-services.ru"
DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, path=""):
        self.driver.get(f"{BASE_URL}{path}")

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_loading_overlay_to_disappear(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(CommonLocators.LOADING_OVERLAY))
        except TimeoutException:
            pass

    def click(self, locator):
        self.wait_for_loading_overlay_to_disappear()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_url(self, path):
        target = path.rstrip("/")
        self.wait.until(lambda d: d.current_url.replace(BASE_URL, "").rstrip("/") == target)

    def current_path(self):
        url = self.driver.current_url
        return url.replace(BASE_URL, "").rstrip("/") or "/"


class MainPage(BasePage):
    def open_main_page(self):
        self.open("/")

    def click_logo(self):
        self.click(MainPageLocators.LOGO)

    def click_header_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def click_header_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_bun_tab(self):
        self.click(MainPageLocators.BUN_TAB)

    def click_sauce_tab(self):
        self.click(MainPageLocators.SAUCE_TAB)

    def click_filling_tab(self):
        self.click(MainPageLocators.FILLING_TAB)

    def wait_bun_tab_active(self):
        return self.find(MainPageLocators.BUN_TAB_ACTIVE)

    def wait_sauce_tab_active(self):
        return self.find(MainPageLocators.SAUCE_TAB_ACTIVE)

    def wait_filling_tab_active(self):
        return self.find(MainPageLocators.FILLING_TAB_ACTIVE)


class RegisterPage(BasePage):
    def open_register_page(self):
        self.open("/register")

    def fill_form(self, name, email, password):
        self.type_text(RegisterPageLocators.NAME_INPUT, name)
        self.type_text(AuthFormLocators.EMAIL_INPUT, email)
        self.type_text(AuthFormLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(RegisterPageLocators.SUBMIT_BUTTON)

    def click_login_link(self):
        self.click(RegisterPageLocators.LOGIN_LINK)

    def get_password_error_text(self):
        return self.find(RegisterPageLocators.PASSWORD_ERROR).text


class LoginPage(BasePage):
    def open_login_page(self):
        self.open("/login")

    def wait_for_login_form(self):
        self.find(AuthFormLocators.EMAIL_INPUT)

    def fill_form(self, email, password):
        self.type_text(AuthFormLocators.EMAIL_INPUT, email)
        self.type_text(AuthFormLocators.PASSWORD_INPUT, password)

    def submit(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def login(self, email, password):
        self.fill_form(email, password)
        self.submit()

    def click_register_link(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)


class ForgotPasswordPage(BasePage):
    def open_forgot_password_page(self):
        self.open("/forgot-password")

    def click_login_link(self):
        self.click(ForgotPasswordPageLocators.LOGIN_LINK)


class AccountPage(BasePage):
    def click_logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
