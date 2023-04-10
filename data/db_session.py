from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

db_path = 'users_base.sqlite'
engine = create_engine('sqlite:///%s' % db_path, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

id = 0


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


def add_user(nameus, passwordus):
    global id, session
    id += 1
    c = Users(name=nameus, password=passwordus)
    session.add(c)
    session.commit()

