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
    crewmember_id = int(input("Enter CrewMember's ID: "))
    role_id = int(input("Enter the new Role ID: "))
    crewmember = session.get(CrewMember, crewmember_id)
    role = session.get(Role, role_id)

    if not crewmember or not role:
        print("Invalid Strawhat ID or Role ID")
        return
    crewmember.role_id = role_id
    session.commit()
    print("Role assigned successfully!!")

def list_roles():
    roles = session.query(Role).all()
    if not roles:
        print("No roles found")
    for role in roles:
        print(role)

def list_crewmembers():
    crewmembers = session.query(CrewMember).all()
    if not crewmembers:
        print("No Strawhats found")
    for crewmember in crewmembers:
        print(crewmember)

def view_crewmembers_by_roles():
    role_id = int(input("Enter Role ID to view crewmembers: "))
    role = session.get(Role, role_id)
    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    crewmembers = role.members
    if not crewmembers:
        print(f"No Strawhats found for role {role_id}")
        return
    print(f"Strawhats belonging to '{role.name}' (ID {role_id}): ")
    for crewmember in crewmembers:
        print(crewmember)

def main_menu():
    while True:
        print("\n Welcome to the Strawhat crew. What would you like to do?")
        print("1. Create a Role")
        print("2. Update a Role")
        print("3. Delete a Role")
        print("4. Create a CrewMember")
        print("5. Update a CrewMember")
        print("6. Delete a CrewMember")
        print("7. Assign CrewMember to a role")
        print("8. List Roles")
        print("9. List CrewMembers")
        print("10. View Roles by CrewMembers")
        print("11. Exit")
        option = input("Enter your choice: ")

        if option == "1":
            create_role()
        elif option == "2":
            update_role()
        elif option == "3":
            delete_role()
        elif option == "4":
            create_crewmember()
        elif option == "5":
            update_crewmember()
        elif option == "6":
            delete_crewmember()
        
            
    