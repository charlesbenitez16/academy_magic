
from pydantic import BaseModel, validator
import utils.constants as constants
from utils.utils import find_info

class Agree(BaseModel):
    """
    Clase para hacer una solicitud a la academia.

    """
    id: str
    first_name: str
    last_name: str
    age: int
    magic_affinity: str


    @validator("first_name", "last_name")

    def validate_namess(cls, value: str) -> str:
        """
        Nombre con solo letras.
        """
        if not find_info("^[^0-9]+$", value):
            raise ValueError("El campo debe contener maximo 20 caracteres solo letras.")
        return value


    @validator("age")
    # pylint: disable=no-self-argument
    def valide_age(cls, value: int) -> int:
        """
        Validacion de la edad
        """
        if not find_info("^[0-9]{2}$", str(value)):
            raise ValueError("El campo debe contener solo números de 2 dígitos")
        return value

    @validator("magic_affinity")

    def magical_affinity_verify_value(cls, value: str) -> str:
        """
        Validar Afinidad magica
        """
        affinity = set(constants.list_magic)
        if not value in affinity:
            raise ValueError(f"El valor {value} no está permitido")
        return value


class ResultJson(BaseModel):
    """
    clase que construye JSON para tener un body.
    """
    id:str
    first_name: str
    last_name: str
    age: int
    magic_affinity: str
    grimorio: str
    status: str

    def to_JSON(self) -> dict:
        """
        funcion para retornar un body en formato JSON.
        """
        json = {
            'id': self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "magic_affinity": self.magic_affinity,
            "grimorio": self.grimorio,
            "status": self.status,
        }
        return json
