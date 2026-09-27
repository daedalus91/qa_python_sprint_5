import sys
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.pages import RegisterPage, LoginPage
from generators import generate_login, generate_password, generate_name


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox",
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_driver = webdriver.Chrome(options=options)
        yield chrome_driver
        chrome_driver.quit()

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        firefox_driver = webdriver.Firefox(options=options)
        yield firefox_driver
        firefox_driver.quit()

    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")


@pytest.fixture()
def user_data():
    return {
        "name": generate_name(),
        "email": generate_login(),
        "password": generate_password(),
    }


@pytest.fixture()
def logged_in_driver(driver, user_data):
    register_page = RegisterPage(driver)
    register_page.open_register_page()
    register_page.fill_form(user_data["name"], user_data["email"], user_data["password"])
    register_page.submit()
    register_page.wait_for_url("/login")

    login_page = LoginPage(driver)
    login_page.login(user_data["email"], user_data["password"])
    login_page.wait_for_url("/")

    return driver
