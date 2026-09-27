from pages.pages import MainPage


def test_bun_tab_becomes_active(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_bun_tab()
    main_page.wait_bun_tab_active()


def test_sauce_tab_becomes_active(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_sauce_tab()
    main_page.wait_sauce_tab_active()


def test_filling_tab_becomes_active(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_filling_tab()
    main_page.wait_filling_tab_active()
