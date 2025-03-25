
from flask import Flask, request
from markupsafe import escape
from werkzeug.exceptions import HTTPException



app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        ip_addr = request.remote_addr
        return f'<h1>Your IP address is: {escape(ip_addr)}</h1>'
    except Exception as e:
        return f'<h1>Error: Unable to get IP address</h1>', 500

@app.route('/client')
def client():
    try:
        ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.environ.get('REMOTE_ADDR'))
        return f'<h1>Your IP address is: {escape(ip_addr)}</h1>'
    except Exception as e:
        return f'<h1>Error: Unable to get IP address</h1>', 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    return f'<h1>Error: {e.code} - {e.name}</h1>', e.code

if __name__ == '__main__':
    app.run(debug=True)
