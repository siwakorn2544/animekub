from flask import Flask, jsonify
from flask_cors import CORS
# from flask import request
import requests

# configuration
DEBUG = True
 
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

response = requests.get("https://api.jikan.moe/v4/anime/")
 
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/animekub', methods=['GET'])
def ping_pong():
    return jsonify(response.json())


 
# @app.route('/members', methods=['GET'])
# def all_members():
#     return jsonify({
#         'status': 'success',
#         'members': MEMBERS
#     })
 
if __name__ == '__main__':
    app.run()