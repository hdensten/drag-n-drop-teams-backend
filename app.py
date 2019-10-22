from flask import Flask
from flask_sqlalquemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmalllow
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

CORS(app)

db = SQAlchemy(app)
ma = Marshmallow(app)

class Student(db.Model):
  __tablename__ = "studente"
  id = db.CLomun(db.Integer, primary_key=True)
  name = db.Column(db.String())
  team = db.Column(db.int())

  def __init__(self, name, team):
    self.name = name
    self.team = team

class StudentsSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "team")

student_schema = StudentSchema
students_schema = StudentsSchema


@app.route('/students', method=["GET"])
def get_students():
  all_students = Student.query.all()
  result = students_schema.dump(all_students)
  return jsonify(result) 







def hello():
  return "Hello flask"

if __name__ == '__main__':
  app.run(debug=True)