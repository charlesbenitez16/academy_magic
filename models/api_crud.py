
from fastapi import HTTPException
from sqlalchemy.orm import Session
from config import db_models
from schema import academy_schema
import utils.constants as constants


def verify_id(dbs: Session, id: str) -> list:
    """
    funcion para buscar la solicitud de registro y validarla.

    Params:
        dbs: conexion con la base de datos.
        id: id de solicitud para buscar en base de datos.

    Returns:
        item: una lista de objeto del modelo StudentAcademy.
    """
    item = (
        dbs.query(db_models.StudentAcademy)
        .filter(db_models.StudentAcademy.id == id)
        .first()
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Id not Found")

    return item


def update_user(dbs: Session, user: academy_schema.Agree) -> list:
    """
    Actualiza los registros en la Base de datos.

    Params:
        dbs: conexion con la base de datos
        user: objeto de tipo Agree para actualizar el item en la base de datos.

    Returns:
        item: una lista de objeto del modelo StudentAcademy..
    """
    item = verify_id(dbs, user.id)
    item.first_name = user.first_name
    item.last_name = user.last_name
    item.age = user.age
    item.magic_affinity = user.magic_affinity

    dbs.add(item)
    dbs.commit()
    dbs.refresh(item)
    return item


def create_user(
    dbs: Session, user: academy_schema, grimorio: str
) -> db_models.StudentAcademy:
    """
    Crea un estudiante en la Base de datos

    Params:
        dbs : conexion con la base de datos
        user : objeto de tipo Agree para crear un item.
        grimorio: string aleatorio de un grimorio.

    Returns:
        user: un objeto del modelo StudentAcademy.
    """
    user = db_models.StudentAcademy(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        magic_affinity=user.magic_affinity,
        grimorio=grimorio,
        status=constants.STATUS_INPUT,
    )

    dbs.add(user)
    dbs.commit()

    return user


def update_status(dbs: Session, id: str) -> list:
    """
    Actualiza el estatus de la solicitud del registro.

    Params:
        dbs: conexion con la base de datos
        id: id de solicitud para buscar en la base de datos.

    Returns:
        item: una lista de objeto del modelo StudendAcademy.
    """
    item = verify_id(dbs, id)
    item.status = constants.STATUS_UPDATE
    dbs.add(item)
    dbs.commit()
    dbs.refresh(item)
    return item


def select_grimorio(dbs: Session, id: str) -> list:
    """
    Muestra el grimorio de un registro especifico.

    Params:
        dbs: conexion con la base de datos.
        id : id de solicitud para buscar en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = verify_id(dbs, id)
    return item


def delete_student(dbs: Session, id: str) -> list:
    """
    Elimina un registro.

    Params:
        dbs: conexion con la base de datos.
        id: id de solicitud para eliminar en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = verify_id(dbs,id)
    dbs.delete(item)
    dbs.commit()
    return item