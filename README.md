# 📁 Doc Manager API

This is the backend for the document management system **DocSyncX**. It provides a secure, scalable, and modular Django REST API for managing documents with features like user authentication, JWT-based access, document uploads, expiration reminders, and more.

👉 To learn more about the project goals, UI, and user experience, check out the [frontend repository](https://github.com/your-username/docsyncx-frontend).

### ✨ Key Features
- Custom user authentication with email & password
- JWT-based authentication with refresh support
- Upload and manage PDF and image files
- Add custom metadata fields per document
- Set document expiry and get reminders
- Share documents via link or email
- Organized folder structure for easy management

---

## 🚀 Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- PostgreSQL
- Simple JWT (for auth)
- CORS Headers

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/doc-manager-api.git
cd doc-manager-api
```

### 2. Create and Activate a Virtual Environment

For **Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

For **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Run Migrations
```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

---

## 🔑 Authentication

We use **JWT Authentication**. After login, you'll receive `access` and `refresh` tokens.

- Include the token in headers:
  ```http
  Authorization: Bearer <access_token>
  ```

---

## 📡 API Endpoints

### ✅ Auth & User Endpoints

| Method | URL                          | Description             | Payload (JSON)                                                                | Returns (JSON)                                                  |
|--------|------------------------------|-------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| POST   | `/api/auth/register/`        | Register new user       | `{ "email": "", "full_name": "", "password": "", "password1": "" }`           | `{ "message": "User created successfully" }`                     |
| POST   | `/api/auth/login/`           | Login user              | `{ "email": "", "password": "" }`                                             | `{ "access": "", "refresh": "" }`                               |
| POST   | `/api/auth/token/refresh/`   | Refresh access token    | `{ "refresh": "" }`                                                           | `{ "access": "" }`                                              |
| GET    | `/api/auth/profile/`         | Get user profile (auth) | —                                                                              | `{ "id": "", "email": "", "full_name": "" }`                    |

> ⚠️ Profile endpoint requires authentication using the `Authorization` header.

---

## 🧪 Running Tests

> *(Coming soon)* Add automated test cases using Django's `TestCase`.

```bash
python manage.py test accounts
```

---

## 📁 Project Structure (Important Apps Only)
```
doc-manager-api/
│
├── accounts/               # Custom user model & authentication
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── core/                   # Global settings, root URLs
├── manage.py
└── requirements.txt
```

---

## 📬 Contact

For any issues or contributions, feel free to open an issue or contact the maintainer.

---

## 📜 License

This project is licensed under the MIT License.

