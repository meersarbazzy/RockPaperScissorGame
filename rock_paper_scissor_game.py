import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of gestures
gestures = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors game!")
print("Press 0 for Rock, 1 for Paper, and 2 for Scissors")

# User's choice
action = int(input("Enter a Number: "))
print("You chose")

if action == 0:
    print(gestures[0])
elif action == 1:
    print(gestures[1])
elif action == 2:
    print(gestures[2])
else:
    print("Please enter a valid number for the respective gesture.")
    exit()

# Computer's choice
computer_choice = random.randint(0, 2)
print("Computer chose")
print(gestures[computer_choice])

# Determine the winner
if action == computer_choice:
    print("It's a draw!")
elif (action == 0 and computer_choice == 2) or (action == 1 and computer_choice == 0) or (action == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
