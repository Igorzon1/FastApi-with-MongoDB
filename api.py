from fastapi import FastAPI
from routes.user_route import user_route

app = FastAPI()
app.include_router(user_route)

