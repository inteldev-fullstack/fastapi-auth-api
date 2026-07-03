# FastAPI Auth API

A clean FastAPI authentication API with user registration, login, JWT tokens and protected routes.

## Features

- User registration
- User login
- JWT access token
- Protected `/me` route
- SQLite database
- SQLAlchemy ORM
- Password hashing with bcrypt
- Auto API docs with Swagger
- Basic automated tests

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Passlib / bcrypt
- Pytest

## Project Structure

```text
fastapi-auth-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes.py
├── tests/
│   └── test_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

Create virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status |
| POST | `/register` | Create a new user |
| POST | `/login` | Login and get JWT token |
| GET | `/me` | Protected user profile route |

## Example User

```json
{
  "email": "user@example.com",
  "username": "demo_user",
  "password": "strongpassword123"
}
```
