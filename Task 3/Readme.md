# Week 3 - Advanced Data Aggregation

## Overview
This task extends the E-Commerce REST API by implementing analytics endpoints that provide useful summary statistics using Django ORM aggregation functions. The API returns frontend-friendly JSON responses while keeping database queries efficient.


## Features

Product Statistics
  Total Products
  Average Product Price
  Total Stock

Category Statistics
  Product count for each category

Monthly Product Statistics
  Products grouped by month

User Statistics
  Total Users
  Active Users
  Inactive Users
  Admin Users
  Normal Users

Inventory Statistics
  Total Inventory Value
  Average Product Price

JWT Protected Analytics Endpoints

Swagger API Documentation

Consistent JSON Response Format

Exception Handling with Try-Catch



## API Endpoints

### Analytics

Method      Endpoint 
GET         `/api/analytics/products/` 
GET         `/api/analytics/categories/` 
GET         `/api/analytics/monthly-products/` 
GET         `/api/analytics/users/` 
GET         `/api/analytics/inventory/` 


## Aggregation Functions Used

Count()
Sum()
Avg()
annotate()
aggregate()
TruncMonth()
ExpressionWrapper()
F() Expressions


## Installation

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Load seed data

```bash
python manage.py loaddata seed_data_week3.json
```

Run the server

```bash
python manage.py runserver
```


## Authentication

All analytics endpoints require a valid JWT Access Token.

Include the token in the request header.

```
Authorization: Bearer <access_token>
```


## Sample Files

- seed_data_week3.json
- sample_requests_week3.json


## Documentation

Swagger UI

```
/api/docs/
```

ReDoc

```
/api/redoc/
```


## Week 3 Deliverables

- Analytics Endpoints
- JWT Protected APIs
- Swagger Documentation
- Seed Data
- Sample Requests
- README