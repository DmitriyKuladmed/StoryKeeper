# StoryKeeper

**StoryKeeper** — это API для управления книгами, авторами, жанрами и их бронированием. API предоставляет возможности для создания, чтения, обновления и удаления данных, а также для фильтрации книг по различным критериям.

## Содержание

- [Установка и запуск](#установка-и-запуск)
  - [С использованием Docker Compose](#с-использованием-docker-compose)
- [API](#api)
  - [Книги](#книги)
  - [Авторы](#авторы)
  - [Жанры](#жанры)
  - [Бронирования](#бронирования)
- [Тестовые данные](#тестовые-данные)
  - [Пользователи](#пользователи)
  - [Жанры](#жанры-1)
  - [Книги](#книги-1)
  - [Бронирования](#бронирования-1)

## Установка и запуск

### С использованием Docker Compose

Для запуска **StoryKeeper** с помощью Docker Compose выполните следующие шаги:

1. **Клонируйте репозиторий**

    ```bash
    git clone https://github.com/yourusername/storykeeper.git
    cd storykeeper
    ```

2. **Запустите Docker Compose**

    ```bash
    docker-compose up --build
    ```

    Это создаст и запустит контейнеры для приложения и базы данных. Приложение будет доступно по адресу `http://localhost:8000`.

## API

### Книги

- **Получить все книги**

    ```http
    GET /books/
    ```

- **Создать книгу**

    ```http
    POST /books/
    ```

    **Тело запроса:**

    ```json
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "cost": 499,
        "pages": 223,
        "author_id": 1,
        "genre_ids": [1]
    }
    ```

- **Получить книгу по ID**

    ```http
    GET /books/{book_id}
    ```

- **Фильтрация книг**

    - Получить книги по автору

        ```http
        GET /books/?author_id=1
        ```

    - Получить книги по жанрам

        ```http
        GET /books/?genre_ids=1&genre_ids=2
        ```

    - Получить книги в определенном ценовом диапазоне

        ```http
        GET /books/?min_cost=100&max_cost=500
        ```

    - Комбинированный фильтр

        ```http
        GET /books/?author_id=1&genre_ids=1&min_cost=100&max_cost=500
        ```

### Авторы

- **Получить всех авторов**

    ```http
    GET /users/
    ```

- **Создать автора**

    ```http
    POST /users/
    ```

    **Тело запроса:**

    ```json
    {
        "first_name": "J.K.",
        "last_name": "Rowling",
        "avatar": "rowling_avatar.jpg"
    }
    ```

### Жанры

- **Получить все жанры**

    ```http
    GET /genres/
    ```

- **Создать жанр**

    ```http
    POST /genres/
    ```

    **Тело запроса:**

    ```json
    {
        "name": "Fantasy"
    }
    ```

### Бронирования

- **Создать бронирование**

    ```http
    POST /reservations/
    ```

    **Тело запроса:**

    ```json
    {
        "book_id": 1,
        "user_id": 4,
        "start_date": "2024-07-20T10:00:00",
        "end_date": "2024-07-25T10:00:00",
        "active": true
    }
    ```

- **Получить все бронирования**

    ```http
    GET /reservations/
    ```

- **Получить бронирование по ID**

    ```http
    GET /reservations/{reservation_id}
    ```

- **Отменить бронирование**

    ```http
    DELETE /reservations/{reservation_id}
    ```

## Тестовые данные (добавление данных происходит по отдельности, по 1 записи)

### Пользователи

```json
[
    {
        "first_name": "J.K.",
        "last_name": "Rowling",
        "avatar": "rowling_avatar.jpg"
    },
    {
        "first_name": "George",
        "last_name": "Orwell",
        "avatar": "orwell_avatar.jpg"
    },
    {
        "first_name": "J.R.R.",
        "last_name": "Tolkien",
        "avatar": "tolkien_avatar.jpg"
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "avatar": "john_doe_avatar.jpg"
    }
]
```

### Жанры
```json
[
    {
        "name": "Fantasy"
    },
    {
        "name": "Science Fiction"
    },
    {
        "name": "Dystopian"
    }
]
```

### Книги
```json
[
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "cost": 499,
        "pages": 223,
        "author_id": 1,
        "genre_ids": [1]
    },
    {
        "title": "1984",
        "cost": 299,
        "pages": 328,
        "author_id": 2,
        "genre_ids": [3]
    },
    {
        "title": "The Hobbit",
        "cost": 399,
        "pages": 310,
        "author_id": 3,
        "genre_ids": [1]
    }
]
```
### Бронирования
```json
[
    {
        "book_id": 1,
        "user_id": 4,
        "start_date": "2024-07-20T10:00:00",
        "end_date": "2024-07-25T10:00:00",
        "active": true
    },
    {
        "book_id": 2,
        "user_id": 4,
        "start_date": "2024-07-15T12:00:00",
        "end_date": "2024-07-20T12:00:00",
        "active": false
    }
]
```

