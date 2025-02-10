# djangoBlog

Started: 02/09/2025

# Technology Stack
- Python
- Django
- Sqlite3
- HTML
- CSS/BootStrap
- Hosted on PythonAnywhere
  - [Blog Webpage](https://awesomly.pythonanywhere.com)

# Verify the necessary libraries are installed (Windows)
1. Verify python is installed (3.10.11+)
2. Create Virtual Environment
    1. python3 -m venv (NAME OF VENV i.e. **myvenv**)
3. Run the command 
    1. **myvenv\Scripts\activate**
4. Verify pip is installed **python -m pip install --upgrade pip**
5. Create **requirements.txt** with the following text: **Django~=5.1.2**
6. Run **pip install -r requirements.txt**

# How to Run Applicaiton
1. Be in root directory and in virtual environment
2. Run **python manage.py runserver**
3. Visit **localhost:8000** or **localhost:8000/admin**. 
4. Login via **http://localhost:8000/admin/** or **https://awesomly.pythonanywhere.com/admin/**

# Credit to djangogirls
- [Django Tutorial](https://tutorial.djangogirls.org/en/)