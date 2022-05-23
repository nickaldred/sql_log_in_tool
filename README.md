# sql_log_in_tool
A login tool for a website that allows the user to register for an account, and then lets the user log in with their registered details. 
The user's password is encrypted using Bcrypt and then stored in a MySQL database.

This system interacts with an SQL database hosted online by implemenitng API features.
Prepared statements are used to prevent SQL injection and all SQL code is implemented in the Db class.
All backend code is located in the Log_in file.

HTML and CSS are used to display and style the page in a web browser.

-------------------------------------------------------------------------------

Using the log in portal.

First register for an account, using the details provided.
Please note passwords are requried to contain a capital letter, standard letter, a number and a special character.

When registered please enter in the correct details to log in to the system.


On successful login not much will happen.
This is becuase this tool is designed to be implemented into an existing site, where login credentials are required. 

One way of implementing this into a site is upon a successful login returning a JWT token.




