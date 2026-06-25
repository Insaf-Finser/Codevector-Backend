from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routes import router

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Product Browser API",
    version="1.0.0"
)

# Register all routes
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Product Browser API",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }