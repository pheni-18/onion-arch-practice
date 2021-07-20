from ..database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
