from pydantic import BaseModel
class TodoBase(BaseModel):
     title: str
     description: str
class TodoCreate(TodoBase):
     pass
  class TodoOut(TodoBase)
   id: int 
    class TodoUpdate(TodoBase)
     pass 
      class TodoDelete(TodoBase)
       pass
        
     class Config:
         orm_mode = True
