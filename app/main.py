from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Auth API",
    description="Authentication API with JWT, registration, login and protected routes.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "FastAPI Auth API is running",
        "docs": "/docs"
    }
