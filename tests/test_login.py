from pages.pages import MainPage, LoginPage, RegisterPage, ForgotPasswordPage


def _register_via_ui(driver, user_data):
    """Регистрирует нового пользователя через форму регистрации (только UI)."""
    register_page = RegisterPage(driver)
    register_page.open_register_page()
    register_page.fill_form(user_data["name"], user_data["email"], user_data["password"])
    register_page.submit()
    register_page.wait_for_url("/login")


def test_login_from_main_page_button(driver, user_data):
    _register_via_ui(driver, user_data)

    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_login_button()

    login_page = LoginPage(driver)
    login_page.wait_for_login_form()
    login_page.login(user_data["email"], user_data["password"])

    login_page.wait_for_url("/")
    assert login_page.current_path() == "/"


def test_login_via_personal_account_button(driver, user_data):
    _register_via_ui(driver, user_data)

    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_header_account()

    # Неавторизованного пользователя "Личный кабинет" ведёт на форму входа.
    login_page = LoginPage(driver)
    login_page.wait_for_login_form()
    login_page.login(user_data["email"], user_data["password"])

    # После успешного входа сайт возвращает на главную (конструктор) —
    # так же, как и через остальные точки входа, — а не сразу в личный
    # кабинет. Чтобы убедиться, что вход действительно выполнен, переходим
    # в личный кабинет ещё раз: при неудачном входе нас снова перекинуло
    # бы на форму логина, а не на "/account".
    login_page.wait_for_url("/")
    main_page.click_header_account()
    main_page.wait_for_url("/account")
    assert main_page.current_path() == "/account"


def test_login_via_link_in_registration_form(driver, user_data):
    _register_via_ui(driver, user_data)

    register_page = RegisterPage(driver)
    register_page.open_register_page()
    register_page.click_login_link()

    login_page = LoginPage(driver)
    login_page.wait_for_url("/login")
    login_page.login(user_data["email"], user_data["password"])

    login_page.wait_for_url("/")
    assert login_page.current_path() == "/"


def test_login_via_link_in_forgot_password_form(driver, user_data):
    _register_via_ui(driver, user_data)

    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open_forgot_password_page()
    forgot_password_page.click_login_link()

    login_page = LoginPage(driver)
    login_page.wait_for_url("/login")
    login_page.login(user_data["email"], user_data["password"])

    login_page.wait_for_url("/")
    assert login_page.current_path() == "/"
