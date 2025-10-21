from sqlalchemy import create_engine, desc as descend, extract, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

import enum
from sqlalchemy import Column, Integer, BigInteger, Enum, String, ForeignKey, DateTime, Text

class TipoAnimal(enum.Enum):
    gato = 1
    perro = 2

class UnidadMedida(enum.Enum):
    a = 1
    m = 2

class AvisoAdopcion(Base):
    __tablename__ = "aviso_adopcion"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    comuna_id = Column(BigInteger, ForeignKey("comuna.id"), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    celular = Column(String(15), nullable=True)
    tipo = Column(Enum(TipoAnimal), nullable=False)
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(Enum(UnidadMedida), nullable=False)
    fecha_entrega = Column(DateTime, nullable=False)
    descripcion = Column(Text, nullable=True)
    
def numero_avisos_mes():
    from datetime import datetime
    session = SessionLocal()
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    avisos_del_mes = session.query(AvisoAdopcion.fecha_ingreso, func.count(AvisoAdopcion.id)).filter(
        extract('month', AvisoAdopcion.fecha_ingreso) == mes_actual,
        extract('year', AvisoAdopcion.fecha_ingreso) == año_actual
    ).group_by(AvisoAdopcion.fecha_ingreso).all()
    session.close()
    return avisos_del_mes


session = SessionLocal()
session = SessionLocal()
mes_actual = datetime.now().month
año_actual = datetime.now().year
avisos_del_mes = session.query(extract('day', AvisoAdopcion.fecha_ingreso), extract('month', AvisoAdopcion.fecha_ingreso), extract('year', AvisoAdopcion.fecha_ingreso), func.count(AvisoAdopcion.id)).filter(
    extract('month', AvisoAdopcion.fecha_ingreso) == mes_actual,
    extract('year', AvisoAdopcion.fecha_ingreso) == año_actual
).group_by(extract('day', AvisoAdopcion.fecha_ingreso), extract('month', AvisoAdopcion.fecha_ingreso), extract('year', AvisoAdopcion.fecha_ingreso)).all()
session.close()
print(avisos_del_mes)