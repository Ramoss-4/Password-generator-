import random
import string
from cryptography.fernet import Fernet
import locale
import sys

# Установка кодировки для ввода и вывода
locale.setlocale(locale.LC_ALL, '')
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Генерация и загрузка ключа для шифрования паролей
def get_encryption_key():
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
            if len(key) != 44:
                raise ValueError("Ключ неверной длины")
    except (FileNotFoundError, ValueError):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

# Определение параметров пароля
def define_password_parameters():
    while True:
        length = int(input('Введите длину пароля (не менее 8 символов): '))
        if length < 8:
            print("Ошибка: Длина пароля должна быть не менее 8 символов.")
        else:
            break
    use_special_chars = input('Использовать специальные символы? (да/нет): ').lower() == 'да'
    exclude_ambiguous = input('Исключить неоднозначные символы? (да/нет): ').lower() == 'да'
    pronounceable = input('Сделать пароль произносимым? (да/нет): ').lower() == 'да'
    avoid_repeated_chars = input('Исключить повторяющиеся символы? (да/нет): ').lower() == 'да'

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    if exclude_ambiguous:
        characters = characters.replace('0', '').replace('O', '').replace('l', '').replace('I', '')
    return length, characters, pronounceable, avoid_repeated_chars

# Генерация пароля
def generate_password(length, characters, pronounceable=False, avoid_repeated_chars=False):
    password = []
    if pronounceable:
        vowels, consonants = "aeiou", ''.join(set(characters) - set("aeiou"))
        while len(password) < length:
            password.extend([random.choice(consonants), random.choice(vowels)])
            if len(password) > length:
                password = password[:length]
    else:
        while len(password) < length:
            new_char = random.choice(characters)
            # Проверка на повторяющиеся символы
            if not (avoid_repeated_chars and password and password[-1] == new_char):
                password.append(new_char)
    return ''.join(password)

# Проверка пароля
def verify_password(password):
    return len(password) >= 8

# Сохранение пароля
def save_password(password, key, filename="passwords.enc"):
    fernet = Fernet(key)
    with open(filename, "ab") as file:
        file.write(fernet.encrypt(password.encode()) + b'\n')

# Возвращение результата пользователю
def return_password_to_user(num, password):
    return f"Hello, {num}, your password is: {password}"

# Основной процесс генерации пароля
def password_generator_pipeline():
    num = input('login: ')
    length, characters, pronounceable, avoid_repeated_chars = define_password_parameters()
    password = generate_password(length, characters, pronounceable, avoid_repeated_chars)
    
    if verify_password(password):
        key = get_encryption_key()
        save_password(password, key)
        return return_password_to_user(num, password)
    else:
        raise ValueError("Пароль не прошел проверку")

# Пример использования
print(password_generator_pipeline())
