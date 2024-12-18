from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Role, CrewMember

database = "sqlite:///strawhatcrew.db"
engine = create_engine(database)
Session = sessionmaker(bind = engine)
session = Session()

def init_db():
