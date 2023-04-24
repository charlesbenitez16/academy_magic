import os
from dotenv import load_dotenv
#import pandas as pd

load_dotenv()

#variables de entorno
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
BD_NAME = os.getenv("bd_name")
PORT = os.getenv("port")
##########################
# Constants
STATUS_PENDIND = "pending"
STATUS_ACCEPTED = "accepted"



list_magic = ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]


tupla_grimorios = [
    ("Sinceridad", "Trébol de 1 hoja"),
    ("Esperanza", "Trébol de 2 hojas"),
    ("Amor", "Trébol de 3 hojas"),
    ("Buena Fortuna", "Trébol de 4 hojas"),
    ("Desesperación", "Trébol de 5 hojas"),
]