from sqlalchemy import Column,String,Text,ForeignKey,Integer
from db import Base,engine

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    email=Column(String(100),unique=True)
    password=Column(String(100))

class Reports(Base):
    __tablename__="reports"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    resume_text=Column(Text)
    result=Column(Text)


if __name__=="__main__":
    print("creating")
    Base.metadata.create_all(bind=engine)