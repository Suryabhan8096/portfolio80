<<<<<<< HEAD
# Suryabhan Girase — Portfolio Website

A modern, responsive portfolio website built with Django, HTML, CSS, and JavaScript.

## Features

- Modern, clean, and fully responsive design (mobile + desktop)
- Smooth scrolling and animated sections
- Sections: Home, About, Skills, Projects, Services, Education, Contact
- Working contact form with Django backend integration
- Animated skill bars, typing effect, and scroll reveal animations

## Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Backend:** Python, Django
- **Database:** SQLite (default)

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. (Optional) Create a superuser to view contact submissions in admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://127.0.0.1:8000/`

## Admin Panel

Visit `http://127.0.0.1:8000/admin/` to view contact form submissions.

## Project Structure

```
Portfolio_Project/
├── manage.py
├── requirements.txt
├── portfolio_project/      # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/              # Main app
    ├── models.py           # Contact model
    ├── views.py            # Index view + contact handler
    ├── forms.py            # ContactForm
    ├── urls.py
    ├── admin.py
    ├── templates/portfolio/index.html
    └── static/portfolio/
        ├── css/style.css
        └── js/script.js
```
=======
# portfolio80
>>>>>>> 0ddd132e2fb56396254d6b0440d94b90bcb65c75
