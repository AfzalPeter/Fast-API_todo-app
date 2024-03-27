# crud.py
from sqlmodel import Session, select
from models import Todo

def get_session():
    with Session(engine) as session:
        yield session

def create_todo(todo, session):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def read_todos(session):
    todos = session.exec(select(Todo)).all()
    return todos

def delete_todo(todo_id, session):
    todo = session.exec(select(Todo).where(Todo.id == todo_id)).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted successfully"}

def update_todo(todo_id, todo, session):
    existing_todo = session.get(Todo, todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_todo, key, value)
    session.add(existing_todo)
    session.commit()
    session.refresh(existing_todo)
    return existing_todo
