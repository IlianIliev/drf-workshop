# Django REST Framework Workshop


## Initial setup
 - adding README
 - adding gitignore
 - adding `docker-compose` for running PostgreSQL


## Project setup
 1. Adding `requirements.txt`
    - Django==2.1.1
    - psycopg2==2.7.5
 2. Creating Django project
    - django-admin startproject drf_workshop .
 3. Configuring DATABASES
 4. Run the project:
    - `./manage.py runserver`

## DRF setup
 1. Add `djangorestframework==3.8.2` to `requirements.txt`
 2. Add `rest_framework` to `INSTALLED_APPS`
 3. Create the `api` app.
    - `python startapp api`
 4. Create a router and add it to the urls
    - Create `urls.py` in `api`
    - Create a new router and include its URLs
    - Include the API urls in the general URLs config
    - Test that it works `http://127.0.0.1:8000/api/`
