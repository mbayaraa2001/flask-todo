from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    todo_form = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    # show all todos
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    #add new item
    todo_form= request.form.get("todo_form")
    new_todo= Todo(todo_form=todo_form, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update():
    #update form
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete
   
    db.session.
    db.session.commit()
    return redirect(url_for("index"))



if __name__=="__main__":
    with app.app_context():
        db.create_all()
        new_todo= Todo(todo_form="todo 1", complete=False)
        db.session.add(new_todo)
        db.session.commit()
    #new_todo 
   
    
    app.run(debug=True)