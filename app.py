from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/msi/Desktop/ToDoApp/todo.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    todos=Todo.query.all()
    return render_template("index.html",todos=todos)

@app.route("/add",methods=["POST"])
def addTodo():
    title=request.form.get("title")
    content=request.form.get("content")
    newTodo=Todo(title=title,content=content)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def detailTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    return render_template("detail.html",todo=todo)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    #title = db.Column(db.String(80), unique=True, nullable=False)




if __name__=='__main__':
    app.run(debug=True)