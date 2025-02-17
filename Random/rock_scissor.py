import random

# ASCII art for Rock, Paper, Scissors
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

# Store choices in a list
choices = [rock, paper, scissors]

# User input
user_choice = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors:\n "))

# Validate input
if user_choice not in [0, 1, 2]:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    # Computer's random choice
    computer_choice = random.randint(0, 2)

    # Display choices
    print("\nYou chose:")
    print(choices[user_choice])

    print("Computer chose:")
    print(choices[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")