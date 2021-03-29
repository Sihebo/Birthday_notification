
import sqlite3
from sqlite3 import Error
import os


def create_connection(path):  # Function to create DB and create connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        #print("Connection to SQLite DB successful.")
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# Connect to DB and create connection variable.
connection = create_connection("Path_to_DB/Birthday_DB.sqlite")


print("\nWelcome to Simon`s birthdays notification script. \n") # Welcome message of script, printed to terminal.

# Function to quit, when choice has been made to create new entry or delete existing one.
def quit(variable):
    while True:
        if variable == "q": # If 'q' is typed, the main function is called and if clause is no longer continued.
            main()
            break
        else:
            break

# Main function with different possibilities in 'menu'.
def main():
    print("###################")
    print("Type 'N' to create a new entry.")
    print("Type 'O' to get an overview of all entries.")
    print("Type 'D' to delete an entry.")
    print("Type 'E' to exit the script.")
    print("###################\n")

    choice = input("Please make a choice: ")

    if choice == "N" or choice == "n": # Name, birthday and relation are stored in variables. After each variable, quit() function is called, so that if clause is skipped in case 'q' is typed in.
        print("You chose to make a new entry. Type 'q' to exit.")
        name = input("Insert name here: ")
        quit(name)
        birthday = input("Insert date of birth here (Format:YYYY-MM-DD): ")
        quit(birthday)
        relation = input("Insert relation here (choose either 'family' or 'friends'): ")
        quit(relation)

        def new_entry(con): # Function that creates new entry in DB with created variables.
            cur = con.cursor() # Create cursor object
            try: # Execute method on cursor object,  to make query.
                cur.execute("INSERT INTO birthdays (name, birth_data, relation) VALUES (?,?,?);", (name, birthday, relation))
                con.commit() # Save (commit) changes with .commit method.
                print("Query executed succesfully.")
            except Error as e:
                print(f"The error '{e}' occurred.")

        new_entry(connection) # Call function to insert new entries with connection object.

        os.system('clear') # Clear terminal.

        main() # Call main function again.

    elif choice == "O" or choice == "o": # Outputs an overview of all entries to the terminal
        print("You chose to get an overview of all entries. \n")
        def execute_read_query(connection, query): # overview function
            cursor = connection.cursor()
            result = None
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"The error '{e}' occurred.")

        select_users = "SELECT * from birthdays" # SQLite query to output all entries stored in 'birthdays' table.
        users = execute_read_query(connection, select_users)

        for user in users: # For loop, to loop over every entry in 'birthdays' table
            print(user)

        main()

    elif choice == "D" or choice == "d": # Delete entry clause.
        print("You chose to delete an entry. Type 'q' to quit.")
        name_delete = input("Enter name of entry you want to delete: ") # Variable to store name of entry that should be deleted
        name_delete = '%' + name_delete + '%' # Add SQL wildcard characters to query name

        quit(name_delete) # Call quit() to exit delete.


        def delete_entry(con): # Define delete function.
            cursor = con.cursor()
            try:
                cursor = connection.cursor()
                #print("delete from birthdays where name like (?);", (name_delete,))
                cursor.execute("delete from birthdays where name like (?);", (name_delete,)) # SQLite statement to delete name stored in 'name_delete' variable.
                connection.commit()
                print("The entry " + name_delete.strip('%') + " was deleted succesfully.")
            except Error as e:
                print(f"The error '{e}' occurred.")

        delete_entry(connection) # Call delete function with connection object.

        main()

    elif choice == "E" or choice == "e": #Exit script.
        print("Goodbye!")
        exit()

    else:
        os.system('clear')
        main()



main()







