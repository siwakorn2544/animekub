from flask import Flask
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
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/animekub', methods=['POST'])
def insert_com():
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO comment (animeid, personname, comment)VALUES(%s,%s,%s)''',(1,'Peng','สวยพี่น้อง'))
    mysql.connection.commit()
    cursor.close()
    return {'msg':"เสร็จละ"}
if __name__ == '__main__':
    app.run()