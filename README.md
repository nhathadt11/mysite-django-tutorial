This project is built by working through tutorials from [Django](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) and [django-rest-framework](https://www.django-rest-framework.org/api-guide/viewsets/#example)

# RESTful Architect

## RESTful Client - written in React
  REST consumer

## RESTful Server - written in Python Django
  REST provider

1. ORM support - DB manipulation via code
2. Migration - DB versioning, code first
3. Routing - Parse and delegate HTTP request

  Django does not come with RESTful support by default. In order to do this, include `django-rest-framework` or `flask` to app dependencies. This project takes `django-rest-framework`.
  

## Prerequisite
  - Python 3.6.7
  - Django 2.1.4

## Getting started
  `python3 manage.py runserver`

## TODO:
- [ ] Project structure and flow overview
- [ ] React app to consume RESTful data
- [ ] Use `virtualenv` to scope down dependencies to project
