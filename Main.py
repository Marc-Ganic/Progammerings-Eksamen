from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)
print("Starting...")

@app.route('/')
@app.route('/index')
def index():
  name = request.args.get('name')
  if name == "Play!": # name should be the same as name of Gamebtn in index.html
    return render_template("template.html")
  else:
    return render_template("index.html")


@app.route('/template')
def template():
  return render_template("template.html")

if __name__ == "__main__":
  serve(app, host="0.0.0.0", port=8888)