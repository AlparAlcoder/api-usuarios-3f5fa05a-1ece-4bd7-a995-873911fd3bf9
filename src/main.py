from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str


users_db = []


@app.post("/users/", response_model=User)
def create_user(user: User):
    """
    Create a user
    """
    user.id = len(users_db) + 1
    users_db.append(user.dict())
    return user


@app.get("/users/", response_model=List[User])
def read_users():
    """
    Get all users
    """
    return users_db


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    """
    Get a specific user
    """
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    """
    Update a specific user
    """
    for index, existing_user in enumerate(users_db):
        if existing_user["id"] == user_id:
            users_db[index] = user.dict()
            users_db[index]["id"] = user_id
            return users_db[index]
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    """
    Delete a specific user
    """
    for index, existing_user in enumerate(users_db):
        if existing_user["id"] == user_id:
            removed_user = users_db.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User not found")