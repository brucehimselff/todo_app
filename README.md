# Todo App (FastAPI)

A simple Todo RESTful API built with **FastAPI**, **SQLite**, and **Pydantic**.  
It supports full CRUD operations on todo items.

---

## Features

- Create a new todo
- Read all todos
- Read a single todo by ID
- Update a todo
- Delete a todo

---

## Tech Stack

- FastAPI
- SQLite
- Pydantic
- Python 3

---

## Folder Structure
todo_app/
│
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── routes.py
└── main.py

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Bruce Nyeha/todo_app.git

# Navigate into the project folder
cd todo_app

# Install dependencies
pip install fastapi uvicorn

# Run the app
uvicorn main:app --reload

API Endpoints
Method.   Endpoint.       Description.
GET.      /todos/.        Get all todos
GET.     /todos/{todo_id} Get a specific todo
POST.    /todos/.          Create a todo
PUT.    /todos/{todo_id}   Update a todo
DELETE. /todos/{todo_id}    Delete a todo



