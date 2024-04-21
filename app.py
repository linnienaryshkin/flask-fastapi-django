from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request

# https://flask.palletsprojects.com/en/3.0.x/quickstart/#context-locals
app = Flask(__name__)

"""
curl http://127.0.0.1:5000/
"""
@app.route('/')
def index():
    return 'Index Page'

"""
curl http://127.0.0.1:5000/var/ASD
"""
@app.route("/user/<username>")
def user(username):
    return f"Hello, {escape(username)}!"

"""
curl http://127.0.0.1:5000/post/12
"""
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

"""
curl http://127.0.0.1:5000/html/World
"""
@app.route('/html/')
@app.route('/html/<name>')
def html(name=None):
    return render_template('hello.html', name=name)

"""
curl http://127.0.0.1:5000/json
"""
@app.route("/json")
def json():
    # https://docs.python.org/3/library/logging.html#logging.Logger
    app.logger.info('We are in the /json route')
    return {
        "username": 'username',
        "theme": 'theme',
    }

# https://www.geeksforgeeks.org/with-statement-in-python/
with app.test_request_context():
    print(url_for('index'))
    print(url_for('user', username='John Doe'))
    print(url_for('show_post', post_id=1))
    print(url_for('static', filename='test-static'))
    print(url_for('html', name='World'))
    print(url_for('json'))

with app.test_request_context('/', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/'
    assert request.method == 'GET'

with app.test_request_context('/user/John', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/user/John'
    assert request.method == 'GET'