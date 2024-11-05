0x02. i18n
Description
This project focuses on internationalization (i18n) using Flask and Flask-Babel. It involves setting up a Flask application that supports multiple languages, determining the correct locale based on various factors, and localizing timestamps. This enhances the usability of the application for users from different linguistic and cultural backgrounds.

Learning Objectives
Learn how to parameterize Flask templates to display different languages.

Learn how to infer the correct locale based on URL parameters, user settings, or request headers.

Learn how to localize timestamps.

Requirements
All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).

All files should end with a new line.

A README.md file at the root of the project folder is mandatory.

Code should use the pycodestyle style (version 2.5).

The first line of all Python files should be #!/usr/bin/env python3.

All Python files should be executable.

All modules should have a documentation string.

All classes should have a documentation string.

All functions and methods should have a documentation string.

All functions and coroutines must be type-annotated.

Table of Contents
Tasks

Installation

Usage

Contributing

License

Tasks
Task 0: Basic Flask app
Set up a basic Flask app in 0-app.py. Create a single / route and an index.html template that outputs "Welcome to Holberton" as the page title and "Hello world" as the header.

Task 1: Basic Babel setup
Install the Babel Flask extension and instantiate the Babel object in your app. Create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"]. Set Babel’s default locale to "en" and timezone to "UTC". Use this class as config for your Flask app.

Task 2: Get locale from request
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with the supported languages.

Task 3: Parametrize templates
Use the _ or gettext function to parametrize your templates. Create a babel.cfg file, initialize translations, and compile your dictionaries.

Task 4: Force locale with URL parameter
Implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs. Modify the get_locale function to detect this parameter.

Task 5: Mock logging in
Create a mock user table and a get_user function. Define a before_request function that uses get_user to find a user and set it as a global variable. Update your HTML template to display a welcome message if a user is logged in.

Task 6: Use user locale
Modify the get_locale function to use a user’s preferred locale if it is supported. The order of priority should be:

Locale from URL parameters

Locale from user settings

Locale from request header

Default locale

Task 7: Infer appropriate time zone
Define a get_timezone function with the babel.timezoneselector decorator. Implement logic to determine the time zone from URL parameters, user settings, or default to UTC.

Contributing
Contributions are welcome!
