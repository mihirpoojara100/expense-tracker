# 💰 Expense Tracker API

A modern, fast, and scalable expense tracking API built with FastAPI, PostgreSQL, and SQLAlchemy. Track your expenses, manage budgets, and get insights into your spending habits.

## 🚀 Features

- **User Management**: Secure user registration and authentication with JWT
- **Expense Tracking**: Add, edit, and categorize expenses
- **Budget Management**: Set monthly budgets with alerts
- **Categories**: Organize expenses with custom categories
- **Reports & Analytics**: Get insights into your spending patterns
- **Profile Management**: User profiles with avatar support
- **RESTful API**: Clean, documented API endpoints
- **Database Migrations**: Alembic for database schema management

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **Migrations**: Alembic
- **Settings**: Pydantic Settings
- **Documentation**: Auto-generated OpenAPI/Swagger

## 📋 Prerequisites

- Python 3.13+
- PostgreSQL
- pip

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd expense-tracker
```

### 2. Create Virtual Environment

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
# PostgreSQL Database
PGSQL_HOST=localhost
PGSQL_PORT=5432
PGSQL_USER=####
PGSQL_PASSWORD=####
PGSQL_DB=expense_tracker

# JWT Secret for sessions
JWT_SECRET=your-super-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXP_DELTA_SECONDS=3600
```

### 5. Database Setup

```bash
# Run database migrations
alembic upgrade head
```

### 6. Start the Application

```bash
# Development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production server
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
expense-tracker/
├── alembic/                 # Database migrations
│   ├── env.py              # Alembic configuration
│   └── versions/           # Migration files
├── app/
│   ├── core/               # Core functionality
│   ├── database/           # Database configuration
│   │   ├── models/         # SQLAlchemy models
│   │   │   └── users.py    # User model
│   │   └── session.py      # Database session
│   ├── routes/             # API routes
│   │   └── v1/             # API version 1
│   │       └── __init__.py # V1 router
│   └── schemas/            # Pydantic schemas
├── .env                    # Environment variables
├── alembic.ini            # Alembic configuration
├── main.py                # FastAPI application
├── requirements.txt       # Python dependencies
├── settings.py            # Application settings
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

| Variable                | Description         | Default         |
| ----------------------- | ------------------- | --------------- |
| `PGSQL_HOST`            | PostgreSQL host     | localhost       |
| `PGSQL_PORT`            | PostgreSQL port     | 5432            |
| `PGSQL_USER`            | PostgreSQL username | postgres        |
| `PGSQL_PASSWORD`        | PostgreSQL password | root            |
| `PGSQL_DB`              | Database name       | expense_tracker |
| `JWT_SECRET`            | JWT secret key      | -               |
| `JWT_ALGORITHM`         | JWT algorithm       | HS256           |
| `JWT_EXP_DELTA_SECONDS` | JWT expiration      | 3600            |

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

### API Endpoints

```
/api/v1/
├── /                    # API information
├── /health             # Health check
├── /users/             # User management
├── /auth/              # Authentication
├── /expenses/          # Expense tracking
├── /categories/        # Categories
├── /budgets/           # Budget management
└── /reports/           # Analytics
```

## 🗄️ Database Models

### User Model

- Authentication fields (email, username, password)
- Profile information (name, avatar, phone)
- Preferences (currency, timezone, language)
- Budget settings (monthly budget, alerts)
- Security features (2FA, login attempts)

## 🔄 Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migrations

```bash
alembic downgrade -1
```

## 🧪 Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest
```

### Code Formatting

```bash
# Install formatting tools
pip install black isort

# Format code
black .
isort .
```

### Linting

```bash
# Install linting tools
pip install flake8

# Run linter
flake8 .
```

## 🚀 Deployment

### Docker (Recommended)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables for Production

```env
# Production settings
DEBUG=false
DATABASE_ECHO=false
JWT_SECRET=your-production-secret-key
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [API Documentation](http://localhost:8000/docs)
2. Review the [Issues](../../issues) page
3. Create a new issue with detailed information

## 🔮 Roadmap

- [ ] Expense categories management
- [ ] Budget alerts and notifications
- [ ] Export functionality (PDF, CSV)
- [ ] Multi-currency support
- [ ] Mobile app integration
- [ ] Advanced analytics and charts
- [ ] Recurring expenses
- [ ] Expense sharing between users

---

**Happy Expense Tracking! 💰📊**
