# PreciousPals
#### Video Demo:  <https://youtu.be/_kztYwIAhkw>
#### Description:

The PreciousPals web application is a powerful tool for managing your friendships, whether it's to keep track of your closest friends or to stay in touch with acquaintances. The app's intuitive interface allows you to easily add, edit, and delete friends, making it easy to stay on top of your social life. With the ability to create an account and log in, users can keep their friends list secure and private, ensuring that their personal information stays safe.

As the developer of this app, I was motivated by a deep interest and passion for creating tools that help people connect with each other. I believe that having strong social connections is essential for our well-being, and the PreciousPals app is a small but meaningful way to help people build and maintain those connections. In addition, I wanted to challenge myself to build a web application using the Flask framework and to explore the capabilities of Flask SQLAlchemy and Flask-Login.

One of the main reasons why I wrote this app was to improve my Flask development skills. I had been learning Flask for some time and wanted to build a real-world application to apply my knowledge and gain experience. Additionally, I had a personal interest in creating an application that would allow users to manage a list of friends. As someone who values strong relationships, I thought it would be useful to have a tool to help keep track of my own friends and their contact information.

Furthermore, I wanted to create an app that was simple and easy to use. With the PreciousPals app, users can easily create and manage their list of friends without any unnecessary complexity. The app has a clean and user-friendly interface, making it accessible for users with different levels of technical expertise.

I believe that the PreciousPals app has the potential to be useful for a wide range of people, from those who want to keep track of their personal friends to professionals who need to manage a list of contacts. The app provides a simple and effective way to manage and organize contact information, making it an indispensable tool for maintaining strong relationships. Additionally, the app demonstrates the power and versatility of Flask, and can serve as a useful reference for developers who are learning Flask or building their own applications.

### Files:
The PreciousPals App consists of four Python files:

app.py: This is the main file of the app, which contains the Flask application and routes.
models.py: This file contains the SQLAlchemy database models for the app.
views.py: This file contains the Flask views for the app, including rendering templates and handling form submissions.
auth.py: This file contains the Flask authentication logic, including user login and registration.

### Database:

The app uses a SQLite database, which is stored in the database.db file. The database schema is defined in the models.py file.

### Usage:

To run the app, execute the following command in the project directory:

python app.py


### File Explanations:

### app.py:

The app.py file serves as the main entry point for the Flask web application. It creates a Flask instance and sets the necessary configurations such as the secret key and the database URI.

The create_app function is defined in app.py, which is responsible for initializing and configuring the Flask app instance, setting up the SQLAlchemy database object, and registering the blueprints that contain the different routes and views of the app.

In create_app function, two blueprints are registered: views and auth. The views blueprint contains the routes and views for the main functionality of the app, such as viewing user profiles and searching for friends. The auth blueprint contains the routes and views for user authentication, such as registering, logging in, and logging out.

In addition to setting up the blueprints, the create_app function also initializes the Flask-Login extension for user authentication and sets up a user_loader function to load users from the database based on their ID.

Finally, the create_database function is defined to create the SQLite database if it does not already exist.

### models.py:

The models.py file contains the definition of the database tables for the PreciousPals application using SQLAlchemy ORM. It defines two tables: User and Friend.

User table represents the registered users in the application. The table contains the following columns:

id: primary key of the table and is automatically generated by the database.
email: unique email of the user which is used to login into the application.
password: hashed password of the user for security reasons.
name: name of the user.
friends: a one-to-many relationship with the Friend table that links the user with their friends.
Friend table represents the relationship between the users in the application. The table contains the following columns:

id: primary key of the table and is automatically generated by the database.
user_id: foreign key that links the friend with the user who added them as a friend.
friend_id: foreign key that links the friend with the user who they are friends with.
The tables are defined using SQLAlchemy's declarative syntax, which allows us to define the tables as Python classes. These classes define the columns of the tables as class attributes and provide a convenient way to interact with the database.

The models.py file also includes helper functions for retrieving, adding, and deleting data from the database. These functions are used in the views.py file to interact with the database and perform CRUD (Create, Read, Update, and Delete) operations.

### views.py:

The views.py file in your Flask application contains the functions that define how your application will respond to HTTP requests. It is responsible for rendering the templates (if any), fetching data from the database (if required), and returning an HTTP response to the client.

Here is a brief overview of what each of the functions in views.py might be doing:

home: This function handles the HTTP GET request for the homepage of your application. It might fetch some data from the database and pass it to the template that will be rendered by Flask's built-in templating engine (Jinja2) to generate the HTML that will be sent to the client.

about: This function handles the HTTP GET request for the about page of your application. It might also fetch some data from the database and pass it to the template that will be rendered by Flask's built-in templating engine (Jinja2) to generate the HTML that will be sent to the client.

contact: This function handles the HTTP GET request for the contact page of your application. It might render a static HTML page, or it might render a form that the user can fill out to send an email or message to the site owner.

create_post: This function handles the HTTP GET and POST requests for creating a new blog post. If the request is a GET request, it might render a form for the user to fill out. If the request is a POST request, it might validate the form data, save the new blog post to the database, and redirect the user to the newly created post.

view_post: This function handles the HTTP GET request for viewing a single blog post. It fetches the post data from the database and passes it to the template that will be rendered by Flask's built-in templating engine (Jinja2) to generate the HTML that will be sent to the client.

update_post: This function handles the HTTP GET and POST requests for updating an existing blog post. If the request is a GET request, it might render a form pre-populated with the current post data. If the request is a POST request, it might validate the form data, update the existing post in the database, and redirect the user back to the updated post.

delete_post: This function handles the HTTP POST request for deleting an existing blog post. It deletes the post from the database and redirects the user back to the homepage or a confirmation page.

All of these functions (with the exception of contact) require the user to be authenticated. This is achieved using Flask-Login, which requires the user to log in before they can access any of the protected routes. If the user is not logged in, they will be redirected to the login page.

### auth.py:

The auth.py file is responsible for managing user authentication and authorization in the PreciousPals app.

It defines a blueprint named auth and registers it with the Flask app in the create_app function in app.py. This blueprint defines several routes for user authentication, including login, logout, and signup.

The auth blueprint imports the User model from models.py to manage user data. It also uses the bcrypt library to hash user passwords for security.

The login route (/login) uses the LoginForm class defined in forms.py to create a form for users to enter their login credentials. If the user successfully logs in, they are redirected to the home page (/).

The logout route (/logout) logs the user out by removing their session data and redirecting them to the login page (/login).

The signup route (/signup) uses the SignupForm class defined in forms.py to create a form for users to enter their registration information. If the user successfully registers, they are automatically logged in and redirected to the home page (/).

### Templates:

The following templates are used in the PreciousPals app:

#### base.html
This template serves as the base for all other templates and includes the header and footer of the website. It defines the basic HTML structure and includes static files such as CSS and JavaScript.

#### home.html
This template displays the home page of the website, which includes a welcome message and a list of recently added friends.

#### login.html
This template displays the login form and allows users to log in to their account.

#### register.html
This template displays the registration form and allows new users to create an account.

#### profile.html
This template displays the profile page of a user and includes information such as their name, email address, and a list of their friends.

#### add_friend.html
This template displays the form to add a new friend to a user's profile.

#### edit_friend.html
This template displays the form to edit an existing friend's information.

#### delete_friend.html
This template displays a confirmation message when a user attempts to delete a friend from their profile.

#### error.html
This template displays an error message when a user encounters an error while using the website.

Each of these templates extends the base.html template and includes its own content in the body of the page. The templates are rendered dynamically using data from the Flask app and are designed to provide a clean and user-friendly interface for the website.

### Design Choices:

One design choice I made was to use Flask-Login to handle user authentication instead of writing my own authentication code. While it would have been possible to implement my own authentication code, using Flask-Login allowed me to take advantage of its built-in features such as session management and password hashing. Additionally, it helped ensure that the authentication code was secure and free of common vulnerabilities such as SQL injection and cross-site scripting attacks.

Another design choice I made was to use SQLite as the database for this application instead of a more scalable database such as PostgreSQL. The reason for this choice was that the application was intended to be a small-scale project, and SQLite is a lightweight and easy-to-use database that is well-suited for such applications. Additionally, SQLite does not require a separate database server, making it easier to set up and deploy.

A third design choice I made was to use Flask Blueprints to organize the code for this application into separate modules. By using Blueprints, I was able to keep related code organized in separate files, making it easier to navigate and maintain the codebase. Additionally, Blueprints allowed me to easily add new features to the application without having to modify the main Flask application instance.

Another design choice that I debated was the use of HTML templates for the front-end. While it provided an easy way to create consistent and visually appealing web pages, it also added extra overhead to the application, since the server has to render the template for every request. However, I ultimately decided that the benefits of using templates outweighed the costs, since it allowed me to separate the logic from the presentation and make it easier to maintain and update the code in the future. It also allowed me to reuse the same templates for different pages, which saved time and effort.
