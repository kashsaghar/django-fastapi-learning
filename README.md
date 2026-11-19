# Student Management System

A simple Django app for managing student records (add, edit, delete, list).

## Setup

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your own `SECRET_KEY`:
   ```
   copy .env.example .env
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. (Optional) Create an admin user:
   ```
   python manage.py createsuperuser
   ```

## Run

```
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

- Admin panel: http://127.0.0.1:8000/admin/
