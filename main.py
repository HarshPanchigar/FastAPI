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
def get_todo(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "data": todos
    }