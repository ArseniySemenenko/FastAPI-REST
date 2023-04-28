import sys
sys.path.insert(0, "..")
from services.users_service import UserService as service
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

class UserController():
    def getUser(id):
        return service.getUserById(id)

    def getUsers():
        return service.getUsers()

    def deleteUserById(id):
        return service.deleteUserById(id)

    def createUser(body: User):
        return service.createUser(body.name, body.password)

    def updateUser(body: User, id):
        return service.updateUser(body.name, body.password, id)