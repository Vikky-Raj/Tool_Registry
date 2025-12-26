# Tool Registry - Quick Start Guide

## ✅ Pre-flight Checklist

All required files are in place:

- ✅ Backend code structure
- ✅ Database models (Tool, Bundle, Policy)
- ✅ Docker compose configuration
- ✅ Environment variables
- ✅ Requirements file

## 🚀 How to Run

### Step 1: Start PostgreSQL Database

```bash
cd infra
docker-compose up -d
```

Verify it's running:

```bash
docker ps
```

You should see `tool_registry_db` and `tool_registry_pgadmin` containers.

### Step 2: Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python main.py
```

Or with uvicorn:

```bash
uvicorn main:app --reload
```

### Step 4: Test the Application

**Health Check:**

```bash
curl http://localhost:8000/health
```

**API Documentation:**

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**Database Management:**

- pgAdmin: http://localhost:5050
  - Email: admin@toolregistry.local
  - Password: admin

## 🔍 What Happens on Startup

1. ✅ Application loads configuration from `.env`
2. ✅ Connects to PostgreSQL database
3. ✅ Creates tables automatically (Tool, Bundle, Policy)
4. ✅ Starts FastAPI server on port 8000
5. ✅ API documentation available at /docs

## 📋 Expected Output

When you run `python main.py`, you should see:

```
🚀 Starting Tool Registry API v1.0.0
📊 Environment: development
🗄️  Database: localhost:5432/toolregistry_db
✅ Database initialized
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## ⚠️ Troubleshooting

### Database Connection Error

- Make sure Docker is running: `docker ps`
- Check if PostgreSQL is healthy: `docker logs tool_registry_db`
- Verify .env has correct credentials

### Import Errors

- Ensure you're in the backend directory
- Activate virtual environment if using one
- Reinstall dependencies: `pip install -r requirements.txt`

### Port Already in Use

- Change port in main.py or kill the process using port 8000

## 🎯 Next Steps

Once running, you can:

1. Access API docs at http://localhost:8000/docs
2. Test endpoints via Swagger UI
3. View database in pgAdmin at http://localhost:5050
4. Start building API routes in `app/routers/`

## 📁 Project Structure

```
Tool_Registry/
├── backend/
│   ├── app/
│   │   ├── config/       # Settings & database config
│   │   ├── models/       # ORM models (Tool, Bundle, Policy)
│   │   ├── routers/      # API routes (empty - ready for Day 3)
│   │   └── services/     # Business logic (empty - ready for Day 3)
│   ├── main.py           # Application entry point ✅
│   └── requirements.txt  # Dependencies ✅
├── infra/
│   └── docker-compose.yml # PostgreSQL & pgAdmin ✅
├── .env                   # Environment variables ✅
└── docs/                  # Documentation
```

## ✨ Status: READY TO RUN! ✨
