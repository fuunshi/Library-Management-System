# Django Library Management API

This Django API provides endpoints for managing users, books, and borrowed books in a library system.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fuunshi/Library-Management-System.git
    cd Library-Management-System/server
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Docker
- You may also use docker for running
- `docker-compose build`
- `docker-compose up`


## Assumptions

- This API assumes that userID, bookID, detailID and so on are integers which are auto generated.
- Youre not fetching from browser url directly and using tools like `curl, http`
- This guide assumes you are using linux based OS.

## API Authorization

- This application uses Token Authorization of REST framework
- To disable token authorization comment out the token authorization middleware in settings.py
- `'bookmanager.middleware.TokenAuthorizationMiddleware'` is the middleware which verifies each token.

### How to get token

- Create a user either superuser(using manage.py) or user(from admin)
- To create super user:
```bash
python3 manage.py createsuperuser
```
- Fill out the given field
- Run the following lines of code in `python3 manage.py shell`
```py
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user = User.objects.get(username='your_username')  # Replace 'your_username' with an existing username
token, created = Token.objects.get_or_create(user=user)
print(f'Token for user {user.username}: {token.key}')
```
- Using tokens in http fetch a GET operation:
```bash
http GET $apiUrl "Authorization: Token `$tokenHere`"
```

## API Endpoints

- URL : `http://127.0.0.1:8000/api/`

### Users

#### 1. Create User

- **Endpoint:** `/create-user/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "membershipDate": "YYYY-MM-DD"
    }
    ```
- **Response Example:**
    ```json
    {
        "UserID": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "membershipDate": "YYYY-MM-DD"
    }
    ```

#### 2. List Users

- **Endpoint:** `/users/`
- **Method:** `GET`
- **Response Example:**
    ```json
    [
        {
            "UserID": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "membershipDate": "YYYY-MM-DD"
        },
        ...
    ]
    ```

#### 3. User Detail

- **Endpoint:** `/users/<UserID>/`
- **Method:** `GET`
- **Response Example:**
    ```json
    {
        "UserID": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "membershipDate": "YYYY-MM-DD"
    }
    ```

### Books

#### 1. Create Book

- **Endpoint:** `/create-book/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "title": "The Great Gatsby",
        "ISBN": "1234567890123",
        "publishedDate": "YYYY-MM-DD",
        "genre": "Fiction"
    }
    ```
- **Response Example:**
    ```json
    {
        "bookID": 1,
        "title": "The Great Gatsby",
        "ISBN": "1234567890123",
        "publishedDate": "YYYY-MM-DD",
        "genre": "Fiction"
    }
    ```

#### 2. List Books

- **Endpoint:** `/books/`
- **Method:** `GET`
- **Response Example:**
    ```json
    [
        {
            "bookID": 1,
            "title": "The Great Gatsby",
            "ISBN": "1234567890123",
            "publishedDate": "YYYY-MM-DD",
            "genre": "Fiction"
        },
        ...
    ]
    ```

#### 3. Book Detail

- **Endpoint:** `/books/<BookID>/`
- **Method:** `GET`
- **Response Example:**
    ```json
    {
        "bookID": 1,
        "title": "The Great Gatsby",
        "ISBN": "1234567890123",
        "publishedDate": "YYYY-MM-DD",
        "genre": "Fiction"
    }
    ```

#### 4. Assign/Update Book Details

- **Endpoint:** `/book-details/<int:bookID>/`
- **Methods:** `POST`, `PUT`
- **Request Body:**
    ```json
    {
        "numberOfPages": 300,
        "publisher": "Publisher XYZ",
        "language": "English"
    }
    ```
- **Response Example:**
    ```json
    {
        "detailsID": 1,
        "bookID": 1,
        "numberOfPages": 300,
        "publisher": "Publisher XYZ",
        "language": "English"
    }
    ```

### Borrowed Books

#### 1. Borrow Book

- **Endpoint:** `/borrow-book/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "userID": 1,
        "bookID": 1,
        "borrowDate": "YYYY-MM-DD",
        "returnDate": "YYYY-MM-DD"
    }
    ```
- **Response Example:**
    ```json
    {
        "userID": 1,
        "bookID": 1,
        "borrowDate": "YYYY-MM-DD",
        "returnDate": "YYYY-MM-DD"
    }
    ```

#### 2. Return Book

- **Endpoint:** `/return-book/<int:borrow_id>/`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "returnDate": "YYYY-MM-DD"
    }
    ```
- **Response Example:**
    ```json
    {
        "message": "Book returned successfully"
    }
    ```

#### 3. List Borrowed Books

- **Endpoint:** `/list-borrowed-books/`
- **Method:** `GET`
- **Response Example:**
    ```json
    [
        {
            "id": 1,
            "userID": 1,
            "bookID": 1,
            "borrowDate": "YYYY-MM-DD",
            "returnDate": "YYYY-MM-DD"
        },
        ...
    ]
    ```
