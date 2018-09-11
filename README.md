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
    
## Adding signup 
 1. Let's migrate first
    `python manage.py migrate`
 2. Add the Users to the API
    - create `users` folder inside the `api` app
    - add `serializer.py` to the users folder
    - create a signup serializer with 3 fields: `username`, `email`, `password`
    - create a signup view (APIView) that users the serializer
    - install factory-boy
    - create user factory (`users/factories.py`)
    - create test case for the view. Use https://gist.github.com/IlianIliev/4dd1d6b667f36be0e501321e195f6db6
    - add the view to the url config
    - add a test to verify the serialization  

## Logging in
 1. Create a login test an watch it fail
 2. Create a LoginView and add it to the url
 3. The test will fail (tricky moment wih the UserFactory)
 4. Fix the factory and watch the test succeed
 5. Lets talk about token auth (and JWT)
 
## Retrieving and updating singles instance
 1. Create Profile serializer
 2. Create profile view
 3. Write tests for getting the profile as logged and anonymous user
 4. Specify the permissions for the View
 5. Add test for profile update
