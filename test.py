# let's import the flask
from flask import Flask, Response
import json
import pymongo
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://marinkoco:xxxx@30daysofpython.wzhhpfw.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['30DaysofPython']  # accessing the database
students = list(db.students.find())

@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    response = Response(json.dumps(students), mimetype='application/json')
    client.close()  # close the database connection
    return response

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
