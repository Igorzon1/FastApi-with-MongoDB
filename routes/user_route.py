from fastapi import APIRouter
from config.database import conection
from models.user import UserModel
from schemas.userSchemas import listaUserEntidade, userEntidade
from bson import ObjectId

user_route = APIRouter()

@user_route.get("/")
async def get_home():
    return ("bem vindo ao meu sistema de usuarios")

@user_route.get("/user")
async def fetch_all_users():
    return listaUserEntidade(conection.local.user.find())

@user_route.get("/user/{id}")
async def fetch_user_by_id(id: str):
    return userEntidade(conection.local.user.find_one({"_id": ObjectId(id)}))

@user_route.post("/user")
async def create_user(user: UserModel):
    conection.local.user.insert_one(dict(user))
    return ("Usuario criado com sucesso")

@user_route.put("/user/{id}")
async def update_user(id: str, user: UserModel):
    conection.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}
    )
    return ("Usuario atualizado com sucesso")

@user_route.delete("/user/{id}")
async def delete_user(id: str):
    conection.local.user.find_one_and_delete({"_id": ObjectId(id)})
    return ("Usuario deletado com sucesso")