This project is built by working through tutorials from [Django](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) and [django-rest-framework](https://www.django-rest-framework.org/api-guide/viewsets/#example)

# RESTful Architecture style with Django + React

## RESTful Client - written in React
  REST consumer: [mysite-react](https://github.com/nhathadt11/mysite-react)

## RESTful Server - written in Python Django
  REST provider

1. ORM support - DB manipulation via code
2. Migration - DB versioning, code first
3. Routing - Parse and delegate HTTP request

  Django does not come with RESTful support by default. In order to do this, include `django-rest-framework` or `flask` to app dependencies. This project takes `django-rest-framework`.
  

## Prerequisites
  - Pipenv 2018.11.26
  - Python 3.6.7

## Getting started
  ```
    // Create virtualenv and install project dependencies
    $ pipenv install

    // Activate virtualenv
    $ pipenv shell

    // Run migration
    $ python manage.py migrate

    // Start server
    $ python manage.py runserver

    // Exit virtualenv
    $ exit
  ```
  Visit swagger doc at: `http://localhost:8000/swagger`

## TODO:
- [ ] Visualize project structure and flow overview
- [x] React app to consume RESTful data
- [x] Use `virtualenv` to make dependencies to project-scope level
