from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    skills = Column(String, nullable=False)
    duties = Column(String, nullable=True)

    members = relationship('CrewMember', back_populates='role')

    def __repr__(self):
        return f"Role(id = {self.id}, name = '{self.name}, skills ='{self.skills}, duties ='{self.duties}')"
    
class CrewMember(Base):
    __tablename__ = 'crewmembers'

    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    ability = Column(String, nullable=False)
    dream= Column(String, nullable=False)
    bounty= Column(Integer, nullable=False)
    role_id= Column(Integer, ForeignKey('roles.id'))
    ship_id = Column(Integer, ForeignKey('ships.id')) 

    role = relationship('Role', back_populates='members')
    ship = relationship('Ship', back_populates='members')
    
    def __repr__(self):
        return f"CrewMember(id = {self.id}, name ='{self.name}', ability ='{self.ability}', dream ='{self.dream}', bounty = {self.bounty}, role_id = {self.role_id}, ship_id= {self.ship_id}))"

class Ship(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    ship_wright = Column(String, nullable=False)  
    max_capacity = Column(Integer, nullable=False)  


    members = relationship('CrewMember', back_populates='ship') 

    def __repr__(self):
        return f"Ship(id = {self.id}, name = '{self.name}', ship wright = '{self.ship_wright}', max capacity = '{self.max_capacity}')"