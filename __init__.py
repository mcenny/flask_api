from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD!'})

    @app.route('/smiley')
    def smiley():
        return ':)'

    @app.route('/cost')
    def cost():
        return jsonify({'cost':2500, 'name': 'fried rice', 'quantity': '1 plate'})

    return app