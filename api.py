from fastapi import FastAPI
from routes.user_route import user_route
from fastapi.middleware.cors import CORSMiddleware

cliente_app = [
    "http://localhost:3000",
]

app = FastAPI()
app.include_router(user_route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cliente_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)