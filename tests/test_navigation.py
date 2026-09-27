from pages.pages import MainPage, AccountPage, LoginPage


def test_go_to_personal_account(logged_in_driver):
    main_page = MainPage(logged_in_driver)
    main_page.click_header_account()
    main_page.wait_for_url("/account")
    assert main_page.current_path() == "/account"


def test_go_to_constructor_via_menu_link(logged_in_driver):
    main_page = MainPage(logged_in_driver)
    main_page.click_header_account()
    main_page.wait_for_url("/account")

    main_page.click_header_constructor()
    main_page.wait_for_url("/")
    assert main_page.current_path() == "/"


def test_go_to_constructor_via_logo(logged_in_driver):
    main_page = MainPage(logged_in_driver)
    main_page.click_header_account()
    main_page.wait_for_url("/account")

    main_page.click_logo()
    main_page.wait_for_url("/")
    assert main_page.current_path() == "/"


def test_logout(logged_in_driver):
    main_page = MainPage(logged_in_driver)
    main_page.click_header_account()
    main_page.wait_for_url("/account")

    account_page = AccountPage(logged_in_driver)
    account_page.click_logout()

    login_page = LoginPage(logged_in_driver)
    login_page.wait_for_url("/login")
    assert login_page.current_path() == "/login"
