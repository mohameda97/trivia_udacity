# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## API Documentation 

In this workspace, your task is to practice writing documentation for the bookstore app we created earlier.

You'll soon be writing documentation for your final project (the Trivia API), after which you'll get feedback from a reviewer. You can think of this as some rudimentary practice to prepare for that.

At each step, you can compare what you've written with our own version. Of course, there isn't a single correct way to write a piece of documentation, so your version may look quite different. However, there are principles and practices you should follow in order to produce quality documentation, and we'll point this out so you can check whether you've incorporated them in what you wrote.

To get started, go ahead and move to the next page in this workspace

## Getting Started

* Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
* Authentication: This version of the application does not require authentication or API keys.


# Error Handling
Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 404,
    "message": "not found"
}
```
The API will return three error types when requests fail:

* 404: Resource Not Found
* 422: Not Processable
# Endpoints
#### GET/categories
###### General 
return a list from all categories
###### Sample
from postman write http://127.0.0.1:5000/categories and select GET method

```
"categories": [
    {
      "id": 1,
      "type": 'History',
    }],
      "success": True,
      "total_books": 1
    }
```
#### GET/questions
###### General 
return a list from all questions
###### Sample
from postman write http://127.0.0.1:5000/questions and select GET method
```
"questions": [
    {
      'id': 1,
      'question': 'What is your name',
      'answer': 'Mohamed',
      'category': 'History',
      'difficulty': 5
    }],
      'success': True,
      'questions': [{
              'question': 'What is your name',
              'answer': 'Mohamed',
              'category': 'History',
              'difficulty': 5
            }],
      'total_questions': 1,
      'current_category': None,
      'categories': [{"type": 'History'}]
    }
```
#### DELETE/questions
###### General 
delete question with given id
###### Sample
from postman write http://127.0.0.1:5000/questions/5 and select DELETE method
```
"questions": [
    {
        'success': True,
        'deleted': 5,
        'questions': 'id': 1,
              'question': 'What is your name',
              'answer': 'Mohamed',
              'category': 'History',
              'difficulty': 5
            }],
        'total_questions': 1
    }
```
#### POST/questions
###### General 
create question 
###### Sample
from postman write http://127.0.0.1:5000/questions and select POST method
```
    {
        'question': 'What is your name',
        'answer': 'Mohamed',
        'category': 'History',
        'difficulty': 5
    }
           
        'success': True,
        'created':2,
        'questions':[ 
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5},
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5}
                    ]
        'total_questions': 2
    }
```
#### POST/searchQuestions
###### General 
search for a question 
###### Sample
from postman write http://127.0.0.1:5000/questions/search and select POST method
```
    {
        'searchTerm': 'What is your name'
    }
           
        'success': True,
        'questions':[ 
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5},
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5}
                    ]
        'total_questions': 2
    }
```
#### GET/questions by category ID
###### General 
get all questions for specific category
###### Sample
from postman write http://127.0.0.1:5000/categories/1/questions and select GET method
```
   {
        'success': True,
        'questions': [ 
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5},
                        {'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5}
                    ],
        'total_questions':2,
        'current_category':'History'
    }
```
#### POST/quizzes
###### General 
create random questions for new quiz
###### Sample
from postman write http://127.0.0.1:5000/quizzes and select POST method
```
   {
      'success': True,
      'question':{'id':1,'question': 'What is your name','answer': 'Mohamed','category': 'History','difficulty': 5}

   }
```
