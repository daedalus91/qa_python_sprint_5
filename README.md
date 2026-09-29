# Автотесты для Stellar Burgers

Автотесты для сайта
[stellarburgers.education-services.ru](https://stellarburgers.education-services.ru/).

## Что покрыто

- **Регистрация** (`tests/test_registration.py`)
  - успешная регистрация с валидными именем, email вида `логин@домен` и
    паролем от 6 символов;
  - ошибка при регистрации со слишком коротким паролем.
- **Вход в аккаунт** (`tests/test_login.py`) — все 4 точки входа на форму логина:
  - кнопка «Войти в аккаунт» на главной странице;
  - кнопка «Личный кабинет» в шапке;
  - ссылка «Войти» в форме регистрации;
  - ссылка «Войти» в форме восстановления пароля.
- **Навигация** (`tests/test_navigation.py`)
  - переход в личный кабинет по клику на «Личный кабинет»;
  - переход из личного кабинета в конструктор по ссылке «Конструктор»;
  - переход из личного кабинета в конструктор по клику на логотип;
  - выход из аккаунта по кнопке «Выйти».
- **Конструктор** (`tests/test_constructor.py`)
  - переключение вкладок «Булки», «Соусы», «Начинки».

## Структура проекта

```
sprint5/
├── pages/
│   ├── locators.py           # все локаторы, сгруппированы по страницам, с комментариями
│   └── pages.py              # Page Object классы с методами взаимодействия
├── generators.py             # генераторы логина (email), пароля, имени
├── tests/
│   ├── conftest.py           # все фикстуры проекта (driver, тестовые данные, логин через UI)
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_navigation.py
│   └── test_constructor.py
├── pytest.ini
└── README.md
```

## Запуск тестов

По умолчанию тесты запускаются в Chrome:

Для Linux

```bash
python pytest tests/
```

Для Windows

```bash
py -m pytest tests/
```

Запуск в конкретном браузере:

```bash
pytest --browser_name=chrome
pytest --browser_name=firefox
```

Запуск одного файла или теста:

```bash
pytest tests/test_registration.py
pytest tests/test_login.py::test_login_from_main_page_button
```
