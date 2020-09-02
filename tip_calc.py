import inquirer
from pprint import pprint

# Tip calculator without modules

# Collects bill total from user, and removes '$' if user inputs it
bill_total = float(input("What is your bill total?\n").strip('$'))

# Calculates tip
cheap = float(bill_total * 0.15)
gracious = float(bill_total * 0.20)
very_gracious = float(bill_total * 0.25)

# Calculates and formats bill total with tip
cheap_total = format((cheap + bill_total), '.2f')
gracious_total = format((gracious + bill_total), '.2f')
very_gracious_total = format((very_gracious + bill_total), '.2f')

# Shows user tip suggestions based on bill total
print("\n---------------------Tip Suggestions-------------------------")
print(f"If you want to be cheap, then tip ${cheap:.2f}")
print(f"\nIf you want to be gracious, then tip ${gracious:.2f}")
print(f"\nAnd if you want to be VERY gracious, then tip ${very_gracious:.2f}")
print("-------------------------------------------------------------\n")

# Gives user list of answers to choose from
questions = [
    inquirer.List('tips',
                  message="Which do you want to be?",
                  choices=['Cheap', 'Gracious', 'Very Gracious'],
                  ),
]
answers = inquirer.prompt(questions)

# Based on user choice, gives tip total and bill total
if answers['tips'] == "Cheap":
    print(f"Alright cheap skate, tip is ${cheap:.2f} and the total is ${cheap_total}")
elif answers['tips'] == "Gracious":
    print(f"Good on ya, tip is ${gracious:.2f}, and your bill total is ${gracious_total}")
elif answers['tips'] == "Very Gracious":
    print(f"Wow, look at you! Your generous tip is ${very_gracious:.2f}, and your bill total is ${very_gracious_total}")
else:
    print("")