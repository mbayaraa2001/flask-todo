from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Todo(db.Model):
    todo_id = db.Column(Integer, primary_key = True)
    todo_name = db.Column(db.String(100))
    todo_comment = db.Column(db.String(200))
    todo_time = db.Column(db.DateTime())
    todo_complete = db.Column(db.Boolean)

@app.route("/")
def index():
    # print all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', return_todo_list = todo_list)


@app.route("/todo_add", methods=["POST", "GET"])
def todo_add():
    if request.method=="POST":       
        new_todo = Todo(todo_name = request.form.get("todo_name"), todo_comment = request.form.get("todo_comment"), todo_time = datetime.now(), todo_complete=False)
        db.session.add(new_todo)
        db.session.commit()
        print(db.session.commit())
        return redirect(url_for("index")) 


if __name__=="__main__":
    with app.app_context():
        db.create_all() 
    
    app.run(debug=True)