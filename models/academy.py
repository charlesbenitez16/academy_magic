from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import SmallInteger, String, Boolean
from config.db import engine, meta_data



academy_users = Table("academy_users", meta_data,
    Column("id",String(10), primary_key = True),
    Column("first_name", String(20), nullable=False),
    Column("last_name",String(20), nullable = False),
    Column("age",SmallInteger, nullable = False),
    Column("magic_affinity",String(20), nullable = False),
    Column("grimorio",String(255), nullable = False),
    Column("status",String(20)))


meta_data.create_all(engine)