import enum
from .db import Base
from .comuna import Comuna
from sqlalchemy import Column, Integer, BigInteger, Enum, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

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

    #comunas = relationship('Comuna', back_populates="avisos")