from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True
 
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pongHello!')


 
# @app.route('/members', methods=['GET'])
# def all_members():
#     return jsonify({
#         'status': 'success',
#         'members': MEMBERS
#     })
 
if __name__ == '__main__':
    app.run()