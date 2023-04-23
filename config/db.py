from venv import create
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import constants

engine = create_engine(f"mysql+pymysql://{constants.USER}:{constants.PASSWORD}@{constants.HOST}:{constants.PORT}/{constants.BD_NAME}")
#engine = create_engine(f"mysql+pymysql://charles:cjbb1234@localhost:3306/academic_magic")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Crear tablas
# Base.metadata.create_all(bind=engine)


def get_db():
    """
    conexion database
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


#conn = engine.connect()



#meta_data = MetaData()
  