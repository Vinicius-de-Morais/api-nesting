# main.py
from fastapi import FastAPI
from api import routes

app = FastAPI()

# include the routes in app
app.include_router(routes.router)
