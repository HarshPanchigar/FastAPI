from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends

app = FastAPI()
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todo.db"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(title : str , db : Session = Depends(get_db)):
    todo = Todo(title = title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message" : "todo created",
        "data" : todo
    }

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "data": todos
    }

@app.get("/todos/{id}")
def get_todo(id: int, db: Session = Depends(get_db)):
    return db.get(Todo, id)

@app.put("/todos/{id}")
def update_todo(id: int,title:str,completed:str,db: Session = Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        return {"message": "Todo not found"}

    # todo.title = title
    # todo.completed = completed

    db.commit()
    db.refresh(todo)

    return todo

@app.delete("/todos/{id}")
def delete_todo(id:int,db:Session = Depends(get_db)):
    todo = db.get(Todo,id)

    if not todo:
        return {"message": "Todo not found"}
    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted successfully"
    }