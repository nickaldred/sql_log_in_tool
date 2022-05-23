import mysql.connector
from mysql.connector import connection




class Db:
    """ A class that can create a mySQL database hosted on a server and
    provides all the functions to make use of that
        database such as:
        Add user
        Commit data
        Delete table
        Delete user
        """
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def connect_db(self):
        """ Connects to the database using the details provided to the 
        class and returns the connection so it can be utilised
        """

        conn = mysql.connector.connect(
        host = self.host,
        user = self.user,
        password = self.password,
        database = self.database
        )

        return conn


    def create_cursor(self, conn):
        """Creates and returns a cursor for the mySQL connection that 
        can be used to interact with the database.""" 

        cursor = conn.cursor()
        return(cursor)


    def create_db(self, cursor):
        """Creates a database and table using the mySQL connection."""

        cursor.execute("CREATE DATABASE IF NOT EXISTS sql4483509")
        cursor.execute("""CREATE TABLE IF NOT EXISTS account
        (email VARCHAR(128) PRIMARY KEY, 
        firstname VARCHAR(32),
        surname VARCHAR(32),  
        password VARCHAR(128))""")


    def add_data(self, cursor, account):
        """A method to add a new account to the table using the mySQL 
        connection and using an account object.
        """
        cursor.execute(f"""INSERT INTO account (email, firstname, surname, password) VALUES 
        ('{account.email_address}','{account.first_name}','{account.surname}','{account.password}')""")


    def commit_data(self, conn):
        """A method that commits the data to the table 
        """
        conn.commit()


    def delete_all_rows(self, cursor):
        """A method that deletes all the accounts contained in the 
        accounts table."""

        cursor.execute("DELETE FROM account ")


    def delete_acc(self, cursor, email):
        """A method that deletes an account from the table."""
        
        cursor.execute(f"DELETE FROM account WHERE email = {email}")

    def find_acc(self, cursor, email):
        """A method that finds and returns an account details using the 
        email provided."""
        cursor.execute(f"SELECT * From account WHERE email = '{email}'")
        result = cursor.fetchall()
        return(result)

    







class User: 
    """An object that creates a user using the provided details and 
    then encrypts that data and stores it in a database for future 
    use."""
    

    def __init__ (self, first_name, surname, email_address, password):
        self.first_name = first_name
        self.surname = surname
        self.email_address  = email_address
        self.password = password



