# Tool Registry Backend

FastAPI backend for the MCP Tool Registry application.

## Setup

### 1. Create a virtual environment

```bash
cd backend
python -m venv venv
```

### 2. Activate the virtual environment

**Windows:**

```bash
.\venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` in the project root:

```bash
copy ..\.env.example ..\.env  # Windows
cp ../.env.example ../.env    # Linux/Mac
```

### 5. Start PostgreSQL with Docker

From the infra directory:

```bash
cd ../infra
docker-compose up -d
```

This will start:

- PostgreSQL database on port 5432
- pgAdmin on port 5050 (optional, for database management)

### 6. Run the application

```bash
python main.py
```

Or with uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once the application is running:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

## Project Structure

```
backend/
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py      # Application settings
│   │   └── database.py      # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── tool.py          # Tool ORM model
│   │   ├── bundle.py        # Bundle ORM model
│   │   └── policy.py        # Policy ORM model
│   ├── routers/             # API routes (to be implemented)
│   ├── services/            # Business logic (to be implemented)
│   └── __init__.py
├── main.py                  # Application entry point
├── requirements.txt         # Production dependencies
└── requirements-dev.txt     # Development dependencies
```

## Database Management

### Access pgAdmin

1. Open http://localhost:5050
2. Login with:

   - Email: admin@toolregistry.local
   - Password: admin

3. Add server connection:
   - Host: postgres
   - Port: 5432
   - Database: toolregistry_db
   - Username: toolregistry
   - Password: devpassword

### Stop Docker services

```bash
cd ../infra
docker-compose down
```

### Stop and remove volumes (⚠️ this will delete all data)

```bash
cd ../infra
docker-compose down -v
```

## Development

### Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### Run tests

```bash
pytest
```

### Format code

```bash
black app/
```

### Lint code

```bash
flake8 app/
```
