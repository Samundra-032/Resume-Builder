# creating Resume builder
## prerequisite
- install python on the machine
- enable virtual environment
    - python -m venv <virtual env name>
- activate the virtual environment

## Start the project
```{python} 
django-admin startproject resume_builder
```
```{python} 
cd resume_builder
```

## start app
```{python} 
python manage.py startapp resumes
```

## need to change the file or need to create
### change
- urls.py
- settings.py

### create
- templates folder and its content
- static folder and its content
- forms.py
- models.py
- urls.py
- views.py

## After model is ready
```{python} 
python manage.py makemigrations
python manage.py migrate
```

## after project is ready
```{python} 
python manage.py createsuperuser
```

## to run server
```{python} 
python manage.py runserver
```

