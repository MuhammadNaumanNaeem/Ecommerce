# Week 2 – Authentication & Role-Based Access Control

## Overview

This task extends the Week 1 E-Commerce REST API by implementing secure authentication and authorization using JWT. The API now supports user registration, login, role-based access control, and protected endpoints.


## Features

- User Registration
- User Login using JWT
- Secure Password Hashing
- Role-Based Access Control (Admin & User)
- Protected API Endpoints
- Request Logging Middleware
- Swagger API Documentation



## Authentication

The API uses JWT (JSON Web Token) authentication.

### Public Endpoints


POST /api/accounts/register/
POST /api/accounts/login/


### Protected Endpoints


GET  /api/accounts/me/

GET  /api/categories/
POST /api/categories/
PUT  /api/categories/{id}/
PATCH /api/categories/{id}/
DELETE /api/categories/{id}/

GET  /api/products/
POST /api/products/
PUT  /api/products/{id}/
PATCH /api/products/{id}/
DELETE /api/products/{id}/


For protected endpoints, include:


Authorization: Bearer <access_token>


## Authorization

### Admin
- Create records
- Update records
- Delete records
- View records

### User
- View records only



## API Documentation

Swagger UI


http://127.0.0.1:8000/api/docs/


OpenAPI Schema


http://127.0.0.1:8000/api/schema/




## Included Files

- `Sample_request_2.openapi.json` – API request collection
- `seed_data.json` – Sample database records



## Setup

bash
pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata seed_data.json

python manage.py runserver




## Author

**Muhammad Nauman Naeem**
