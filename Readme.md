# SaaS Onboarding Project

This Django project provides APIs for onboarding organizations to our SaaS product.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Database Setup](#database-setup)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)
- [Version Control](#version-control)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/saas-onboarding.git



## Routes To Implement

| METHOD | ROUTE | FUNCTIONALITY |DATA|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/users/``` | _Get all user_| _All users_|
| *GET* | ```/api/users?page=1&limit=10&name=James&sort=-age``` | _Get user according to the requirenment_|_Selected users_|
| *POST* | ```/api/users/``` | _create new user_|_create new users_|
| *GET* | ```/api/users/{id}``` | _Retrieve an user_|_Selected user_|
| *PUT* | ```/api/users/{id}``` | _Update an user_|_selected users_|
| *DELETE* | ```/api/users{id}``` | _Delete/Remove an user_ |_selected users_|

## How to run the Project
- Install mysyqlclient
- Install Python
- Install Django using pip install django 
- Install Django Rest Framework using pip install djangorestframework
- Git clone the project with ``` git clone https://github.com/Laxmika1401/RESTAPI_task.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Create you database with `python manage.py runserver` 
- Finally run the API 
``` python manage.py runserver ```