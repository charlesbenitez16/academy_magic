import os
from dotenv import load_dotenv
#import pandas as pd
# Cargar .env
load_dotenv()
#PATH_HOME = os.getcwd()

# Leer variables de entorno

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
BD_NAME = os.getenv("bd_name")
PORT = os.getenv("port")

# Constants
STATUS_INPUT = False
STATUS_UPDATE = True
STATUS_PENDIND = "pending"
STATUS_ACCEPTED = "accept"



list_magic = ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]


tupla_grimorios = [
    ("Sinceridad", "Trébol de 1 hoja"),
    ("Esperanza", "Trébol de 2 hojas"),
    ("Amor", "Trébol de 3 hojas"),
    ("Buena Fortuna", "Trébol de 4 hojas"),
    ("Desesperación", "Trébol de 5 hojas"),
]