from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        db.session.add(Item(name=name))
        db.session.commit()
        return redirect("/")
    return render_template("create.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    item = Item.query.get_or_404(id)

    if request.method == "POST":
        item.name = request.form["name"]
        db.session.commit()
        return redirect("/")
        
    return render_template("edit.html", item=item)

@app.route("/delete/<int:id>")
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
