from fastapi import APIRouter
from config.database import conection
from models.user import UserModel

user_route = APIRouter()

@user_route.get("/")
def get_users():
    db = conection['user_database']
    users_collection = db['users']
    users = list(users_collection.find({}, {'_id': 0}))
    return users

