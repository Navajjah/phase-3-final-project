from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Role, CrewMember

database = "sqlite:///strawhatcrew.db"
engine = create_engine(database)
Session = sessionmaker(bind = engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("The Database is initialized")

def create_role():
    name = input("Enter Role: ")
    skills = input("Enter Skills: ")
    duties = input("Enter duties: ")
    role = Role(name=name, skills=skills, duties=duties)
    session.add(role)
    session.commit()
    print(f"Role '{name}' created with ID {role.id}")

def update_role():
    role_id = int("Enter Role ID to update: ")
    role = session.get(Role, role_id)
    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    role.name = input(f"Enter new Role (current: {role.name}): ")
    role.skills = input(f"Enter new skills (current: {role.skills}): ")
    role.duties = input(f"Enter new duties (current: {role.duties}): ")
    session.commit()
    print(f"Role ID {role_id} updated successfully!!")

def delete_role():
    role_id = int(input("Enter Role ID to delete: "))
    role = session.get(Role, role_id)

    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    session.delete(role)
    session.commit()
    print(f"Role ID {role_id} has been deleted successfully!!")

def create_crewmember():
    name = input("Enter CrewMember's name: ")
    ability = input("Enter CrewMember's ability: ")
    dream = input("Enter CrewMember's dream: ")
    bounty = int("Enter CrewMember's bounty: ")
    role_id = int("Enter Role ID: ")
    role = (Role, role_id)
    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    crewmember = CrewMember(name=name, ability=ability, dream=dream, bounty=bounty)
    session.add(crewmember)
    session.commit()
    print(f"🏴‍☠️ A new Straw Hat has joined! '{name}' (ID: {crewmember.id}) is now part of the adventure as a '{role_id}'! 🌟")


def update_crewmember():
    crewmember_id = int("Enter CrewMembers ID to update: ")
    crewmember = session.get(CrewMember, crewmember_id)

    if not crewmember:
        print(f"The Strawhat")