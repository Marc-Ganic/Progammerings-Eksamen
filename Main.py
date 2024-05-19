from flask import Flask, render_template, request
from waitress import serve
import random

Answer1 = None
Answer2 = None
Answer3 = None

app = Flask(__name__)
print("Starting...")


#Placeholder questions made by blackbox AI
question = [
        "What is the syntax for defining a function in Python?",
        "How do you declare a variable in JavaScript?",
        "What is the difference between var, let, and const in JavaScript?",
        "What is the purpose of the __init__ method in Python classes?",
        "What is the difference between a list and a tuple in Python?"
]

#TODO difficulty algorithm, Score Board, 3 health points, how to gain scorepoints and lose health.

@app.route('/')
def template():
    selected_question = random.choice(question) #picks random questioen
    return render_template("template.html", question=selected_question) #displays random picked question on website

@app.route('/update_variable', methods=['POST'])
def update_variable():
    global Answer1, Answer2, Answer3
    Answer1 = request.form['Answer1']
    Answer2 = request.form['Answer2']
    Answer3 = request.form['Answer3']
    new_selected_question = random.choice(question) #a new picks random questioen
    return render_template("template.html", question=new_selected_question) #displays picked question on website

if __name__ == "__main__":
  serve(app, host="0.0.0.0", port=8001)