from fastapi import FastAPI
from router.router import academy

app = FastAPI()

app.include_router(academy)