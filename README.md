# To-do-list

This project provides a simple to-do list of user's tasks. It includes account creation, password change, password reset, and basic CRUD operations for tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- **Account creation and management:** Create your account, change password, or generate a new one if needed.
- **Task-related CRUD operations:** Manage your task list as you see fit.
- **Restricted view:** You need to be logged in to see your tasks - each user may only see their own tasks.

## Requirements

- Python 3.x  
- [asgiref](https://pypi.org/project/asgiref/) == 3.8.1  
- [black](https://pypi.org/project/black/) == 25.1.0  
- [click](https://pypi.org/project/click/) == 8.1.8  
- [colorama](https://pypi.org/project/colorama/) == 0.4.6  
- [Django](https://pypi.org/project/Django/) == 5.0.13  
- [mypy-extensions](https://pypi.org/project/mypy-extensions/) == 1.0.0  
- [packaging](https://pypi.org/project/packaging/) == 24.2  
- [pathspec](https://pypi.org/project/pathspec/) == 0.12.1  
- [platformdirs](https://pypi.org/project/platformdirs/) == 4.3.7  
- [sqlparse](https://pypi.org/project/sqlparse/) == 0.5.3  
- [tzdata](https://pypi.org/project/tzdata/) == 2025.1  

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MaciejPJ/To-do-list
2. **Create and activate a virtual environment - optional but recommended**
   ```bash
   python -m venv .venv
   venv\Scripts\activate
   ```
3. **Install the required libraries (requirements.txt)**
   ```bash
   pip install -r requirements.txt
4. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Usage

Open the application in browswer using the following address: http://127.0.0.1:8000/

Once launched, the application window will allow you to log in, create new account or reset the password. After that you may see your tasks and perform CRUD operations on them.

## Project structure

- **requirements.txt** – Contains list of required packages.
- **django_project/** – Main project configuration folder.
  - **settings.py** – Main settings of the project (Time zone, E-mail backend, installed apps, etc.).
- **accounts/** – app related to accounts with tests.
- **pages/** - app defining the view logic of homepage.
- **static/** - stores CSS styles.css.
- **tasks/** - app containing logic for managing task.
- **templates/** - stores all HTML templates used across the project
  - **registration/** - stores all templates related to login, password change and reset.


