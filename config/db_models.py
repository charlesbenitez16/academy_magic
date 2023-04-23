from sqlalchemy import Column, SmallInteger, String, Boolean, Tuple as SqlTuple
from config.db import Base


class StudentAcademy(Base):
    """
    Modelo para crear la Base de datos
    """

    __tablename__ = "academy_users"
    id = Column(String(10), primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(SmallInteger)
    magic_affinity = Column(String(20))
    grimorio = Column(String(255))
    status = Column(String(20), default=True)