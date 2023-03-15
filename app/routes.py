from app import app

@app.before_request
def before_request_function():
  print('before request function running')


@app.after_request
def after_request_function(response):
    print("after_request is running")
    return response

@app.route('/')
@app.route('/splash')
def splash():
  return '<h1>Hello World. Sample App.</h1>'


@app.route('/about')
def about():
  return '<h1>About</h1><p>My name is Will Corona. I am an App Academy graduate who is passionate about soccer and coding. I wanted to build an app to create easy access to find all of the latest news, scores, and updates for football/soccer all over the world</p>'