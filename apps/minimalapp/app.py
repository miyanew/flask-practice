from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return "Hello, Flaskbook!"

@app.get("/hello/<int:num>",
          endpoint = "hl")
def hello(num):
  return f"Hello, {num}"

# show_name エンドポイント
@app.get("/name/<name>")
def show_name(name):
  return render_template("index.html", name=name)
