from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/main')
def splash():
  return render_template('index.html', appname='footyhub')


@app.route('/item/<int:id>')
def item(id):
  if 0 < id and id < 100:
    item = {
      "id": id,
      'name': f'fancy item {id}',
      'description': 'Coming soon!'
    }
    return render_template('item.html', item=item)
  else:
    return '<h1>Item Not Found</h1>'


@app.route('/help')
def help():
  return '<h1></h1>'


@app.route('/login')
def login():
  return render_template('login.html')


# @app.before_request
# def before_request_function():
#   print('before request function running')


# @app.after_request
# def after_request_function(response):
#     print("after_request is running")
#     return response


# @app.route('/about')
# def about():
#   return '<h1>About</h1><p>My name is Will Corona. I am an App Academy graduate who is passionate about soccer and coding. I wanted to build an app to create easy access to find all of the latest news, scores, and updates for football/soccer all over the world</p>'
