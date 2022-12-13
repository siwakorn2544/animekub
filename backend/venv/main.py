from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

MYSQLHOST=os.getenv("MYSQLHOST")
MYSQLUSER=os.getenv("MYSQLUSER")
MYSQLPASSWORD=os.getenv("MYSQLPASSWORD")
MYSQL_DB=os.getenv("MYSQL_DB")

# configuration
# DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# connect database
app.config['MYSQL_HOST'] = MYSQLHOST
app.config['MYSQL_USER'] = MYSQLUSER
app.config['MYSQL_PASSWORD'] = MYSQLPASSWORD
app.config['MYSQL_DB'] = MYSQL_DB
mysql = MySQL(app)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return {'msg':"NICEEEE"}


@app.route('/postcomment', methods=['POST'])
def insert_com():
    cursor = mysql.connection.cursor()
    result = request.json
    print(result)
    cursor.execute(''' INSERT INTO comment (animeid, personname, comment)VALUES(%s,%s,%s)''',(result['animeid'], result['personname'], result['comment']))
    mysql.connection.commit()
    cursor.close()
    return {'msg':"เสร็จละ"}

@app.route('/getcomment/<id>', methods=['GET'])
def get_com(id):
    # result1 = request.args.get()
    cursor = mysql.connection.cursor()
    #sql = ''' SELECT * FROM comment WHERE animeid = %s'''
    cursor.execute("SELECT * FROM comment WHERE animeid = %s", {id})
    result = cursor.fetchall()
    response = jsonify(result)
    response.status_code = 200
    return response
    
    
if __name__ == '__main__':
    app.run()
