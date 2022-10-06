# final-project-iti
iti project
# ITI Final Project (Blogger)
<Add Project Description>

## Installation

1- Create a virtual environment using:

bash
py -m venv venv

or
bash
python -m venv venv

2- Activate the virtual environment:
bash
venv\Scripts\activate

3- Install requirements
bash
pipenv install -r requirements.txt

4- Add your MySQL database connection string:

   - Open blogger\settings.py
   - Change the DATABASES variable to apply to your database 
python
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : '<Database Name>',
        'USER'    : '<User Name>',
        'PASSWORD': '<User Password>',
        'HOST'    : 'localhost',
        'PORT'    : '3306',
    }
}

5- Make Migrations
bash
py manage.py makemigrations

6- Apply the migrations
bash
py manage.py migrate  

7- Create an Admin
bash
py manage.py createsuperuser

Username: Admin
Email address: Admin@Admin.com
Password: Admin
Password (again): Admin
Bypass password validation and create user anyway? [y/N]: y


8- Run the project
bash
py manage.py runserver


## Contributing

- Maha Esam AbdElRhman Mohamed
- Marina Soryal Frenses Soryal
- Nada Saad Ali Meleha
- Nada Said Younes
