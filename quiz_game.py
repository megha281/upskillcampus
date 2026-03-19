import random
import os
import time


class QuizGame:

    def __init__(self):
        self.score = 0
        self.time_limit = 10
        self.high_score_file = "highscore.txt"

        self.questions = [
            {"question": "What does 'print()' do?", "options": {"A": "Input", "B": "Output", "C": "Store", "D": "Loop"}, "answer": "B", "category": "python", "difficulty": "easy"},
            {"question": "Which symbol is used for comments?", "options": {"A": "#", "B": "//", "C": "--", "D": "/* */"}, "answer": "A", "category": "python", "difficulty": "easy"},
            {"question": "Which keyword defines a function?", "options": {"A": "func", "B": "def", "C": "function", "D": "define"}, "answer": "B", "category": "python", "difficulty": "medium"},
            {"question": "What is a list?", "options": {"A": "Immutable", "B": "Ordered & changeable", "C": "Number", "D": "Loop"}, "answer": "B", "category": "python", "difficulty": "medium"},
            {"question": "What is the output of len([1,2,3])?", "options": {"A": "2", "B": "3", "C": "1", "D": "Error"}, "answer": "B", "category": "python", "difficulty": "hard"},
            {"question": "Which data type is immutable?", "options": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"}, "answer": "C", "category": "python", "difficulty": "medium"},
            {"question": "Which loop is used when iterations are known?", "options": {"A": "while", "B": "for", "C": "loop", "D": "repeat"}, "answer": "B", "category": "python", "difficulty": "easy"},
            {"question": "What is the output of 3**2?", "options": {"A": "6", "B": "9", "C": "8", "D": "5"}, "answer": "B", "category": "python", "difficulty": "easy"},
            {"question": "Which keyword is used to handle exceptions?", "options": {"A": "catch", "B": "try", "C": "handle", "D": "excepted"}, "answer": "B", "category": "python", "difficulty": "medium"},
            {"question": "What does 'len()' function do?", "options": {"A": "Counts elements", "B": "Adds elements", "C": "Removes elements", "D": "Sorts elements"}, "answer": "A", "category": "python", "difficulty": "easy"},

            {"question": "Capital of India?", "options": {"A": "Mumbai", "B": "Delhi", "C": "Chennai", "D": "Kolkata"}, "answer": "B", "category": "gk", "difficulty": "easy"},
            {"question": "Largest planet?", "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"}, "answer": "C", "category": "gk", "difficulty": "medium"},
            {"question": "Who discovered gravity?", "options": {"A": "Newton", "B": "Einstein", "C": "Tesla", "D": "Edison"}, "answer": "A", "category": "gk", "difficulty": "easy"},
            {"question": "Speed of light?", "options": {"A": "300,000 km/s", "B": "150,000 km/s", "C": "1,000 km/s", "D": "500 km/s"}, "answer": "A", "category": "gk", "difficulty": "hard"},
            {"question": "National animal of India?", "options": {"A": "Lion", "B": "Tiger", "C": "Elephant", "D": "Leopard"}, "answer": "B", "category": "gk", "difficulty": "easy"},
            {"question": "Smallest prime number?", "options": {"A": "1", "B": "2", "C": "3", "D": "0"}, "answer": "B", "category": "gk", "difficulty": "easy"},
            {"question": "Which ocean is largest?", "options": {"A": "Atlantic", "B": "Indian", "C": "Pacific", "D": "Arctic"}, "answer": "C", "category": "gk", "difficulty": "medium"},
            {"question": "Who is known as the Father of Computers?", "options": {"A": "Newton", "B": "Einstein", "C": "Charles Babbage", "D": "Alan Turing"}, "answer": "C", "category": "gk", "difficulty": "medium"},
            {"question": "Which gas do plants absorb?", "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon Dioxide", "D": "Hydrogen"}, "answer": "C", "category": "gk", "difficulty": "easy"},
            {"question": "Which country hosted FIFA 2018?", "options": {"A": "Brazil", "B": "Russia", "C": "Qatar", "D": "Germany"}, "answer": "B", "category": "gk", "difficulty": "hard"}
        ]

    def load_high_score(self):
        if not os.path.exists(self.high_score_file):
            return 0
        try:
            with open(self.high_score_file, "r") as f:
                return int(f.read().strip())
        except:
            return 0

    def save_high_score(self, score):
        try:
            with open(self.high_score_file, "w") as f:
                f.write(str(score))
        except:
            print("Error saving high score.")

    def choose_option(self, prompt, choices):
        while True:
            print("\n" + prompt)
            for key, value in choices.items():
                print(f"{key}. {value}")

            choice = input("Enter choice: ").strip()

            if choice in choices:
                return choices[choice]
            else:
                print("Invalid choice. Try again.")

    def filter_questions(self, category, difficulty):
        return [q for q in self.questions if q["category"] == category and q["difficulty"] == difficulty]

    def ask_question(self, q):
        print("\n" + "-" * 50)
        print(q["question"])

        for opt, text in q["options"].items():
            print(f"{opt}. {text}")

        start = time.time()
        ans = input("Answer (A/B/C/D): ").upper()
        end = time.time()

        if end - start > self.time_limit:
            print("⏰ Time up!")
            return False

        if ans not in ["A", "B", "C", "D"]:
            print("Invalid answer.")
            return False

        if ans == q["answer"]:
            print("✅ Correct")
            return True
        else:
            print(f"❌ Wrong. Correct: {q['answer']}")
            return False

    def show_result(self, total):
        percent = (self.score / total) * 100

        print("\n📊 RESULT")
        print(f"Score: {self.score}/{total}")
        print(f"Percentage: {percent:.2f}%")

        if percent >= 80:
            print("🌟 Excellent!")
        elif percent >= 50:
            print("👍 Good job!")
        else:
            print("📘 Keep practicing!")

    def run(self):
        print("\n🎯 QUIZ GAME ")

        category = self.choose_option("Choose Category:", {"1": "python", "2": "gk"})
        difficulty = self.choose_option("Choose Difficulty:", {"1": "easy", "2": "medium", "3": "hard"})

        filtered = self.filter_questions(category, difficulty)

        if not filtered:
            print("No questions available for this selection.")
            return

        random.shuffle(filtered)
        self.score = 0

        for q in filtered:
            if self.ask_question(q):
                self.score += 1

        self.show_result(len(filtered))

        high = self.load_high_score()
        print(f"🏆 High Score: {high}")

        if self.score > high:
            print("🎉 New High Score!")
            self.save_high_score(self.score)

        again = input("\nPlay again? (y/n): ").lower()
        if again == "y":
            self.run()
        else:
            print("Thanks for playing! 👋")


if __name__ == "__main__":
    game = QuizGame()
    game.run()