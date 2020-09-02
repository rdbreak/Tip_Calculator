import inquirer
# noinspection PyUnresolvedReferences,PyUnresolvedReferences
from font import color


# Tip calculator with modules
def bill_total():
    while True:
        global bill_total
        bill_total = input("What is your bill total?\n").strip('$')
        try:
            check_bill_total = float(bill_total)
            print(f"\n{color.BOLD}{color.GREEN}Bill total entered: ${check_bill_total:.2f}")
            print(color.END)
            break
        except ValueError:
            try:
                float(bill_total)
                print(f"\n{color.BOLD}{color.GREEN}Bill total entered: ${bill_total:.2f}")
                print(color.END)
                break
            except ValueError:
                print(f"\n{color.BOLD}{color.RED}I need a number to calculate the bill...Try again\n")
                print(color.END)
    return


# Calculates tip
def calculate_tip():
    global cheap
    global generous
    global very_generous
    # noinspection PyTypeChecker
    cheap = (float(bill_total) * 0.15)
    # noinspection PyTypeChecker
    generous = (float(bill_total) * 0.20)
    # noinspection PyTypeChecker
    very_generous = (float(bill_total) * 0.25)
    # Shows user tip suggestions based on bill total
    print(f"{color.YELLOW}-------------------- Tip Suggestions ------------------------\n")
    print(f"If you want to be cheap, then tip ${cheap:.2f}")
    print(f"\nIf you want to be generous, then tip ${generous:.2f}")
    print(f"\nAnd if you want to be VERY generous, then tip ${very_generous:.2f}\n")
    print(f"-------------------------------------------------------------\n{color.END}")
    return


# Calculates and formats bill total with tip
def calculate_bill_and_tip():
    global cheap_total
    global generous_total
    global very_generous_total
    # noinspection PyTypeChecker
    cheap_total = format((cheap + float(bill_total)), '.2f')
    # noinspection PyTypeChecker
    generous_total = format((generous + float(bill_total)), '.2f')
    # noinspection PyTypeChecker
    very_generous_total = format((very_generous + float(bill_total)), '.2f')
    return


# Gives user list of answers to choose from
def questions_list():
    global answers
    questions = [
        inquirer.List('tips',
                      message="Which do you want to be?",
                      choices=['Cheap - 15%', 'Generous - 20%', 'Very Generous - 25%'],
                      ),
    ]
    answers = inquirer.prompt(questions)


def answer_choices():
    if answers['tips'] == "Cheap - 15%":
        print(f"{color.RED}Alright cheap skate, tip is ${cheap:.2f} and the total is ${cheap_total}{color.END}")
    elif answers['tips'] == "Generous - 20%":
        print(f"Good on ya, tip is ${generous:.2f}, and your bill total is ${generous_total}")
    elif answers['tips'] == "Very Generous - 25%":
        print(
            f"{color.GREEN}Wow, look at you! Your generous tip is ${very_generous:.2f}, and your bill total is ${very_generous_total}{color.END}")
    else:
        print("")
    return answers


#  Collects bill total from user, and removes '$' if user inputs it
if __name__ == "__main__":
    bill_total()

    tip_total = (calculate_tip())

    calculate_tip_bill = (calculate_bill_and_tip())

    list_questions = (questions_list())

    list_final_bill = answer_choices()
