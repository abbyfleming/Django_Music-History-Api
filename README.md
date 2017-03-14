# Muisc History API

### Initial Setup
* Install [Python 3.6](http://https://www.python.org/downloads/release/python-360/)
* Install [Pip](https://pip.pypa.io/en/stable/installing/)


### Getting Started

Using your terminal:

* ```pip install django```
* ```pip install djangorestframework``` 

After installing django and djangorestframework, clone the repo locally to your computer.


### Sync the Database

In the main project directory, run:

```python manage.py migrate```


### Start with Sample Data

In the main project directory, run:
```python manage.py loaddata musichistory_initial_data.json```


### Run the Server

```python manage.py runserver```

Check to see where the server is running. 
(Example: Development server is running at http://127.0.0.1:8000/)

On your browser, go to your local host
(Example: http://localhost:8000/)
