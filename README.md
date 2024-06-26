# Costly Expenses App

![Money Image](static/images/readme-imgs/money.png)

Link to the deployed project: https://costly-413690edf851.herokuapp.com/

# Purpose of this project

The Costly app is here to let a user better organize, display, edit and delete their expenses. By simply clicking on 'Add Expense' and filling out the simple form the user can add their costs to a list. They can also edit these expenses or delete them. Additionally the user gets informed about their total cost of all the expenses.

# Table of contents

* [User demographic](<https://github.com/Tekali7/Costly#user-demographic>)
  * [User experience](<https://github.com/Tekali7/Costly#user-experience>)
* [Agile methodology](<https://github.com/Tekali7/Costly#agile-methodology>)
  * [Epics and user stories](<https://github.com/Tekali7/Costly#epics-and-user-stories>)
  * [User Authentication and Authorization](<https://github.com/Tekali7/Costly#user-authentication-and-authorization>)
  * [Expense Management and Validation](<https://github.com/Tekali7/Costly#expense-management-and-validation>)
  * [User Interface, Experience and Feedback](<https://github.com/Tekali7/Costly#user-interface-experience-and-feedback>)
* [Features](<https://github.com/Tekali7/Costly#features>)
  * [Add expenses](<https://github.com/Tekali7/Costly#add-expenses>)
  * [Edit expenses](<https://github.com/Tekali7/Costly#edit-expenses>)
  * [Delete expenses](<https://github.com/Tekali7/Costly#delete-expenses>)
  * [Total cost overview](<https://github.com/Tekali7/Costly#total-cost-overview>)
  * [User-Friendly Interface](<https://github.com/Tekali7/Costly#user-friendly-interface>)
  * [Secure authentication](<https://github.com/Tekali7/Costly#secure-authentication>)
  * [Future features](<https://github.com/Tekali7/Costly#future-features>)
  * [Bug Fixes](<https://github.com/Tekali7/Costly#bug-fixes>)
* [Design](<https://github.com/Tekali7/Costly#design>)
  * [Color](<https://github.com/Tekali7/Costly#color>)
  * [Typography](<https://github.com/Tekali7/Costly#typography>)
* [Wireframes](<https://github.com/Tekali7/Costly#wireframes>)
  * [Entity relationship diagram](<https://github.com/Tekali7/Costly#entity-relationship-diagram>)
  * [User interface](<https://github.com/Tekali7/Costly#user-interface>)
* [Technology](<https://github.com/Tekali7/Costly#technology>)
  * [Languages](<https://github.com/Tekali7/Costly#languages>)
  * [Django Packages](<https://github.com/Tekali7/Costly#django-packages>)
  * [Frameworks - Libraries - Programs Used](<https://github.com/Tekali7/Costly#frameworks---libraries---programs-used>)
* [Testing](<https://github.com/Tekali7/Costly#testing>)
* [Project Creation](<https://github.com/Tekali7/Costly#project-creation>)
  * [Creating the Django app](<https://github.com/Tekali7/Costly#creating-the-django-app>)
  * [Deployment of This Project](<https://github.com/Tekali7/Costly#deployment-of-this-project>)
  * [Final Deployment](<https://github.com/Tekali7/Costly#final-deployment>)
  * [Forking This Project](<https://github.com/Tekali7/Costly#forking-this-project>)
  * [Cloning This Project](<https://github.com/Tekali7/Costly#cloning-this-project>)
* [Credits](<https://github.com/Tekali7/Costly#credits>)

# User demographic

The user demographic for an expense tracking app typically includes people from many age groups, families managing household finances, and small business owners tracking business expenses. These users look for ways to gain better control over their finances, track spending habits, and achieve their financial goals.

# User experience
As a user, I want to be able to:
- Securely log in to my account using authentication credentials.
- Access and view my own expenses.
- Add new expenses.
- Edit or update details of my existing expenses.
- Ensure that my financial data remains private and secure.

# Agile methodology

Throughout this project, an Agile approach was taken in order to develop the app. Each of the three Epics were broken down into smaller User Stories, which were then refined into more manageable Tasks. Each of the User Stories has different acceptance criteria. The User Stories can be found in the kanban board linked [here](<https://github.com/users/Tekali7/projects/3/views/1>). This made the overall project much more manageable to build.

## Epics and user stories
Epics which I came up with for the app before the start of the project, which were then rewritten to fit the app in a more tailored way.

### User Authentication and Authorization
To ensure the security and privacy of user data within the expense tracking app, implementing robust user authentication and authorization mechanisms is essential.
This epic focuses on providing users with secure access to their accounts while restricting access to unauthorized users. By implementing user authentication, users can securely log in to their accounts using unique credentials, such as usernames and passwords. Additionally, user authorization ensures that authenticated users have appropriate permissions to access specific features and data within the app. This epic should show the need for a secure way in and out of the app.
- [User Story #10 Authorization](<https://github.com/Tekali7/Costly/issues/10>)

### Expense Management and Validation
 Effective management and validation of expenses are crucial aspects of the app which ensure the accuracy and reliability of financial data. This epic focuses on providing users with comprehensive tools for managing their expenses, including adding, editing, and deleting expenses. Additionally, the app also needs validation mechanisms to verify the expense data entered by users. By enabling users to track expenses accurately and reliably, this epic aims to empower users to make informed financial decisions and achieve their financial goals effectively.
- [User Story #1 Track Expenses](<https://github.com/Tekali7/Costly/issues/1>)
- [User Story #2 Edit expenses](<https://github.com/Tekali7/Costly/issues/2>)
- [User Story #4 Validate expenses](<https://github.com/Tekali7/Costly/issues/4>)
- [User Story #5 Total amount of costs](<https://github.com/Tekali7/Costly/issues/5>)
- [User Story #8 Saving expenses for each user](<https://github.com/Tekali7/Costly/issues/8>)
- [User Story #3 Delete expenses](<https://github.com/Tekali7/Costly/issues/3>)
- [User Story #6 Expense currency](<https://github.com/Tekali7/Costly/issues/6>)

### User Interface, Experience and Feedback
This epic emphasizes optimizing the UI of the app. It involves the users need for a clean and easy to navigate page. Additionally, the epic focuses on implementing feedback features such as messages when the user adds, edits or deletes an expense. The user should also get a deletion modal upon clicking the delete button, which asks the user to confirm the deletion of an expense. By prioritizing UI enhancements and feedback, this epic aims to raise user satisfaction, and overall app usability.
- [User Story #7 Friendly UI](<https://github.com/Tekali7/Costly/issues/7>)
- [User Story #9 User feedback](<https://github.com/Tekali7/Costly/issues/9>)

# Features
The app consists of one main page with many features for the user.

## Add expenses
Adds a new expense to the list of expenses including the amount and currency.
![Add expense](static/images/readme-imgs/add-expense.PNG)

## Edit expenses
Edit an existing expense either the expense name, amount or currency.
![Edit expense](static/images/readme-imgs/edit-expense.PNG)

## Delete expenses
Delete an expense, the user is asked to confirm on a modal before deletion.
![Delete expense](static/images/readme-imgs/delete-expense.PNG)

## Total cost overview
The total amount of all the expenses is displayed on the bottom of the list for transparency.
![Total cost](static/images/readme-imgs/total-cost.PNG)

## User-Friendly Interface
The UI is user-friendly, simple and therefore easy to navigate.
![User Interface](static/images/readme-imgs/user-interface.PNG)

## Secure authentication
Robust authentication measures were taken place to safely store each users private data.
Every user needs to authenticate themselves before accessing the features and data.
The authentication features include Sign In, Sign up and Sign out.
### Sign In
![Sign In](static/images/readme-imgs/sign-in.PNG)
### Sign Up
![Sign Up](static/images/readme-imgs/sign-up.PNG)
### Sign Out
![Sign Out](static/images/readme-imgs/sign-out.PNG)

## Future features

Future features might include.

- Total cost that calculates all currencies together with consideration of their current exchange rates.

- Analytics that analyze a users spending habits over time to let them know where they could improve.

- Reminders for open payments or upcoming bills.

## Bug Fixes
- Bug: Two different users can't name their items the same.

  - Working solution: Remove 'unique=True' from the item field in the Model.

- Bug: User can't add an expense.
  - Working solution: Clean up forms file and add widgets.

Currently theres a bug where a white bar with a slash appears on top of the page.
I couldn't find the error for this just yet.

# Design
## Color
![Color](static/images/readme-imgs/color.PNG)
![Contrast](static/images/readme-imgs/contrast.PNG)

The app adopts a dark color scheme to provide contrast and ensure visibility against the background. This choice helps users quickly locate features and enhances overall usability.

## Typography
The app name stands out with a simple serif font in the navbar, and the 'page/form titles' stand out with 'Franklin Gothic Medium'.
Other than that the default font has been left.

# Wireframes
## Entity relationship diagram
![ERD](static/images/readme-imgs/erd.PNG)

## User interface
![UI](static/images/readme-imgs/wireframe.PNG)

# Technology

## Languages

- HTML 5
- CSS 3
- JavaScript
- Django
- Python

## Django Packages

- Gunicorn: As the server for Heroku

- Dj_database_url: To parse the database URL from the environment variables in Heroku

- Psycopg2: As an adaptor for Python and DB

- Allauth: For authentication, registration and account management

- Crispy Forms: To style the forms

## Frameworks - Libraries - Programs Used

- Bootstrap: Was used to style the app

- Jquery: All the scripts were written using jquery library

- Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub

- GitHub: GitHub is used to store the project's code after being pushed from Git

- Heroku: Heroku was used to deploy the live project

- PostgreSQL: With ElephantSQL through Heroku

- Gitpod: Gitpod was used to create and edit the app

- Lucidchart: Lucidchart was used to create the database diagram

- PEP8: PEP8 was used to validate all the Python code

- W3C - HTML: W3C- HTML was used to validate all the HTML code

- W3C - CSS: W3C - CSS was used to validate the CSS code

- Google Chrome Dev Tools: To check App responsiveness and debugging

# Testing
The tests can be found [here](<https://github.com/Tekali7/Costly/blob/main/TESTS.md>)

# Project Creation
## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or click Manual Deploys

## Final Deployment 

1. Create a runtime.txt `python-3.12.3`
2. Create a Procfile `web: gunicorn your_project_name.wsgi`
3. When development is complete change the debug setting to: `DEBUG = False` in settings.py
4. If you use the summernote editor add this for it to work on Heroku: `X_FRAME_OPTIONS = SAMEORIGIN ` to settings.py.
5. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/Tekali7/Costly)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/Tekali7/Costly)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

# Credits

- The delete confirmation modal was adapted from the walkthrough project.
- The HTML for displaying Django messages was adapted from the walkthrough project.
- The 10 lines in the base template's main section were adapted from the walkthrough project.
- The header in the base template was adapted from the walkthrough project.

- I found a lot of information about Django's urls, forms, models etc on the [Django Documentation](<https://docs.djangoproject.com/en/5.0/>).
- My Mentor Brian Macharia taught me about aggregation, styling and authentication.

- The remainder of the code was written by me with the help from the mentioned Documentation and also [Stackoverflow](<https://stackoverflow.com/>) to solve problems.