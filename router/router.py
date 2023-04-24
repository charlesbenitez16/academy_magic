import random
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from schema import academy_schema
from config import db_models, db
from models import api_crud
from utils import constants
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

academy = APIRouter()
templates = Jinja2Templates(directory="./templates")

@academy.get("/update", response_class= HTMLResponse)
def update(request:Request):
    return templates.TemplateResponse("update.html", {"request":request})
@academy.get("/create", response_class= HTMLResponse)
def create(request:Request):
    return templates.TemplateResponse("create.html", {"request":request})
@academy.get("/inicio", response_class= HTMLResponse)
def inicio(request:Request):
    return templates.TemplateResponse("inicio.html", {"request":request})

@academy.post("/api/solicitud")
async def create_solicitud(
    request:Request,
    id:str=Form(),
    first_name:str=Form(),
    last_name:str=Form(),
    age:int = Form(),
    magic_affinity:str = Form(),
    dbs: Session= Depends(db.get_db)):
    """
        Endpoint: crear una nueva solictud
        Method: POST
    """
    user = {
        "id":id,
        "first_name": first_name,
        "last_name": last_name,
        "age":age,
        "magic_affinity":magic_affinity,
    }
    
    # Accionacion de grimorio aleatorio
    grimorio_tuple = random.choice(constants.tupla_grimorios)
    grimorio = f"{grimorio_tuple[0]}, {grimorio_tuple[1]}"
    try:
        #CRUD para enviar solicitud
        register = api_crud.create_user(dbs, user, grimorio)

        result = academy_schema.ResultJson(
            id = register.id,
            first_name=register.first_name,
            last_name=register.last_name,
            age=register.age,
            magic_affinity=str(register.magic_affinity),
            grimorio=register.grimorio,
            status= register.status,
        )

        return templates.TemplateResponse("index.html", {"request":request})

    except Exception as e:
        raise e

@academy.get("/api/get_only_user")
def get_user(id:str, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Trae un solo registro de la base de datos
        Method: GET
    """
    try:
        # Extaer un registro
        payload = api_crud.verify_id(dbs,id)
        return payload
    except Exception as e:
        raise e

@academy.get("/api/get_users",response_class= HTMLResponse)
def get_users(request:Request,dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Trae todos los registros de la base de datos
        Method: GET
    """
    try:
        # Extrae todos los registros.
        payload = dbs.query(db_models.StudentAcademy).all()   

        return templates.TemplateResponse("index.html", {"request":request,"context":payload})
    except Exception as e:
        raise e

@academy.get("/api/get_grimorio/")
def get_grimorio(id:str,dbs:Session = Depends(db.get_db)):
    """
        Endpoint: Trae el grimorio de un id
        Method: POST
    """
    try:
        # Extrae el grimorio de un registro
        register = api_crud.select_grimorio(dbs,id)
        return {"id":register.id, "grimorio":register.grimorio}
    except:
        return {"id":id, "grimorio":"No Asignado"}

@academy.post("/api/update/",response_class= HTMLResponse)
def update_student(
    request:Request,
    id:str=Form(),
    first_name:str=Form(),
    last_name:str=Form(),
    age:int = Form(),
    magic_affinity:str = Form(),
    dbs: Session= Depends(db.get_db)):
    
    
    user = {
        "id":id,
        "first_name": first_name,
        "last_name": last_name,
        "age":age,
        "magic_affinity":magic_affinity,
    }
    """
        Endpoint: actualiza un registro de la academia
        Method: POST
    """
    try:
        # Actualiza un registro
        register = api_crud.update_user(dbs,user)
        return templates.TemplateResponse("index.html", {"request":request})
    except:
        return {"status": "Not found"}

@academy.post("/api/status/",response_class= HTMLResponse)
def update_status(
    request:Request,
    id:str = Form(), 
    dbs: Session= Depends(db.get_db)):
    """
        Endpoint: actualiza el status de una solictud
        Method: POST
    """
    try:
        # actualiza el status de una solictud
        register = api_crud.update_status(dbs,id)
        return templates.TemplateResponse("index.html", {"request":request})
    except:
        return {'Update status': "Erro not found"}


@academy.post("/api/delete_student",response_class= HTMLResponse )
def delete_student(
    request:Request,
    id:str = Form(), 
    dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Elimina un registro por id
        Method: POST
    """
    try:
        # Elimina un registro
        register = api_crud.delete_student(dbs,id)
        return templates.TemplateResponse("index.html", {"request":request})
    except Exception as e:
        raise e   