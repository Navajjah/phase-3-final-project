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
    bounty = int(input("Enter CrewMember's bounty: "))
    role_id = int(input("Enter Role ID: "))
    role = (Role, role_id)

    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    crewmember = CrewMember(name=name, ability=ability, dream=dream, bounty=bounty)
    session.add(crewmember)
    session.commit()
    print(f"🏴‍☠️ A new Straw Hat has joined! '{name}' (ID: {crewmember.id}) is now part of the adventure as a '{role_id}'! 🌟")


def update_crewmember():
    crewmember_id = int(input("Enter CrewMembers ID to update: "))
    crewmember = session.get(CrewMember, crewmember_id)

    if not crewmember:
        print(f"The Strawhat with ID {crewmember_id} does not exist")
        return
    crewmember.name = input("Enter new CrewMember's name: (current: {crewmember.name}): ")
    crewmember.ability = input("Enter new CrewMember's ability: (current: {crewmember.ability}): ")
    crewmember.dream = input("Enter new CrewMember's dream: (current: {crewmember.dream}): ")
    crewmember.bounty = input("Enter new CrewMember's bounty: (current: {crewmember.bounty}): ")
    new_role_id = input("Enter new Role ID for CrewMember: (current: {crewmember.role_id}): ")
    if new_role_id:
        new_role = session.get(Role, int(new_role_id))
        if not new_role:
            print(f"The Role with ID {new_role_id} does not exist. Skipping Role update")
        else:
            crewmember.role_id = new_role_id
    session.commit()
    print(f"The Stawhat {crewmember_id} updated successfully")

def delete_crewmember():
    crewmember_id = int(input("Enter CrewMember's ID to delete: "))
    crewmember = session.get(CrewMember, crewmember_id)
    if not crewmember:
        print(f"The Strawhat with ID {crewmember_id} does not exist")
        return
    session.delete(crewmember)
    session.commit()
    print(f"the Strawhat {crewmember_id} deleted successfully!!")

def assign_crewmember():
    studen

    