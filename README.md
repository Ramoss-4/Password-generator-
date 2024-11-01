# Password Generator

Этот проект представляет собой утилиту для генерации и шифрования паролей. Она позволяет пользователям настраивать параметры паролей, такие как длина, наличие специальных символов и многое другое. Сгенерированные пароли шифруются с использованием библиотеки cryptography.fernet и сохраняются в файл.

## Оглавление

1. [Описание](#Описание)
2. [Требования](#Требования)
3. [Установка](#Установка)
4. [Использование](#Использование)
5. [Функции](#Функции)
6. [Пример Использования](#Пример-Использования)
7. [Лицензия](#Лицензия)

## Описание

Скрипт включает следующие функции:

### Генерация и загрузка ключа для шифрования паролей (`get_encryption_key`)
Создает новый ключ шифрования или загружает существующий из файла secret.key. Если файл или ключ неверной длины отсутствует, создается новый ключ и сохраняется в файл.

### Определение параметров пароля (`define_password_parameters`)
Пользователь задает параметры пароля:
- Длина пароля (не менее 8 символов)
- Использование специальных символов
- Исключение неоднозначных символов
- Произносимость пароля
- Исключение повторяющихся символов

### Генерация пароля (`generate_password`)
Создает пароль на основе заданных параметров. Поддерживает создание произносимых паролей и исключение повторяющихся символов.

### Проверка пароля (`verify_password`)
Убеждается, что длина пароля составляет не менее 8 символов.

### Сохранение пароля (`save_password`)
Шифрует и сохраняет пароль в файл passwords.enc.

### Возвращение результата пользователю (`return_password_to_user`)
Возвращает сгенерированный пароль пользователю с приветственным сообщением.

## Требования

- Python 3.x
- Библиотека cryptography

## Установка

Установите необходимые библиотеки:
```pip install cryptography```
## Использование

1. Запустите скрипт:
```python password_generator.py```
3. Следуйте инструкциям для определения параметров пароля и генерации нового пароля.

## Функции

### Генерация и загрузка ключа для шифрования паролей

Функция `get_encryption_key` генерирует новый ключ для шифрования паролей или загружает существующий из файла `secret.key`. Если файл не найден или ключ неправильной длины, создается новый ключ.

```python
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
```

### Определение параметров пароля

Функция `define_password_parameters` запрашивает у пользователя параметры для генерации пароля.

```python
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
```

### Генерация пароля

Функция `generate_password` создает пароль на основе заданных параметров.

```python
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
            if not (avoid_repeated_chars and password and password[-1] == new_char):
                password.append(new_char)
    return ''.join(password)
```

### Проверка пароля

Функция `verify_password` проверяет, что длина пароля составляет не менее 8 символов.

```python
def verify_password(password):
    return len(password) >= 8
```

### Сохранение пароля

Функция `save_password` шифрует и сохраняет пароль в файл `passwords.enc`.

```python
def save_password(password, filename, key):
    fernet = Fernet(key)
    with open(filename, "ab") as file:
        file.write(fernet.encrypt(password.encode()) + b'\n')
```

### Возвращение результата пользователю

Функция `return_password_to_user` возвращает сгенерированный пароль пользователю.

```python
def return_password_to_user(num, password):
    return f"Hello, {num}, your password is: {password}"
```

## Пример использования

Пример сессии генерации пароля:

```plaintext
login: user123
Введите длину пароля (не менее 8 символов): 12
Использовать специальные символы? (да/нет): да
Исключить неоднозначные символы? (да/нет): да
Сделать пароль произносимым? (да/нет): нет
Исключить повторяющиеся символы? (да/нет): да
```

Скрипт сгенерирует пароль, проверит его и сохранит в зашифрованном виде в файл `passwords.enc`.

## Лицензия

Этот проект лицензирован на условиях MIT License.

