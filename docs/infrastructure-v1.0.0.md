# Infrastructure Layer

This folder contains all infrastructure-related configuration files.

## Contents

- `docker-compose.yml` - Docker Compose configuration for PostgreSQL and pgAdmin

## Quick Start

### Start all services

```bash
docker-compose up -d
```

### Stop all services

```bash
docker-compose down
```

### Stop and remove all data (⚠️ Warning: This deletes all database data)

```bash
docker-compose down -v
```

## Services

### PostgreSQL

- **Port**: 5432
- **Database**: toolregistry_db
- **User**: toolregistry
- **Password**: devpassword (configurable via .env)

### pgAdmin

- **Port**: 5050
- **URL**: http://localhost:5050
- **Email**: admin@toolregistry.local
- **Password**: admin

## Configuration

Environment variables can be configured in the `.env` file at the project root:

```env
POSTGRES_USER=toolregistry
POSTGRES_PASSWORD=devpassword
POSTGRES_DB=toolregistry_db
POSTGRES_PORT=5432

PGADMIN_EMAIL=admin@toolregistry.local
PGADMIN_PASSWORD=admin
PGADMIN_PORT=5050
```
