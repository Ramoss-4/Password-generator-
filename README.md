# Password Generator

Этот проект представляет собой утилиту для генерации паролей. Он позволяет пользователям настраивать параметры паролей, такие как длина, использование строчных и заглавных букв, цифр и специальных символов, а также создавать настраиваемые пароли.

## Оглавление

1. [Описание](#Описание)
2. [Требования](#Требования)
3. [Установка](#Установка)
4. [Использование](#Использование)
5. [Функции](#Функции)
6. [Пример использования](#Пример-использования)
7. [Лицензия](#Лицензия)

## Описание

Скрипт включает следующие функции:

### Генерация произвольного пароля (`generate_password`)
Создает произвольный пароль, состоящий из букв (заглавных и строчных), цифр и специальных символов.

### Генерация числового пароля (`generate_numeric_password`)
Создает пароль, состоящий только из цифр.

### Генерация буквенного пароля (`generate_alphabetic_password`)
Создает пароль, состоящий только из букв (заглавных и строчных).

### Генерация пароля из строчных букв (`generate_lowercase_password`)
Создает пароль, состоящий только из строчных букв.

### Генерация пароля из заглавных букв (`generate_uppercase_password`)
Создает пароль, состоящий только из заглавных букв.

### Генерация буквенно-цифрового пароля (`generate_alphanumeric_password`)
Создает пароль, состоящий из букв (заглавных и строчных) и цифр.

### Генерация пароля из специальных символов (`generate_special_characters_password`)
Создает пароль, состоящий только из специальных символов.

### Генерация настраиваемого пароля (`generate_custom_password`)
Позволяет пользователю выбрать, какие типы символов будут использоваться: строчные и заглавные буквы, цифры и специальные символы.

## Требования

- Python 3.x

## Установка

Для использования данного скрипта требуется Python версии 3.x.

1. Скачайте и распакуйте проект на свой компьютер.
2. Откройте терминал или командную строку и перейдите в директорию проекта.
3. Запустите программу командой:
    ```bash
    python password_generator.py
    ```

## Использование

После запуска программы пользователю будет предложено выбрать тип пароля и задать его длину. Пользователь может выбрать один из следующих типов паролей:

1. Произвольный пароль
2. Числовой пароль
3. Буквенный пароль
4. Пароль из строчных букв
5. Пароль из заглавных букв
6. Буквенно-цифровой пароль
7. Пароль из специальных символов
8. Настраиваемый пароль

Для выбора пользователю необходимо ввести соответствующий номер и нажать Enter. Далее будет предложено ввести длину пароля.

В случае выбора настраиваемого пароля пользователь также сможет указать, использовать ли строчные буквы, заглавные буквы, цифры и специальные символы.

## Функции

### Генерация произвольного пароля

Функция `generate_password` генерирует пароль, состоящий из букв (заглавных и строчных), цифр и специальных символов.

```python
def generate_password(self, length):
    characters = string.ascii_letters + string.digits + self.special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация числового пароля

Функция `generate_numeric_password` генерирует пароль, состоящий только из цифр.

```python
def generate_numeric_password(self, length):
    characters = string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация буквенного пароля

Функция `generate_alphabetic_password` генерирует пароль, состоящий только из букв (заглавных и строчных).

```python
def generate_alphabetic_password(self, length):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация пароля из строчных букв

Функция `generate_lowercase_password` генерирует пароль, состоящий только из строчных букв.

```python
def generate_lowercase_password(self, length):
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация пароля из заглавных букв

Функция `generate_uppercase_password` генерирует пароль, состоящий только из заглавных букв.

```python
def generate_uppercase_password(self, length):
    characters = string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация буквенно-цифрового пароля

Функция `generate_alphanumeric_password` генерирует пароль, состоящий из букв (заглавных и строчных) и цифр.

```python
def generate_alphanumeric_password(self, length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### Генерация пароля из специальных символов

Функция `generate_special_characters_password` генерирует пароль, состоящий только из специальных символов.

```python
def generate_special_characters_password(self, length):
    password = ''.join(random.choice(self.special_characters) for _ in range(length))
    return password
```

### Генерация настраиваемого пароля

Функция `generate_custom_password` позволяет пользователю выбрать, какие типы символов будут использоваться для генерации пароля.

```python
def generate_custom_password(self, length, use_lowercase, use_uppercase, use_digits, use_special):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += self.special_characters

    if not characters:
        raise ValueError("At least one type of character must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

## Пример использования

Пример сессии генерации пароля:

```plaintext
Выберите тип пароля:
1. Произвольный пароль
2. Числовой пароль
3. Буквенный пароль
4. Пароль из строчных букв
5. Пароль из заглавных букв
6. Буквенно-цифровой пароль
7. Пароль из специальных символов
8. Настраиваемый пароль
0. Выход
Ваш выбор: 1
Введите длину пароля: 12
Пароль: Ab1!Cd2@Ef3#
```

Скрипт сгенерирует пароль на основе выбранных параметров и выведет его на экран.

## Лицензия

Этот проект лицензирован на условиях MIT License.