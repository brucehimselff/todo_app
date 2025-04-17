from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud, database

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@router.get("/", response_model=list[schemas.TodoResponse])
def get_all_todos(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_all_todos(db=db, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, updated_todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    return crud.update_todo(db=db, todo_id=todo_id, todo=updated_todo)

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db=db, todo_id=todo_id)
