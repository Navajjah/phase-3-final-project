from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    skills = Column(String, nullable=False)
    duties = Column(String,nullable=True)

    members = relationship('CrewMember', back_populates='role')

    def __repr__(self):
        return f"Role(id = {self.id}, name= '{self.name}, skills='{self.skills}, duties='{self.duties}')"
    
class CrewMember(Base):
    __tablename__ = "CrewMember"

    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    ability = Column(String, nullable=False)
    dream= Column(String, nullable=False)
    bounty= Column(Integer, nullable=False)

    role = relationship('Role', back_populates='members')
    
    def __repr__(self):
        return f"CrewMember(id = {self.id}, name='{self.name}', ability='{self.ability}', dream='{self.dream}', bounty= {self.bounty}, role= '{self.role.name}')"
    