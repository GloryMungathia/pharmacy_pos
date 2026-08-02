# Pharmacy POS API

This is a backend API for a Point of Sale system for a pharmacy. I built it using FastAPI and SQLAlchemy, with PostgreSQL as the database.

## What this project does

It's a POS system for a pharmacy that sells medicines and other health products. The API lets you manage products, stock, sales, customers, staff, suppliers, and receipts.

## Entities in this project

- Products - the medicines/items sold, with expiry date and whether they need a prescription
- Categories - groups products (e.g. Prescription Medicine, OTC)
- Suppliers - companies that supply the products
- Customers - people who buy from the pharmacy
- Users - staff accounts (cashier, pharmacist etc.)
- Inventory - tracks stock batches and expiry dates
- Sales - a sale transaction
- Sale Items - the individual products in a sale
- Payments - payment info for a sale
- Receipts - receipt generated after a sale

## Tech used

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic for validation

## How to run it

1. Clone this repo
2. Create and activate a virtual environment
3. Install the requirements:

pip install -r requirements.txt

4. Update the database connection in `database.py` with your own PostgreSQL details
5. Start the server:

fastapi dev

6. Go to `http://127.0.0.1:8000/docs` to test the endpoints on Swagger UI

## Project structure

Each entity has its own file in these folders:
- `models/` - the database tables
- `schemas/` - request/response validation
- `repositories/` - talks directly to the database
- `services/` - business logic
- `routers/` - the actual API endpoints

Every entity supports create, read, update and delete, and returns a 404 if you try to get something that doesn't exist.