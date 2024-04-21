from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from typing import Optional, TypedDict
from datetime import datetime

# https://flask.palletsprojects.com/en/3.0.x/quickstart/#context-locals
app = Flask(__name__)

"""
curl http://127.0.0.1:5000/
"""
@app.route('/')
def index():
    return 'Index Page'
with app.test_request_context('/', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/'
    assert request.method == 'GET'

"""
curl http://127.0.0.1:5000/var/ASD
"""
@app.route("/user/<username>")
def user(username: str): # type hinting | https://docs.python.org/3/library/typing.html
    return f"Hello, {escape(username)}!"
with app.test_request_context('/user/John', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/user/John'
    assert request.method == 'GET'

"""
curl http://127.0.0.1:5000/post/12
"""
@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    # show the post with the given id, the id is an integer
    return f'Post {post_id + 1}'

"""
curl http://127.0.0.1:5000/html/World
"""
@app.route('/html/')
@app.route('/html/<name>')
def html(name=None):
    return render_template('hello.html', name=name)

# https://www.geeksforgeeks.org/with-statement-in-python/
with app.test_request_context():
    print(url_for('index'))
    print(url_for('user', username='John Doe'))
    print(url_for('show_post', post_id=1))
    print(url_for('static', filename='test-static'))
    print(url_for('html', name='World'))

"""
curl http://127.0.0.1:5000/json
"""
@app.route("/json")
def json():
    # https://docs.python.org/3/library/logging.html#logging.Logger
    app.logger.info('We are in the /json route')
    return get_json(request.args.get('name'))

# TODO: Understand how type checking works | https://docs.python.org/3/library/typing.html#typing.TypedDict
class Profile(TypedDict):
    name: Optional[str]
    age: int
    city: str

# TODO: use `str | None` instead of `Optional[str] = None` | https://fastapi.tiangolo.com/python-types/#using-union-or-optional
def get_json(name: Optional[str] = None) -> Profile:
    return {
        "name": name,
        "age": 30,
        "city": "New York"
    }

with app.test_request_context('/json', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/json'
    assert request.method == 'GET'
    assert json() == dict(name=None, age=30, city='New York')
