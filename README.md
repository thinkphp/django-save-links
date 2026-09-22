# Django Save Links

A simple Django web application for saving and managing useful links.

Users can add a title and URL, and the saved links are displayed on the home page.

## Features

* Add a new link with a title and URL
* Display all saved links
* Store links in a database
* Django ModelForm for handling form submissions
* PostgreSQL database in production
* SQLite database for local development
* Static files handled with WhiteNoise
* Deployed on Render

## Technologies

* Python
* Django
* PostgreSQL
* SQLite
* HTML
* CSS
* Gunicorn
* WhiteNoise
* Render

## Project Structure

```text
django-save-links/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── links/
│   ├── migrations/
│   ├── static/
│   │   └── links/
│   │       └── style.css
│   ├── templates/
│   │   └── links/
│   │       └── home.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── build.sh
├── manage.py
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/thinkphp/django-save-links.git
cd django-save-links
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser at:

```text
http://127.0.0.1:8000/
```

## Database

For local development, the project uses SQLite by default.

In production, the application uses PostgreSQL through the `DATABASE_URL` environment variable.

## Static Files

Static files are collected using Django's `collectstatic` command and served in production using WhiteNoise.

```bash
python manage.py collectstatic --no-input
```

## Deployment

The application is configured for deployment on Render.

The build process:

```bash
./build.sh
```

The application is started with Gunicorn:

```bash
gunicorn config.wsgi:application
```

## Environment Variables

The production environment requires a `DATABASE_URL`.

A `SECRET_KEY` should also be configured as an environment variable in production.

Example:

```text
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=False
```

Do not commit passwords, secret keys, database URLs, or `.env` files to GitHub.

## What I Learned

This project was built as a learning project to practice:

* Django project and app structure
* Models and migrations
* Django forms
* Views and templates
* URL routing
* Static files
* SQLite and PostgreSQL
* Environment variables
* Gunicorn
* WhiteNoise
* Deploying a Django application to Render

## Live Demo

The application is deployed on Render:

https://django-save-links.onrender.com/

