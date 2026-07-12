# E-Commerce RestAPI Project

## Project Overview

A secure RESTful API built with Django and Django REST Framework for managing 
product categories and products.

## Features

- CRUD operations for Categories
- CRUD operations for Products
- PostgreSQL Database
- Swagger API Documentation
- Seed Data
- RESTful API

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- drf-spectacular (Swagger)

## Installation

### Clone Repository

```bash
git clone <https://github.com/MuhammadNaumanNaeem/Ecommerce>
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update the PostgreSQL database settings in `settings.py`.

### Run Migrations

```bash
python manage.py migrate
```

### Load Seed Data

```bash
python manage.py loaddata seed_data.json
```

### Run Server

```bash
python manage.py runserver
```

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/api/schema/swagger-ui/
http://127.0.0.1:8000/api/docs/
```

## API Endpoints

### Categories

- GET `/api/categories/`
- POST `/api/categories/`
- GET `/api/categories/{id}/`
- PUT `/api/categories/{id}/`
- PATCH `/api/categories/{id}/`
- DELETE `/api/categories/{id}/`

### Products

- GET `/api/products/`
- POST `/api/products/`
- GET `/api/products/{id}/`
- PUT `/api/products/{id}/`
- PATCH `/api/products/{id}/`
- DELETE `/api/products/{id}/`

## Sample Requests

Sample requests are available in the Apidog collection.

## Author

Muhammad Nauman Naeem