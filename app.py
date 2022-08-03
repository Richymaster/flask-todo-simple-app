from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
# from models import Todo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/todo_app'
app.config['SECRET_KEY'] = 'nzyrw4uZOu8fcuaeruolumiouxizif'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean())
    comments = db.Column(db.String(255))
    

    # def __init__(self, *args, **kwargs):
    #     super(Todo, self).__init__(*args, **kwargs)
    def __init__(self, task, completed):
        self.task = task
        self.completd = completed
        
db.create_all()
        
@app.route('/')
def index():
    todos = Todo.query.all()
    print(todos)
    
    return render_template('index.html', todos=todos)

@app.route('/todo', methods=['POST', 'GET'])
def todos():
    if request.method == 'POST':
        task = request.form.get('task')
        completed = request.form.get('completed')
        description = request.form.get('description')
        comments = request.form.get('comments')
        
        new_task = Todo(task=task, description=description, comments=comments, completed=completed)
        db.session.add(new_task)
        db.session.commit()
        message = ("New Task Successfully Created!")
        
        return redirect('/')
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 