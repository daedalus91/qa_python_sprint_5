from selenium.webdriver.common.by import By


class CommonLocators:
    """Элементы, встречающиеся на разных страницах сайта."""

    LOADING_OVERLAY = (By.XPATH, "//img[@alt='loading animation']")


class MainPageLocators:
    LOGO = (By.XPATH, "//header//a[@href='/'][.//*[name()='svg']]")
    # Логотип Stellar Burgers в шапке сайта, ссылка ведёт на главную "/"

    CONSTRUCTOR_LINK = (By.XPATH, "//*[normalize-space()='Конструктор']")
    # Пункт меню "Конструктор" в шапке сайта

    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//*[normalize-space()='Личный Кабинет']")
    # PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")
    # Пункт меню "Личный Кабинет" в шапке сайта

    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    # Кнопка "Войти в аккаунт" в центре главной страницы
    # (видна только неавторизованному пользователю)

    BUN_TAB = (By.XPATH, "//span[normalize-space()='Булки']/parent::*")
    # Вкладка "Булки" переключателя ингредиентов.

    SAUCE_TAB = (By.XPATH, "//span[normalize-space()='Соусы']/parent::*")
    # Вкладка "Соусы" переключателя ингредиентов

    FILLING_TAB = (By.XPATH, "//span[normalize-space()='Начинки']/parent::*")
    # Вкладка "Начинки" переключателя ингредиентов

    BUN_TAB_ACTIVE = (
        By.XPATH,
        "//*[contains(@class,'tab_tab_type_current') and .//span[normalize-space()='Булки']]",
    )
    # Вкладка "Булки" в активном состоянии

    SAUCE_TAB_ACTIVE = (
        By.XPATH,
        "//*[contains(@class,'tab_tab_type_current') and .//span[normalize-space()='Соусы']]",
    )
    # Вкладка "Соусы" в активном состоянии

    FILLING_TAB_ACTIVE = (
        By.XPATH,
        "//*[contains(@class,'tab_tab_type_current') and .//span[normalize-space()='Начинки']]",
    )
    # Вкладка "Начинки" в активном состоянии


class AuthFormLocators:
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/parent::*//input")
    # Поле "Email"

    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/parent::*//input")
    # Поле "Пароль"


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/parent::*//input")
    # Поле "Имя"

    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    # Кнопка "Зарегистрироваться"

    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")
    # Ссылка "Войти" внизу формы регистрации (ведёт на /login)

    PASSWORD_ERROR = (By.XPATH, "//*[normalize-space()='Некорректный пароль']")
    # Текст ошибки под полем пароля при некорректном (слишком коротком) пароле


class LoginPageLocators:
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    # Кнопка "Войти"

    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")
    # Ссылка "Зарегистрироваться" внизу формы входа

    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Восстановить пароль']")
    # Ссылка "Восстановить пароль" внизу формы входа


class ForgotPasswordPageLocators:
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
    # Кнопка "Восстановить"

    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")
    # Ссылка "Войти" внизу формы восстановления пароля


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//*[normalize-space()='Профиль']")
    # Пункт меню "Профиль" в боковом меню личного кабинета

    ORDER_HISTORY_LINK = (By.XPATH, "//*[normalize-space()='История заказов']")
    # Пункт меню "История заказов" в боковом меню личного кабинета

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Выйти'] | //button[normalize-space()='Выход']",
    )
    # Кнопка выхода из аккаунта в боковом меню личного кабинета
