from .db import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

class Comuna(Base):
    __tablename__ = "comuna"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(BigInteger, ForeignKey("region.id"), nullable=False)

    regiones = relationship("Region", back_populates="comunas")