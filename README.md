# Django REST Framework Workshop


### Disclaimer
*This repo shows the creation of REST APIs step by step. Due to its presentational purpose
some of the endpoints does not have protection and every user can modify the data. Examples of
such permissions are show in other endpoints (check the **Permissions** section).
If you use this repo as a reference while building your project, make sure you have properly
tested the permission to for each endpoint (test CRUD with anonymous user, a user who is the 
object owner and a user that is not the object owner)*


Happy Coding )))
 


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
    - `python manage.py startapp api`
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
 
## Using ModelViewSet
 1. Create the authors app 
   - `python manage.py startapp authors`
   - add `authors` to `INSTALLED_APPS`
 2. Create the author models with the following fields: `name`, `date_of_birth`, `website`, `bio`
 3. Make the migrations
 4. Create the serializer
 5. Create the view (extends ModelViewSet)
 6. Register the view with the router and take a look at the browsable API
 7. Let's add some tests
 8. Settings pagination globally
 9. Fixing broken tests


## Nested Serializers
 1. Let's add books app
 2. The book model has the following fields: `title`, `authors`, `description`
 3. Creating the serializer without relation
 4. Adding the nested serializer
 5. Can we have link to the author - HyperlinkedModelSerializer


## CRUD and Nested Serializers
 1. Add test to create book
 2. Add test to update existing book
 3. Delete book


## Permissions
 1. Test that anonymous users can not delete books
 2. Set global permissions
 3. Add book ownership
 4. HiddenField + CurrentUserDefault
 5. Protect delete for owner only


## Actions
 1. Let's create like functionality
 

## Modifying the queryset based on the current user
 1. Creating "My books" endpoint
