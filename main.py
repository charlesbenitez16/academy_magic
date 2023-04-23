"""
Proyect Academy Magic
author: Charles Benitez
mail: charlesjbenitez1993@gmail.com
"""


from fastapi import FastAPI
from router.router import academy

app = FastAPI()

app.include_router(academy)