from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# connect database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pete040101'
app.config['MYSQL_DB'] = 'comment_animekub'
mysql = MySQL(app)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, resources={r'/*': {'origins': '*'}})


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