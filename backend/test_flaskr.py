import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('postgres:root@localhost', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {'question': 'What is your name?', 'answer': 'Mohamed','category': 1,'difficulty': 3,}
        self.new_quiz = {
            'previous_questions': [1],
            'quiz_category': {
                'id':1,
            }
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_get_categories_failures(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), 10)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])


    def test_questions_not_found(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')



    def test_delete_question(self):
        res = self.client().delete('/questions/6')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_failed_to_delete_question(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'resource not found')

    def test_create_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_failed_to_create_question(self):
        res = self.client().post('/questions',json= {
            'question': '',
            'answer': '',
            'difficulty': '',
            'category': '',
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')

    def test_search_question(self):
        res = self.client().post('/questions/search',json={'searchTerm':'What'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_fail_search_question(self):
        res = self.client().post('/questions/search',json={'searchTerm':'fasjbfcjhsdvbjhdsvbj'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def get_paginated_questions_by_category(self):
        res = self.client().get('/categories/1/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_failed_to_get_question_by_category(self):
        res = self.client().get('/categories/1/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_quiz(self):
        res = self.client().post('/quizzes',json=self.new_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['question']))

    def test_failed_to_create_quiz(self):
        res = self.client().post('/quizzes',json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_failed_create_due_number_of_questions(self):
        res = self.client().post('/quizzes',json={
            'previous_questions': [1],
            'quiz_category': {
                'id':3,
            }})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()