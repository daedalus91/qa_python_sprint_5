import random
import string

DOMAINS = ["ya.ru", "yandex.ru", "mail.ru"]


def generate_login(prefix: str = "dmitry_stelmah_54") -> str:
    random_digits = "".join(random.choices(string.digits, k=3))
    domain = random.choice(DOMAINS)
    return f"{prefix}_{random_digits}@{domain}"


def generate_simple_email(login: str = "123") -> str:
    random_suffix = "".join(random.choices(string.digits, k=6))
    domain = random.choice(DOMAINS)
    return f"{login}{random_suffix}@{domain}"


def generate_password(length: int = 8) -> str:
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def generate_invalid_password(length: int = 4) -> str:
    if length >= 6:
        length = 5
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def generate_name(length: int = 6) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length)).capitalize()

