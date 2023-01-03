from sqlalchemy import Boolean, Column, String, Text, Integer
from sqlalchemy.ext.declarative  import declarative_base

import uuid

Base = declarative_base()


class Memo(Base):
    __tablename__ = 'memos'

    id = Column(String(120), primary_key = True, default = lambda : str(uuid.uuid4()))
    title = Column(String(80), default ='No title', nullable = False, index = True)
    content = Column(Text, nullable = True)
    is_favorite = Column(Boolean, nullable = False, default = False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    password = Column(String(100), nullable = False)