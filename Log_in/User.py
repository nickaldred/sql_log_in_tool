
#from _typeshed import Self
import datetime
import re
from Log_in.Password import Password
from Log_in.db import Db
from dotenv import load_dotenv
import os

load_dotenv()




class User: 
    """An object that creates a user using the provided details and then 
    encrypts that data and stores it in a database for future use"""
    

    def __init__ (self, first_name, surname, email_address, password):
        self.first_name = first_name
        self.surname = surname
        self.email_address  = email_address
        self.password = password

    def check_details(self, render_template, accform, password, firstname, 
        surname, email):
        """ A method that runs all the other methods of the class to create a 
        list of errors contained in dictionarys and returns the render template 
        based on error or non error"""

        error = (self.check_first_name(), self.check_surname(), 
        self.check_email(), self.check_password())
        if error[0]['firstname'] == True:
            return(render_template('user_registration.html', result = True, 
            accform = accform, log = "Please enter a valid first name"))

            
        elif error[1]['surname'] == True:
            return(render_template('user_registration.html', result = True, 
            accform = accform, log = "Please enter a valid surname"))


        elif error[2]['email'] == True:
            return(render_template('user_registration.html', result = True, 
            accform = accform, log = "Please enter a valid email address"))

        elif error[3]['password'] == True:
            return(render_template('user_registration.html', result = True, 
            accform = accform, log = "Please enter a valid password"))



        else:
            #encrypts password with bcrypt
            encrpyt = Password(password)
            hashed = encrpyt.hash()
            hashed = hashed.decode("utf-8") 
            newuser = User(first_name=firstname, surname=surname, 
            email_address=email, password=hashed)

            #connects to the account database and create a cursor, then saves 
            # the account to the database.
            database = Db(host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"), 
            password=os.environ.get("MYSQL_PASS"), 
            database=os.environ.get("MYSQL_NAME")) 
            conn = database.connect_db()
            cursor = database.create_cursor(conn)
            database.create_db(cursor)
            database.add_data(cursor=cursor, account=newuser)
            database.commit_data(conn=conn) 

            return(render_template('user_registration.html', result = True, 
            accform = accform, log = "Account created successully"))
        


    def check_first_name(self):
        """
        A method that checks the first name is not empty.

        """

        if self.first_name == "":
            error = {"firstname" : True}
            return(error)
        else:
            error = {"firstname" : False}
            return(error)

        
        


    def check_surname(self):
        """
        A method that checks the second name is not empty
        
        """

        if self.surname == "":
            error = {"surname" : True}
            return(error)
        else:
            error = {"surname" : False}
            return(error)
        


              

    def check_email(self):
        """
        A method that checks email address provided is a valid email.

        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if((re.fullmatch(regex, self.email_address)) == None):
            error = {"email" : True}
            return(error)
        else:
            error = {"email" : False}
            return(error)
                
        
    def check_password(self):
        """
        A method that checks the password is a valid password in the correct 
        format.
        """    

        error = {"password": True} 
        if (len(self.password)<8):
            return(error)
        elif not re.search("[a-z]", self.password):
            return(error)
        elif not re.search("[A-Z]", self.password):
            return(error)
        elif not re.search("[0-9]", self.password):
            return(error)
        elif not re.search("[!@#$%^&*()-+?_=,<>/]", self.password):
            return(error)
        elif re.search("\s", self.password):
            return(error)
        else:
            error = {"password" : False}
            return(error)



            