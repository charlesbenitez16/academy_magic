import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import academy_schema
from config import db_models, db
from models import api_crud
from utils import constants


academy = APIRouter()

@academy.post("/api/solicitud")
def create_solicitud(user:academy_schema.Agree, dbs: Session= Depends(db.get_db)):
    """
        Endpoint: crear una nueva solictud
        Method: POST
    """
    
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

        return result.to_JSON()
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

@academy.get("/api/get_users")
def get_users(dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Trae todos los registros de la base de datos
        Method: GET
    """
    try:
        # Extrae todos los registros.
        payload = dbs.query(db_models.StudentAcademy).all()
        return payload
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
@academy.put("/api/update/")
def update_student(id:academy_schema.Agree, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: actualiza un registro de la academia
        Method: PUT
    """
    try:
        # Actualiza un registro
        register = api_crud.update_user(dbs,id)
        return {"status": "successfully"}
    except:
        return {"status": "Not found"}

@academy.put("/api/status/")
def update_status(id:str, dbs: Session= Depends(db.get_db)):
    """
        Endpoint: actualiza el status de una solictud
        Method: PUT
    """
    try:
        # actualiza el status de una solictud
        register = api_crud.update_status(dbs,id)
        return {'Update status': constants.STATUS_ACCEPTED}
    except:
        return {'Update status': "Erro not found"}


@academy.delete("/api/delete_student")
def delete_student(id:str, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Elimina un registro por id
        Method: DELETE
    """
    try:
        # Elimina un registro
        register = api_crud.delete_student(dbs,id)
        return {"User": register}
    except Exception as e:
        raise e 
       