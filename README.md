# Django Task Manager
 This is a simple Django application for managing tasks. It provides a list of tasks for each day of the week and allows navigation to specific tasks using both the day name and a number.

## Features
 List all tasks for the week
 View tasks for a specific day
 Redirect to tasks using a numeric index

## Project Structure
 The project consists of the following views:

 index: Displays the list of all tasks for the week.
 challenges: Displays the task for a specific day.
 numberchallenge: Redirects to the task for a specific day using a numeric index.
 
## Installation
 Clone the repository:

  git clone https://github.com/Yashashree1111/python-Django-projects.git
 
 Create a virtual environment and activate it:

 python -m venv venv
 source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

 
 Run the Django development server:
 python manage.py runserver
 
 ## Usage
 View all tasks:
 Navigate to the root URL to see the list of all tasks for the week.

 View task for a specific day:
 Navigate to /challenges/<day>/ where <day> is the name of the day (e.g., monday, tuesday, etc.).

 Redirect to a task using a number:
 Navigate to /numberchallenge/<num>/ where <num> is the index of the day (e.g., 1 for Monday, 2 for Tuesday, etc.).

 ![image](https://github.com/Yashashree1111/ToDo-list-using-Django/assets/106982749/e305a85e-009a-44b7-adf6-3a6c5d4dd6ab)

 ![image](https://github.com/Yashashree1111/ToDo-list-using-Django/assets/106982749/af3221b7-07eb-4107-8648-deac1c0944b5)


