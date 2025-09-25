from .db import Base
from sqlalchemy import Column, BigInteger, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
from .aviso_adopcion import AvisoAdopcion

class Foto(Base):
    __tablename__ = "foto"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    aviso_id = Column(BigInteger, ForeignKey("aviso_adopcion.id"), nullable=False)

    #avisos = relationship('AvisoAdopcion', back_populates="fotos")