from fastapi import FastAPI

app = FastAPI(title="Demo API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Demo API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    
from app.models import UserCreate

@app.post("/users/")
def create_user(user: UserCreate):
    return{"username" : user.username, "email" : user.email, "id":1}