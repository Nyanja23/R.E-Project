
# TaskTracker

TaskTracker is a Django-based task management web application that lets users create, manage, and track tasks. Built with PostgreSQL for data storage and deployed on Render, it includes user authentication, task CRUD operations, and profile picture uploads (with Render Disks for persistence). This README guides you through running it locally or deploying it on Render.

## Features

- **Task Management**: Add, view, edit, and delete tasks.
- **User Authentication**: Secure login/logout with a custom `base.User` model.
- **Profile Pictures**: Upload profile images (persistent on Render via Disks).
- **Responsive Design**: Powered by Bootstrap 5 and Crispy Forms.
- **Deployment**: Runs on Render with Docker and Gunicorn.

## Prerequisites

- **Python**: 3.13+
- **PostgreSQL**: 17+ (local database)
- **Git**: To clone the repo
- **Render Account**: For deployment
- **Docker**: Optional, for Render (handled automatically)

## Running Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nyanja23/R.E-PROJECT.git
cd TaskTracker
```

### Step 2: Set Up Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Ensures `django`, `psycopg2-binary`, `dj-database-url`, `gunicorn`, `crispy-forms`, and `crispy-bootstrap5` are installed.

### Step 4: Configure PostgreSQL

#### Install PostgreSQL

Download from [postgresql.org](https://www.postgresql.org/) and install (e.g., version 17).

#### Create Database

```bash
psql -U postgres
CREATE DATABASE task_tracker_db;
\q
```

#### Verify Password

Default password in `settings.py` is `postgres2025`. If different, update:

```python
# settings.py
'PASSWORD': os.getenv('DB_PASSWORD', 'your_password_here')
```

#### Test connection

```bash
psql -U postgres -d task_tracker_db
```

### Step 5: Apply Migrations

```bash
python manage.py migrate
```

### Step 6: Run the Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. Add tasks or upload a profile pic to test.

### Optional: Load Sample Data

If you have a `data.json` file:

```bash
python manage.py loaddata data.json
```

## Deploying on Render

### Step 1: Prepare the Project

#### Check `requirements.txt`

Should include:

```text
django>=4.2
psycopg2-binary
dj-database-url
gunicorn
crispy-forms
crispy-bootstrap5
whitenoise
```

#### Verify `Dockerfile`

```dockerfile
FROM python:3.13-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 DJANGO_SETTINGS_MODULE=TaskTracker.settings PORT=8000
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn TaskTracker.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
```

### Step 2: Set Up Render

#### Create a Render Account

Sign up at [render.com](https://render.com).

#### New Web Service

Dashboard > New > Web Service. Connect your GitHub repo (`yourusername/TaskTracker`).

#### Configure Environment Variables

Add:

```text
DEBUG=False
SECRET_KEY=your-secret-key-here  # Generate a secure key
DATABASE_URL=postgres://user:password@host:port/dbname  # From Render PostgreSQL
```

Create a PostgreSQL instance on Render and copy its Internal Database URL.

### Step 3: Add Render Disks for Media

#### Add Disk

Dashboard > Your Service > Disks > Add Disk.

- **Name**: media
- **Mount Path**: /app/media
- **Size**: 1 GB (adjust as needed).

#### Update `urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

# Serve media files in production
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Step 4: Deploy

#### Push Changes

```bash
git add requirements.txt Dockerfile TaskTracker/urls.py
git commit -m "Prepare for Render with Disks"
git push origin main
```

#### Monitor Deployment

Render builds and deploys automatically. Check logs for gunicorn startup and no errors.

### Step 5: Test Online

Visit `https://your-service.onrender.com` (e.g., `https://task-tracker-mit4.onrender.com`). Log in, add a task, upload a profile pic, and refresh to confirm persistence.

## Troubleshooting

- **Local Error: psycopg2 Missing**:
  Run `pip install psycopg2-binary`.
- **Render Error: gunicorn: not found**:
  Ensure `gunicorn` is in `requirements.txt` and redeploy.
- **Profile Pics Not Showing on Render**:
  Verify Render Disk is mounted at `/app/media` and `urls.py` serves media.
- **Database Connection Fails**:
  Check `DATABASE_URL` on Render or local password in `settings.py`.

## Contributing

1. Fork the repo.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push: `git push origin feature/your-feature`.
5. Open a Pull Request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
