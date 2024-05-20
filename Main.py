from flask import Flask, render_template, request
from waitress import serve
import random

Answer1 = None
Answer2 = None
Answer3 = None

app = Flask(__name__)
print("Starting...")


#Placeholder questions (Ai questions removed after logs got lost)
question = [
        "Question 1", "Question 2", "Question 3", "Question 4", "Question 5",
]
#adaptivelearning 
class AdaptiveLearning:
    def __init__(self):
        self.difficulty = 5  # Start with a medium difficulty level
        self.min_difficulty = 1
        self.max_difficulty = 10

    def adjust_difficulty(self, correct):
        """Adjust the difficulty based on the previous answer."""
        if correct:
            self.difficulty += 1
        else:
            self.difficulty -= 1
        
        # Ensure difficulty stays within bounds
        self.difficulty = max(self.min_difficulty, min(self.max_difficulty, self.difficulty))
        
        return self.difficulty

    def get_next_question(self):
        """Fetch the next question based on the current difficulty."""
        # For demonstration, we'll just return the difficulty level as the question
        return f"Question with difficulty {self.difficulty}"

# Example usage
learning_system = AdaptiveLearning()

# Simulate answering questions
answers = [True, True, False, True, False, False, True]  # Example answers: True for correct, False for incorrect

for answer in answers:
    next_difficulty = learning_system.adjust_difficulty(answer)
    next_question = learning_system.get_next_question()
    print(f"Next question: {next_question}, New difficulty: {next_difficulty}")


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
