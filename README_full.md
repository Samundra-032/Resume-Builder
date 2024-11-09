
# Django Resume Builder

This guide walks you through setting up and building a Django resume builder application from scratch. The project allows users to create an ATS-friendly resume by filling out a form, dynamically adding multiple entries in sections like Education, Experience, Skills, Projects, and Extra-Curricular Activities. The final output is a downloadable PDF resume generated from the data entered.

## Table of Contents
- Project Overview
- Prerequisites
- Starting a Django Project
- Setting Up the Resume Builder Project
- Folder Structure
- Detailed Project Build Steps
- Running the Project
- Deployment

## Project Overview
The Django Resume Builder allows users to:

- Enter multiple entries for each resume section: Education, Experience, Skills, Projects, and Extra-Curricular Activities.
- Dynamically add and remove entries within each section.
- Generate and download a PDF resume with a single header for each section, displaying all related entries underneath.

## Prerequisites
Before you begin, make sure you have the following:

- **Python**: Version 3.8 or higher.
- **pip**: Python package installer.
- **Virtualenv**: Optional, but recommended for isolating project dependencies.

To install Virtualenv:

```bash
pip install virtualenv
```

## Starting a Django Project
Set up a Django project environment.

Create a new directory and navigate into it:

```bash
mkdir django-resume-builder
cd django-resume-builder
```

Set up a virtual environment and install Django.

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Django and other required packages
pip install django xhtml2pdf
```

Create a Django project.

```bash
django-admin startproject resume_builder .
```

Create the main app for the project.

```bash
python manage.py startapp resumes
```

## Setting Up the Resume Builder Project
Add the app to your project:

Open `resume_builder/settings.py` and add `resumes` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'resumes',
]
```

Migrate the database:

```bash
python manage.py migrate
```

Create Superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

## Folder Structure
After creating the app and setting up initial configurations, your folder structure should look like this:

```
resume_builder/
├── manage.py
├── resume_builder/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── resumes/
    ├── migrations/
    ├── templates/
    │   └── resumes/
    │       ├── create_resume.html          # HTML form for creating a resume
    │       └── resume_template.html        # HTML template for PDF generation
    ├── static/
    │   └── resumes/
    │       ├── css/
    │       │   └── style.css               # CSS for styling the form
    │       └── js/
    │           └── formset.js              # JavaScript for dynamic form fields
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py                            # Forms for Profile, Education, Experience, etc.
    ├── models.py                           # Models for Profile, Education, Experience, etc.
    ├── tests.py
    ├── urls.py                             # App-specific URLs
    └── views.py                            # Logic for form handling and PDF generation
```

## Detailed Project Build Steps

### 1. Define Models in models.py
In `resumes/models.py`, define models for each section (Profile, Education, Experience, Skill, Project, ExtraCurricular):

```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

# Define models for Education, Experience, Skill, Project, ExtraCurricular with ForeignKey to Profile
```

### 2. Create Forms in forms.py
Create forms to capture user inputs, including formsets for dynamically adding multiple entries per section.

```python
from django import forms
from .models import Profile, Education, Experience, Skill, Project, ExtraCurricular

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'summary', 'linkedin', 'github']
```

### 3. Create Views in views.py
Define views to handle form submission, save data to the database, and generate the PDF.

```python
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
# Define create_resume view here
```

### 4. Design Templates
- `create_resume.html`: Build the form layout and add JavaScript for dynamically adding fields.
- `resume_template.html`: Create the structure for the PDF output with one header per section and a loop for entries.

### 5. Static Files
Add `style.css` and `formset.js` for styling and dynamic field functionality. Reference these files in `create_resume.html`.

## Running the Project
Run the Development Server:

```bash
python manage.py runserver
```

Access the Form:

Open your web browser and go to `http://127.0.0.1:8000/create/` to view the form.

Generate PDF:

Fill out the form, add multiple entries, and click "Generate PDF" to download the resume.

## Deployment
### Deploying to a Production Server (Example with Gunicorn and Nginx)

#### Install Gunicorn:

```bash
pip install gunicorn
```

#### Run Gunicorn Server:

```bash
gunicorn resume_builder.wsgi:application
```

#### Configure Nginx:

Set up an Nginx server block to proxy requests to Gunicorn. A sample Nginx configuration might look like this:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/your/static/files;
    }
}
```

#### Set Debug to False:

In `settings.py`, set `DEBUG = False` and configure `ALLOWED_HOSTS` with your domain name.

#### Collect Static Files:

Run the following command to gather static files for production:

```bash
python manage.py collectstatic
```

After these steps, your application should be accessible via your server’s domain.

---

### Additional Tips:
- Consider using `Django Rest Framework` if you plan on expanding this into an API-based service.
- For more complex PDF generation needs, libraries like `ReportLab` can provide advanced customization.
