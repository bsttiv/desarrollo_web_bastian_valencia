import enum
from .db import Base
from sqlalchemy import Column, BigInteger, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
from .aviso_adopcion import AvisoAdopcion

class TipoContacto(enum.Enum):
    whatsapp = 1
    telegram = 2
    x = 3
    instagram = 4
    tiktok = 5
    otra = 6

class ContactarPor(Base):
    __tablename__ = "contactar_por"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(Enum(TipoContacto), nullable=False)
    identificador = Column(String(150), nullable=False)
    aviso_id = Column(BigInteger, ForeignKey("aviso_adopcion.id"), nullable=False)

    #avisos = relationship('AvisoAdopcion', back_populates="contacto")