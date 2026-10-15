import random
from datetime import datetime

def best_score(filename):
    best = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                result = line.strip().split("| ")[1]
                got = int(result.split("/")[0])
                if got > best:
                    best = got
    except FileNotFoundError:
        return 0
    return best

questions = [
    {"question": "What is the capital of Nigeria?", "answer": "Abuja"},
    {"question": "How many days are in a week?", "answer": "7"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "How many seconds make a minute?", "answer": "60"},
    {"question": "Nigeria is in which continent?", "answer": "Africa"}    
]

count = min(10, len(questions))
selected = random.sample(questions, count)
score = 0

for q in selected:
    answer = input(q["question"] + " ").strip()
    if answer.lower() == q["answer"].lower():
        print("Correct!")
        score = score + 1
    else:
        print(f"Wrong. The answer is {q['answer']}.")
        
print(f"You scored {score} out of {len(selected)}.")

now = datetime.now().strftime("%Y-%m-%d %H:%M")
with open("scores.txt", "a") as file:
    file.write(f"{now} | {score}/{len(selected)}\n")
    
print(f"Best score so far: {best_score('scores.txt')}")
            