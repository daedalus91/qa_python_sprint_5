from pages.pages import MainPage


class TestConstructorTabs:
    def test_switching_to_bun_tab_activates_it(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
 
        main_page.click_sauce_tab()
        main_page.click_bun_tab()
 
        active_tab = main_page.wait_bun_tab_active()
        assert active_tab.is_displayed()
 
    def test_sauce_tab_becomes_active(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
 
        main_page.click_sauce_tab()
 
        active_tab = main_page.wait_sauce_tab_active()
        assert active_tab.is_displayed()
 
    def test_filling_tab_becomes_active(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
 
        main_page.click_filling_tab()
 
        active_tab = main_page.wait_filling_tab_active()
        assert active_tab.is_displayed()

