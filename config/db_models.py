from sqlalchemy import Column, SmallInteger, String, Boolean, Tuple as SqlTuple
from config.db import Base


class StudentAcademy(Base):
    """
    Modelo para crear la Base de datos
    """

    __tablename__ = "academy_users"
    id = Column(String(10), primary_key=True)
    first_name = Column(String(20),nullable=False)
    last_name = Column(String(20),nullable=False)
    age = Column(SmallInteger,nullable=False)
    magic_affinity = Column(String(20),nullable=False)
    grimorio = Column(String(255),nullable=False)
    status = Column(String(20), nullable=False)