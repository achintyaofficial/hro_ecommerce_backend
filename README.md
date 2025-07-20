# HROne E-Commerce Backend with FastAPI

## Features
- Create & list products
- Create & fetch user orders
- MongoDB integration
- Query filters, pagination

## Tech Stack
- FastAPI
- MongoDB Atlas (via Motor)
- Deployed on Render

## Run Locally
```bash
git clone <repo-url>
cd hro_ecommerce_backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment
- `MONGO_URI`
- `MONGO_DB_NAME`