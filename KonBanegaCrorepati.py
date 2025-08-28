# Excercise 2 Kon banega crorepati
heading = "LET's PLAY KON BANEGA CROREPATI"
print(heading.center(150))

questions = [
    "Who was the first President of India?",
    "What is the capital city of Australia?",
    "In which year did India gain independence from British rule?",
    "Which planet is known as the Red Planet?",
    "Who wrote the Indian national anthem 'Jana Gana Mana'?"
]
answers = [
    "Rajendra Prasad",
    "Canberra",
    "1947",
    "Mars",
    "Rabindranath Tagore"
]

money = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.strip().lower() == answers[i].strip().lower():
        print("✅ Correct! You got 100,000")
        money += money
    else:
        print(f"❌ Wrong answer. The correct answer was: {answers[i]}")
        print(f"💥 Today, you are going home with this amount of money: {money}")
        break
else:
    print(f"🎉 Congratulations! You answered all questions correctly.")
    print(f"🏆 Final score: {money}")