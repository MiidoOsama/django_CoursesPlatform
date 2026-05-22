# Django Courses Platform

A Django-based online courses platform built with Django 4.2.30. This application provides user management with role-based access (Student/Teacher) and profile functionality.

## Features

- User authentication and profile management
- Role-based system (Student and Teacher roles)
- Profile image upload capability
- Responsive design with static assets
- Django admin interface
- SQLite database for development

## Technologies Used

- **Python 3**
- **Django 4.2.30**
- **SQLite** (default database)
- **HTML/CSS** (templates and static files)

## Project Structure

```
.
├── src/                    # Main Django project directory
│   ├── manage.py          # Django management script
│   ├── project/           # Project configuration
│   │   ├── settings.py    # Django settings
│   │   ├── urls.py        # Main URL configuration
│   │   └── wsgi.py        # WSGI configuration
│   ├── core/              # Core application
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   ├── users/             # Users application
│   │   ├── models.py      # Profile model with roles
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   └── db.sqlite3         # SQLite database
├── templates/             # HTML templates
│   ├── core/
│   └── users/
├── static/                # Static files (CSS, JS, images)
└── venv/                  # Virtual environment

```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd /project/2nd
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django==4.2.30
   ```

4. **Run database migrations**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Admin Panel

1. Log in to the admin panel using the superuser credentials created during setup
2. Manage users, profiles, and other application data through the Django admin interface

### User Roles

The platform supports two user roles:
- **Student**: For learners accessing courses
- **Teacher**: For instructors creating and managing courses

### Profile Management

Users can:
- Update their profile information
- Upload profile images
- View and manage their role assignments

## Development

### Adding New Features

1. Create new Django apps:
   ```bash
   python manage.py startapp app_name
   ```

2. Add the app to `INSTALLED_APPS` in `src/project/settings.py`

3. Create and run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Static Files

Static files are organized in the `static/` directory at the project root. Collect static files for production:
```bash
python manage.py collectstatic
```

## Configuration

### Database

By default, the project uses SQLite. To switch to PostgreSQL or MySQL:

1. Install the appropriate database driver
2. Update the `DATABASES` setting in `src/project/settings.py`

### Secret Key

For production, replace the `SECRET_KEY` in `src/project/settings.py` with a secure, randomly generated key.

### Debug Mode

Set `DEBUG = False` in `src/project/settings.py` for production deployment.

## License

This project is part of a Udemy Django course and is intended for educational purposes.

## Contributing

This is a learning project. Feel free to fork and modify for your own educational purposes.
