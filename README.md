# Task Manager API

RESTful API для управления задачами с авторизацией и хранением в PostgreSQL.

## Технологии
- **Python** 3.11 / **FastAPI** (или укажите свой язык)
- **PostgreSQL** (база данных)
- **SQLAlchemy** (ORM)
- **JWT** (авторизация)
- **Docker** & **Docker Compose**

## Функциональность
- Регистрация и авторизация пользователей (JWT)
- Создание, редактирование, удаление задач
- Просмотр списка задач с фильтрацией по статусу
- Хранение данных в PostgreSQL

## Запуск проекта

### Локальный запуск
```bash
# Клонируйте репозиторий
git clone https://github.com/metsbis/task-manager-api.git

# Перейдите в папку проекта
cd task-manager-api

# Установите зависимости (если Python)
pip install -r requirements.txt

# Запустите приложение
python main.py
