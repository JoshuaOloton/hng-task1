from . import main
from flask import jsonify, request

@main.route('/')
def index():
    return 'Hello, World!'

@main.route('/hello')
def greeting():
    name = request.args.get('visitor_name')
    print(name)
    return jsonify({'client_ip': request.remote_addr, 'greeting': f'Hello, {name}!'})