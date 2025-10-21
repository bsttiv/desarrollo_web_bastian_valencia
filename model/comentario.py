from .db import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey, DateTime

class Comentario(Base):
    __tablename__ = "comentario"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha=Column(DateTime, nullable=False)
    aviso_id=Column(BigInteger, ForeignKey("aviso_adopcion.id"), nullable=False)