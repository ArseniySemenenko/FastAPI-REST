from fastapi import APIRouter
import sys
sys.path.insert(0, "..")
from controllers.user_controller import UserController as controller
from pydantic import BaseModel

router = APIRouter(
    prefix="/api",
    tags=["users"],
)

class User(BaseModel):
    name: str
    password: str

@router.get("/users")
def getUsers():
    return controller.getUsers()

@router.get("/user/{id}")
def getUserById(id):
    return controller.getUser(id)

@router.delete("/user/{id}")
def deleteUser(id):
    return controller.deleteUserById(id)

@router.post("/user")
def createUser(body: User):
    return controller.createUser(body)

@router.post("/user/{id}")
def updateUser(body: User , id):
    return controller.updateUser(body , id)