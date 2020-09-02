import pytest
import inquirer

test_bill_total = '58'

answers = {'tips': 'Cheap'}


# Calculates tip
def calculate_tip():
    global cheap
    global gracious
    global very_gracious
    cheap = format((float(test_bill_total) * 0.15), '.2f')
    gracious = format((float(test_bill_total) * 0.20), '.2f')
    very_gracious = format((float(test_bill_total) * 0.25), '.2f')
    # Shows user tip suggestions based on bill total
    print("\n---------------------Tip Suggestions-------------------------")
    print(f"If you want to be cheap, then tip ${cheap}")
    print(f"\nIf you want to be gracious, then tip ${gracious}")
    print(f"\nAnd if you want to be VERY gracious, then tip ${very_gracious}")
    print("-------------------------------------------------------------\n")


# Calculates and formats bill total with tip
def calculate_bill_and_tip():
    global cheap_total
    global gracious_total
    global very_gracious_total
    cheap_total = (cheap + test_bill_total)
    gracious_total = (gracious + test_bill_total)
    very_gracious_total = (very_gracious + test_bill_total)
    return


# Gives user list of answers to choose from
def questions_list():
    global answers
    questions = [
        inquirer.List('tips',
                      message="Which do you want to be?",
                      choices=['Cheap', 'Gracious', 'Very Gracious'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers


def answer_choices(answers):
    if answers[0] == "Cheap":
        print(f"Alright cheap skate, tip is ${cheap} and the total is ${cheap_total}")
    elif answers[1] == "Gracious":
        print(f"Goood on ya, tip is ${gracious}, and your bill total is ${gracious_total}")
    elif answers[2] == "Very Gracious":
        print(
            f"Wow, look at you! Your generous tip is ${very_gracious}, and your bill total is ${very_gracious_total}")
    else:
        print("")
    return answers


def test_tip_total():
    print(calculate_tip())
    return


def test_calculate_bill_and_tip():
    print(calculate_bill_and_tip())
    return


def test_list_questions():
    print(test_list_questions)


def test_answer_choices():
    test_choices = answer_choices('Cheap')
    return
