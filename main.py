# Import files 
from ui.cli import start
from services import database

#creates tables
database.create_tables()


#Welcoming 
print("+-+-+-+-+-+-+-+-Welcome to the Finy Finance tracker+-+-+-+-+-+-+-+-")

#Starting the loop of cli
start()

