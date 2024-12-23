from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Role, CrewMember, Ship
import sys

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
    existing_role = session.query(Role).filter_by(name=name).first()
    if existing_role:
        print(f"Role with name '{name}' already exists. No action taken.")
        return
    role = Role(name=name, skills=skills, duties=duties)
    session.add(role)
    session.commit()
    print(f"Role '{name}' created with ID {role.id}")

def update_role():
    role_id = int(input("Enter Role ID to update: "))
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
    role = session.get(Role, role_id)

    if not role:
        print(f"Role with ID {role_id} does not exist")
        return
    crewmember = CrewMember(name=name, ability=ability, dream=dream, bounty=bounty, role_id=role_id)
    session.add(crewmember)
    session.commit()
    print(f"🏴‍☠️ A new Straw Hat has joined! '{name}' (ID: {crewmember.id}) is now part of the adventure as a '{role_id}'! 🌟")


def update_crewmember():
    crewmember_id = int(input("Enter CrewMembers ID to update: "))
    crewmember = session.get(CrewMember, crewmember_id)

    if not crewmember:
        print(f"The Strawhat with ID {crewmember_id} does not exist")
        return
    crewmember.name = input(f"Enter new CrewMember's name: (current: {crewmember.name}): ")
    crewmember.ability = input(f"Enter new CrewMember's ability: (current: {crewmember.ability}): ")
    crewmember.dream = input(f"Enter new CrewMember's dream: (current: {crewmember.dream}): ")
    crewmember.bounty = int(input(f"Enter new CrewMember's bounty: (current: {crewmember.bounty}): "))
    new_role_id = int(input(f"Enter new Role ID for CrewMember: (current: {crewmember.role_id}): "))
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

def create_ship():
    name = input("Enter Ship Name: ")
    ship_wright = input("Enter ShipWright's Name: ")
    max_capacity = int(input("Enter Maximum Capacity of Crew: "))

    existing_ship = session.query(Ship).filter_by(name=name).first()
    if existing_ship:
        print(f"A ship with the name '{name}' already exists!")
        return

    ship = Ship(name=name, ship_wright=ship_wright, max_capacity=max_capacity)
    session.add(ship)
    session.commit()
    print(f"🚢 Ship '{name}' has been created with ID {ship.id}!")


def update_ship():
    ship_id = int(input("Enter Ship ID to update: "))
    ship = session.get(Ship, ship_id)

    if not ship:
        print(f"Ship with ID {ship_id} does not exist.")
        return

    ship.name = input(f"Enter new Ship Name (current: {ship.name}): ")
    ship.ship_wright = input(f"Enter new Captain's Name (current: {ship.ship_wright}): ")
    ship.max_capacity = int(input(f"Enter new Maximum Capacity (current: {ship.max_capacity}): "))
    session.commit()
    print(f"🚢 Ship ID {ship_id} updated successfully!")


def delete_ship():
    ship_id = int(input("Enter Ship ID to delete: "))
    ship = session.get(Ship, ship_id)

    if not ship:
        print(f"Ship with ID {ship_id} does not exist.")
        return

    session.delete(ship)
    session.commit()
    print(f"🚢 Ship ID {ship_id} has been deleted!")

def assign_crewmember_to_ship():
    crewmember_id = int(input("Enter CrewMember's ID: "))
    ship_id = int(input("Enter Ship ID: "))
    crewmember = session.get(CrewMember, crewmember_id)
    ship = session.get(Ship, ship_id)

    if not crewmember:
        print(f"No crewmember found with ID {crewmember_id}")
        return
    if not ship:
        print(f"No ship found with ID {ship_id}")
        return
    
    crewmember.ship_id = ship_id
    session.commit()
    print(f"CrewMember '{crewmember.name}' has been assigned to the ship '{ship.name}' successfully!")


def list_ships():
    ships = session.query(Ship).all()
    if not ships:
        print("No ships found.")
        return

    for ship in ships:
        print(ship)


def main_menu():
    while True:
        print("\n 🌟Welcome aboard the Thousand Sunny, the ship of dreams and nakama!🌟 What would you like to do?")
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
        print("11. Create a Ship")
        print("12. Update a ship")
        print("13. Delete a ship")
        print("14. Assign a crewmember to a ship")
        print("15. List ships")
        print("16. Exit")
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
        elif option == "7":
            assign_crewmember()
        elif option == "8":
            list_roles()
        elif option == "9":
            list_crewmembers()
        elif option == "11":
            create_ship()
        elif option == "12":
            update_ship()
        elif option == "13":
            delete_ship()
        elif option == "14":
            assign_crewmember_to_ship()
        elif option == "15":
            list_ships()
        elif option == "16":
            print("You are now exiting the Thousand Sunny⛵..... To be continued")
            sys.exit()
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main_menu()

    