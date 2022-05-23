from logging import log
from flask.views import MethodView
from wtforms import Form, StringField
from flask import Flask, render_template, request
from wtforms.fields.simple import EmailField, SubmitField, PasswordField
from Log_in.db import Db
from Log_in.User import User
from Log_in.Password import Password


app = Flask(__name__)

class LogInPage(MethodView):
    """
    Create a log in page oject return the log in form and then gathers
    the details on the post request.
    """
    def get(self):
        log_in_form = LogInForm()
        return(render_template('log_in_page.html', loginform = log_in_form))

    def post(self):
        loginform = LogInForm(request.form)
        email = loginform.username.data
        password = loginform.password.data
        password = Password(password)

        if email == "":
            return(render_template('log_in_page.html', result = True,
            loginform = loginform, log = "Invalid email or password"))
        
        template = password.verify_password(email)
        print(email)



        if template == True:
            return(render_template('log_in_page.html', result = True, 
            loginform = loginform, log = "Correct"))

        elif template == False:
            return(render_template('log_in_page.html', result = True, 
            loginform = loginform, log = "Invalid email or password"))



class RegPage(MethodView):
    """
    Create a registration page oject return the registration form and 
    then gathers the details on the post request.
    """
    def get(self):
        acc_form = AccForm()
        return(render_template('user_registration.html', 
        accform = acc_form))

    def post(self):

        accform = AccForm(request.form)
        firstname = accform.firstname.data
        surname = accform.surname.data
        email = accform.username.data
        password = accform.password.data

        newuser = User(first_name=firstname, surname=surname, 
        email_address=email, password=password)
        print(newuser.first_name)
        error = newuser.check_details(render_template = render_template, 
        accform=accform, password = password, firstname=firstname, 
        surname=surname, email=email)
        return(error)




class LogInForm(Form):
    """Creates the log in form"""
    username = StringField('Email: ')
    password = PasswordField('Password: ')
    button = SubmitField("Sign In")


class AccForm(Form):
    """Creates the account form"""
    firstname = StringField('First Name:')
    surname = StringField('Surname: ')
    username = StringField('Email Address: ')
    password = PasswordField('Password: ')

    button = SubmitField("Submit")





app.add_url_rule('/', view_func=LogInPage.as_view('log_in_page'))
app.add_url_rule('/create_account', view_func=RegPage.as_view('create_account'))

#app.run(debug=True)