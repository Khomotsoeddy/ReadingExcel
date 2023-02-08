# ReadingExcel

Problem and Solution
Problem: The user must enter the customer information such as first name, last name and date of birth, upload excel file contains income and expenses for past 12 months, customer information must be saved to database and visualize the excel data.
Solution: The solution to this problem is that I used HTML, SQLite, and Python programming language. HTML allow the user to enter the customer information, upload the excel files and visualize the results. SQLite is used to save the data. Python programming language create models using Django framework, receives data from HTML forms, reads the excel file using Pandas library and redirects the pages.
Number of users: 1


How to run the project

You can use VS Code 2022 or latest

1. cd to the directory where project is located.\
2. activate your virtualenv.\
3. run: pip install -r requirements.txt in your shell.\
4. run: python manage.py makemigrations\
5. run: python manage.py migrate\
6. run: python runserver\

make sure python and pip are install in your machine
