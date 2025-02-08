from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.sqlite3"
db=SQLAlchemy(app)

# Models

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String(80), nullable=False)
    full_name=db.Column(db.String(20), nullable=False)
    qualification=db.Column(db.String(20), nullable=False)
    dob=db.Column(db.Date, nullable=False)
    role=db.Column(db.String(10), nullable=False)    #admin/stud
    scores=db.relationship('Score', backref="user" )
    #cart_item=db.relationship('Cart', backref='user')

class Subject(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    description=db.Column(db.Text)
    chapters=db.relationship("Chapter", backref="subject")

class Chapter(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20), nullable=False, unique=True)
    description=db.Column(db.Text)
    subject_id=db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    quizzes=db.relationship("Quiz", backref="chapter")
    
    

class Quiz(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    chapter_id=db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    quiz_date=db.Column(db.Date, nullable=False)
    time_duration=db.Column(db.String(10), nullable=False)
    remarks=db.Column(db.Text)
    questions=db.relationship("Question", backref="quiz")
    scores=db.relationship("Score", backref="quiz")
    

class Question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    quiz_id=db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    ques_statement=db.Column(db.Text, nullable=False)
    option1=db.Column(db.String(20), nullable=False)
    option2=db.Column(db.String(20), nullable=False)
    option3=db.Column(db.String(20), nullable=False)
    option4=db.Column(db.String(20), nullable=False)
    correct_option=db.Column(db.Integer, nullable=False)

    

class Score(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    quiz_id=db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_score=db.Column(db.Integer, nullable=False)
    timestamp=db.Column(db.DateTime, nullable=False)
    


if(__name__=="__main__"):
    with app.app_context():
        db.create_all()
        print("Database Created successfully")
