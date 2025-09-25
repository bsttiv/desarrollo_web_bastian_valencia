from .db import Base
from .comuna import Comuna
from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.orm import relationship

class Region(Base):
    __tablename__ = "region"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="regiones")