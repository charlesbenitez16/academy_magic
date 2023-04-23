import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import academy_schema
from config import db_models, db
from models import api_crud
from utils import constants
import json

academy = APIRouter()

@academy.post("/api/solicitud")
def create_solicitud(user:academy_schema.Agree, dbs: Session= Depends(db.get_db)):
    """
        Endpoint: crear una nueva solictud
        Method: POST
    """
    grimorio_tuple = random.choice(constants.tupla_grimorios)
    grimorio = f"{grimorio_tuple[0]}, {grimorio_tuple[1]}"
    try:
        db_item = api_crud.create_user(dbs, user, grimorio)

        result = academy_schema.ResultJson(
            id = db_item.id,
            first_name=db_item.first_name,
            last_name=db_item.last_name,
            age=db_item.age,
            magic_affinity=str(db_item.magic_affinity),
            grimorio=db_item.grimorio,
            status= "Accept"#str(constants.STATUS_PENDIND),
        )
        #my_json = result.show_json()
        #print(my_json)
        return result.to_JSON()
    except Exception as e:
        raise e

@academy.get("/api/get_only_user")
def get_user(id:str, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Trae un solo registro de la base de datos
        Method: GET
    """
    payload = api_crud.verify_id(dbs,id)

    return payload

@academy.get("/api/get_users")
def get_users(dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Trae todos los registros de la base de datos
        Method: GET
    """
    payload = dbs.query(db_models.StudentAcademy).all()

    return payload


@academy.get("/api/get_grimorio/")
def get_grimorio(id:str,dbs:Session = Depends(db.get_db)):
    """
        Endpoint: Trae el grimorio de un id
        Method: POST
    """
    
    db_item = api_crud.select_grimorio(dbs,id)

    return {"id":db_item.id, "grimorio":db_item.grimorio}

@academy.put("/api/update/")
def update_student(id:academy_schema.Agree, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: actualiza un registro de la academia
        Method: PUT
    """
    db_item = api_crud.update_user(dbs,id)

    return {"status": "successfully"}

@academy.put("/api/status/")
def update_status(id:str, dbs: Session= Depends(db.get_db)):
    """
        Endpoint: actualiza el status de una solictud
        Method: PUT
    """
    db_item = api_crud.update_status(dbs,id)
    return {'Update status': constants.STATUS_ACCEPTED}


@academy.delete("/api/delete_student")
def delete_student(id:str, dbs: Session = Depends(db.get_db)):
    """
        Endpoint: Elimina un registro por id
        Method: DELETE
    """
    db_item = api_crud.delete_student(dbs,id)
    return {"User": db_item}
       