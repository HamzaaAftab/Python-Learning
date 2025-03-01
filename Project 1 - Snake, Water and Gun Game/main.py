import random

# Dictionary for user input mapping
youDict = {
    "s": 1,  # Snake
    "w": -1, # Water
    "g": 0   # Gun
}

# Randomizing computer's choice
computer = random.choice([-1, 0, 1])  

# Taking user input and validating it
youStr = input("Enter your Choice (s for Snake, w for Water, g for Gun): ").lower()

if youStr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    youNum = youDict[youStr]

    # Checking game result
    if (computer == -1 and youNum == 1):
        print("Computer chose Water, You Win!")
    elif (computer == 1 and youNum == -1):
        print("Computer chose Snake, You Lose!")
    elif (computer == 1 and youNum == 1):
        print("Computer chose Snake, It's a Draw!")
    elif (computer == -1 and youNum == -1):
        print("Computer chose Water, It's a Draw!")
    elif (computer == 0 and youNum == 0):
        print("Computer chose Gun, It's a Draw!")
    elif (computer == 0 and youNum == 1):
        print("Computer chose Gun, You Lose!")
    elif (computer == 0 and youNum == -1):
        print("Computer chose Gun, You Win!")
