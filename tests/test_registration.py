from pages.pages import RegisterPage
from generators import generate_simple_email, generate_invalid_password


def test_successful_registration(driver, user_data):
    register_page = RegisterPage(driver)
    register_page.open_register_page()

    email = generate_simple_email()
    register_page.fill_form(user_data["name"], email, user_data["password"])
    register_page.submit()

    register_page.wait_for_url("/login")
    assert register_page.current_path() == "/login"


def test_registration_with_invalid_password(driver, user_data):
    register_page = RegisterPage(driver)
    register_page.open_register_page()

    invalid_password = generate_invalid_password()
    register_page.fill_form(user_data["name"], user_data["email"], invalid_password)
    register_page.submit()

    error_text = register_page.get_password_error_text()
    assert "Некорректный пароль" in error_text

    assert register_page.current_path() == "/register"
