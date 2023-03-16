from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/main')
def splash():
  return render_template('index.html', appname='footyhub')

# @app.before_request
# def before_request_function():
#   print('before request function running')


# @app.after_request
# def after_request_function(response):
#     print("after_request is running")
#     return response


# @app.route('/help')
# def help():
#   return '<h1>Help page</h1>'

# @app.route('/about')
# def about():
#   return '<h1>About</h1><p>My name is Will Corona. I am an App Academy graduate who is passionate about soccer and coding. I wanted to build an app to create easy access to find all of the latest news, scores, and updates for football/soccer all over the world</p>'

# @app.route('/item/<int:id>')
# def item(id):
#   if 0 < id and id < 100:
#     return f'''<h1>Item Number <h2>{id}</h2></h1>'''
#   else:
#     return '<h1>Item Not Found</h1>'