from flask import Flask
from api import create_app
from waitress import serve
from paste.translogger import TransLogger
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


app = create_app()

if __name__ == '__main__':
    # app.run(debug=True, port=3000)
    # serve(app, host='127.0.0.1', port=8080)
    serve(TransLogger(app, setup_console_handler=False), host='127.0.0.1')