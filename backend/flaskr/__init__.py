import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db,Question,Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = page - 1
  end = start + QUESTIONS_PER_PAGE
  categories = [category.format() for category in selection]
  current_questions = categories[start:end]
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"/api/*": {"origins": "*"}})



  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH,OPTIONS')
    return response

  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    if categories is None:
      abort(404)
    formatted_categories = [category.format() for category in categories]
    return jsonify({
      'success':True,
      'categories':formatted_categories
    })



  @app.route('/questions')
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'current_category': None,
      'categories': formatted_categories


    })



  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.filter(Question.id == question_id).one_or_none()
    if question is None:
      abort(404)
    try:
      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })
    except:
      abort(422)


  @app.route('/questions', methods=['POST'])
  def create_question():
    data = request.get_json(force=True)

    new_question = data.get('question', None)
    new_answer = data.get('answer', None)
    new_category = data.get('category', None)
    new_difficulty = data.get('difficulty', None)
    if new_question is None or new_answer is None or new_category is None or new_difficulty is None:
      abort(422)
    try:
      question = Question(question=new_question, answer=new_answer, category=new_category,difficulty=new_difficulty)
      question.insert()
      selecion = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selecion)
      return jsonify({
        'success': True,
        'created': question.id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })
    except:
      abort(422)


  @app.route('/questions/search', methods=['POST'])
  def search_question():
    body = request.get_json(force=True)
    search = body.get('searchTerm',None)
    selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)
    try:

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(selection.all())
      })
    except:
      abort(422)


  @app.route('/categories/<int:category_id>/questions')
  def get_question_with_categoryID(category_id):
    category = Category.query.get(category_id)

    if category is None:
      abort(404)

    questions = Question.query.filter_by(category=category_id).all()
    current_questions = paginate_questions(request, questions)
    if len(current_questions) == 0:
      abort(404)

    return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'current_category':category.type
    })



  @app.route('/quizzes',methods=['POST'])
  def create_quiz():
    body = request.get_json()
    quiz_category = body.get('quiz_category',None)
    previous_questions = body.get('previous_questions',None)

    if (quiz_category is None):
      abort(404)


    if quiz_category['id'] == 0:
      questions = Question.query.all()
    else:
      questions = Question.query.filter_by(category=quiz_category['id']).all()

    def generate_random_questions():
      return questions[random.randint(0, len(questions) - 1)]

    current_questions = generate_random_questions()
    exist = True
    while exist:
      if current_questions.id in previous_questions:
        current_questions = generate_random_questions()
      else:
        exist = False

    return jsonify({
      'success': True,
      'question': current_questions.format()

    })


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422
  return app

    