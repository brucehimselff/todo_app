from fastapi import FastAPI
from . import models
from .database import engine
from .routers import todo

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="Todo App API",
    description="A simple Todo application built with FastAPI",
    version="1.0.0"
)

# Include todo router
app.include_router(todo.router, tags=["Todos"])
