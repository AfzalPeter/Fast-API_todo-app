# main.py
from fastapi import FastAPI, HTTPException
from app.database import engine, lifespan
from app.models import Todo
from app.crud import get_session, create_todo, read_todos, delete_todo, update_todo

app = FastAPI(
    lifespan=lifespan,
    title="Hello World API with DB",
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos/", response_model=Todo)
def create_todo_handler(todo: Todo, session:Annotated[Session, Depends(get_session)]):
    return create_todo(todo, session)

@app.get("/todos/", response_model=list[Todo])
def read_todos_handler(session:Annotated[Session, Depends(get_session)]):
    return read_todos(session)

@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo_handler(todo_id:int, sission:Session=Depends(get_session)):
    return delete_todo(todo_id, session)

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo_handler(todo_id: int, todo: Todo, session=Depends(get_session)):
    return update_todo(todo_id, todo, session)
