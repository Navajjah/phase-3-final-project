# Strawhat Cli Application
This is a simple Command-line Interface (CLI) for managing and interacting with the Strawhat Crew, inspired by the popular anime series, *One Piece*. The app allows uses to manage crew members and their roles within the crew or their ship the *Thousand Sunny*.

## Features
- Create, update, and delete crew roles i.e Captain, Cook
- Create, update, and delet crew members i.e Monkey. D. Luffy, Roronoa Zoro etc.
- Each role can have associated skills and duties.
- Each crew member can have their abilities, dreams and bounties associated with them.
- Interact with a SQLite database to store and retrieve crew member data.

## Requirements
- Python 3.12 or higher
- SQLAlchemy 

## Installation
1. Clone the repository
`git clone https://github.com/your-username/strawhat-crew-cli.git
cd strawhat-crew-cli`
2. Install dependencies
`pipenv install sqlalchemy alembic`
3. Run the `pipenv shell` to create a virtual environment

## Usage
1. Run the CLI 
- To start the application, simply run the command:
`python cli.py` or `python3 cli.py`

2. Available Commands
- The application will show the following options in the menu:
Create Role
Update Role
Delete Role
List Roles
Create CrewMember
Update CrewMember
Delete CrewMember
Assign CrewMember
List CrewMember

## Database Schema
The database consists of the following tables:
- roles: Stores information about crew roles.
- crewmembers: stores information about individual crew members.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- The application is inspired by the One Piece universe and its characters.
- SQLAlchemy was used for ORM functionality.

