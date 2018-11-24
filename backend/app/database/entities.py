from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Provider(Base):
    __tablename__= 'provider'

    providerId = Column(Integer, primary_key=True, unique=True)
    providerName = Column(String(255),nullable=False)

    def serialize(self):
        return {
            'providerId': self.providerId,
            'providerName': self.providerName,
        }


