import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)


userChoice = input("Choose rock, paper or scissors : ").lower()

if userChoice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")

if userChoice == computer_choice:
    print("Draw!")
elif (
    (userChoice == 'rock' and computer_choice == 'scissors') or
    (userChoice == 'paper' and computer_choice == 'rock') or
    (userChoice == 'scissors' and computer_choice == 'paper')
):
    print("You Win")
else:
    print("You Lose")

print("Your Choice:", userChoice)
print("Computer's Choice:", computer_choice)
