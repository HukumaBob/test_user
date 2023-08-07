# Test Task: Building a User Management System

Background:
Your company is developing a new web application that requires a user management system. The application will allow users to register, log in, view/update their profiles, and perform basic CRUD operations on user accounts. The frontend should be user-friendly and responsive, while the backend should be secure and efficient.

Task Overview:
Create a user management system as a web application. The application should consist of backend and adhere to industry best practices for security, performance, and code organization. You are free to use any programming languages, frameworks, and technologies you're comfortable with.

## Backend Requirements:

1. Design and implement RESTful API endpoints for user registration, login, fetching user profile, updating user profile, and deleting the account.
2. Implement secure password hashing and storage. Do not store plain passwords in the database.
3. Use appropriate validation and error handling techniques for API endpoints.
4. Store user data in a database of your choice.
5. Implement authentication and authorization mechanisms for protecting API routes.


## General Requirements:

1. Use version control (e.g., Git) for tracking changes to the codebase.
2. Implement clear and concise documentation for setting up and running the application.
3. Pay attention to code readability, organization, and best practices.
4. Ensure the application is deployable and provide instructions for deployment.
5. Consider performance optimizations where applicable.

## Installation Instructions
***- Clone the repository:***
```
git clone git@github.com:HukumaBob/test_user.git
```

***- Install and activate the virtual environment:***
- For MacOS/Linux
```
python3 -m venv venv
```
- For Windows
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```

***- Install dependencies from the requirements.txt file:***
```
pip install -r requirements.txt
```
***- Add .env***
```
copy .env.copy .env
```

***- Apply migrations in the folder with the manage.py file:***
```
python manage.py migrate
```
***- Create superuser:***
```
python manage.py createsuperuser
```

***- Start development server at http://127.0.0.1:8000/admin***

***- For API documentation goto http://127.0.0.1:8000/redoc or http://127.0.0.1:8000/swagger***


 