import bcrypt
#from db import Db
from Log_in.db import Db
import os
from dotenv import load_dotenv
load_dotenv()



class Password:
    """ A class that creates an ecrpyt object using the provided password 
    and then has methods to encrypt and also compare passwords. 
    """

    def __init__(self, password):
        self.password = bytes(password, 'utf-8')

    
    def hash(self):
        """
        A method that hash's a password and returns the hashed password
        """
        
        hashed = bcrypt.hashpw(self.password, bcrypt.gensalt())
        return(hashed)


    def compare_pass(self, hashedpass):
        """ A method that compares a new password with a previously hashed 
        password and returns True if the passwords match and False if 
        they dont"""

        if bcrypt.checkpw(self.password, hashedpass):
            return True

        else:
            return False

    def verify_password(self, email):

        """ A method that compares a new password with a previously hashed 
        password and returns True if the passwords match and False if they 
        dont"""

        #connects to the account database and create a cursor
        database = Db(host=os.environ.get("MYSQL_HOST"),user=os.environ.get("MYSQL_USER"), 
        password=os.environ.get("MYSQL_PASS"), database=os.environ.get("MYSQL_NAME")) 
        conn = database.connect_db()
        cursor = database.create_cursor(conn)

        #Creates a search string to find the account with the email address
        email2 = (f"'{email}'")
        searchstring = ("SELECT * FROM account WHERE email =" + email2)
        cursor.execute(searchstring)
        result = cursor.fetchall()
        if result != []:
            password2 = result[0][3]
            password2 = bytes(password2, 'utf-8')
    
            #checks password provided against hashed password in database
            if bcrypt.checkpw(self.password, password2):
                return(True)

            else:
                return(False)
        else:
            return(False)










