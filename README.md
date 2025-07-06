# Rail View Guardian Backend

This is the backend for the Rail View Guardian dashboard, providing RESTful APIs for user management, defect tracking, reporting, and notifications.

## Features

- User authentication with JWT
- Role-based access control (admin, technician)
- CRUD operations for users, defects, and reports
- Notification preferences
- Password hashing and secure storage
- CORS enabled for frontend integration

## Tech Stack

- Python 3.10+
- FastAPI
- MongoDB (via pymongo)
- passlib (bcrypt)
- python-dotenv

## Getting Started

### Prerequisites

- Python 3.10+
- MongoDB instance (local or Atlas)

### Installation

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in [app](http://_vscodecontentref_/1) with:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
MONGODB_URI=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/
```

### Running the Server

```sh
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000/api](http://localhost:8000/api).

### API Endpoints

- `POST /api/login` – User authentication
- `GET /api/users` – List users
- `POST /api/users` – Create user
- `GET /api/users/{user_id}` – Get user by ID
- `PUT /api/users/{user_id}` – Update user (email, password, notifications, language, etc.)
- `DELETE /api/users/{user_id}` – Delete user
- `GET /api/defects` – List defects
- `POST /api/defects` – Create defect
- `GET /api/reports` – List reports
- `POST /api/reports` – Create report

### Notes

- Passwords are hashed using bcrypt.
- JWT tokens include user ID and role.
- CORS is enabled for all origins in development (see [main.py](http://_vscodecontentref_/2)).