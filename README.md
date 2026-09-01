# Evgeni

Мой основной Python-проект.

## Требования

- Python 3.14+

## Установка

Создать виртуальное окружение:

    python3 -m venv .venv
    source .venv/bin/activate

Установить проект и инструменты разработки:

    python -m pip install -e ".[dev]"

## Запуск

    python -m evgeni.main

## Тестирование

    pytest

## Проверка кода

    ruff check .
    black --check .
