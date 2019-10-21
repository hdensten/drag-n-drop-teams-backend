from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Student(db.Model):
    __tablename__ = "students"  # ?
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    team = db.Column(db.Integer)

    def __init__(self, name, team):
        self.name = name
        self.team = team


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('name', 'team')


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@app.route('/student', methods=["POST"])
def add_student():
    name = request.json['name']
    team = request.json['team']

    new_student = Student(name, team)

    db.session.add(new_student)
    db.session.commit()

    student = Student.query.get(new_student.id)

    return student_schema.jsonify(student)


if __name__ == '__main__':
    app.run(debug=True)
