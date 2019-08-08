# TO-DO List App
---
### This is a simple ToDo List app in which task can be created, edited, deleted and viewed through simple User Interface.

To Get start with the app:

1. Download/Clone the app in your system.

2. Requirements: \
   Python (3 and above)\
   Virtualenv \
   Django(2.2) 

3. Setup the virtualenv for the project.

4. Configure migration file for the project: \
   python manage.py makemigrations \
   python manage.py migrate 

5. Create a superuser to access admin interface: \
   python manage.py createsuperuser \
   **(give username and password)** 

6. Run the server: \
   Python manage.py runserver 

   **Copy the server url (http://127.0.0.1:8000) and open in your browser** 

7. Following are the urls to access the app: \
   http://127.0.0.1:8000/                  **To view the main page** \
   http://127.0.0.1:8000/admin             **To access admin interface** \
   http://127.0.0.1:8000/add               **To add new task to the list** \
   http://127.0.0.1:8000/<task_title>      **To view the single task, edit and delete the task** 

   http://127.0.0.1:8000/api               **API to view all the list** \
   http://127.0.0.1:8000/api/<task_title>  **API to view specific task** 
