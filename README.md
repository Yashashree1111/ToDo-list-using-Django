Django Task Manager
This is a simple Django application for managing tasks. It provides a list of tasks for each day of the week and allows navigation to specific tasks using both the day name and a number.

Features
List all tasks for the week
View tasks for a specific day
Redirect to tasks using a numeric index
Project Structure
The project consists of the following views:

index: Displays the list of all tasks for the week.
challenges: Displays the task for a specific day.
numberchallenge: Redirects to the task for a specific day using a numeric index.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Yashashree1111/python-Django-projects.git
Navigate to the project directory:

bash
Copy code
cd python-Django-projects/demoblog
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the Django development server:

bash
Copy code
python manage.py runserver
Usage
View all tasks:
Navigate to the root URL to see the list of all tasks for the week.

View task for a specific day:
Navigate to /challenges/<day>/ where <day> is the name of the day (e.g., monday, tuesday, etc.).

Redirect to a task using a number:
Navigate to /numberchallenge/<num>/ where <num> is the index of the day (e.g., 1 for Monday, 2 for Tuesday, etc.).
