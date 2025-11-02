from fastapi import APIRouter
from config.database import conection
from models.user import UserModel
from schemas.userSchemas import listaUserEntidade, userEntidade

user_route = APIRouter()

@user_route.get("/")
async def get_home():
    return ("bem vindo ao meu sistema de usuarios")

@user_route.get("/users")
async def fetch_all_users():
    return listaUserEntidade(conection.local.user.find())

@user_route.post("/user")
async def create_user(user: UserModel):
    conection.local.user.insert_one(dict(user))
    return ("Usuario criado com sucesso")