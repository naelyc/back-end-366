from fastapi import FastAPI
from milhas_controller import router, prefix
from milhas import *

app = FastAPI()


@app.get('/')
def hello():
    return "Hello"


app.include_router(router, prefix=prefix)
