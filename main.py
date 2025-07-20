from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.order_routes import router as order_router

app = FastAPI(title="HROne Ecommerce App")

app.include_router(product_router)
app.include_router(order_router)