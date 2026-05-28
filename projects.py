#Init
import pandas as pd
import random
global score




data = pd.read_csv('chem.csv')


id=data['id'].tolist()
period=data['Period Number'].tolist()
name=data['Name'].tolist()
symbol=data['Symbol'].tolist()
atomic=data['Atomic Number'].tolist()
classify=data['Atom Classification'].tolist()
group=data['Group'].tolist()


filter = []
radnom_symbol = random.choice(symbol)


#Functions
#This function asks the user for a number, then prints out the elements belonging to that period.
def periods(number):
    for i in range(len(period)):
        if period[i] == number and number == 1:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 2:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 3:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 4:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 5:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 6:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()
        elif period[i] == number and number == 7:
            filter.append(name[i])
            filter.append(symbol[i])
            print(filter)
            filter.clear()


#This function asks the user for an element, and prints out the element along with the symbol.
def symbols(element):
    element = element.strip().lower()
    found = False


    for i in range(len(name)):
        current_name = str(name[i]).strip().lower()


        if element == "all":
            print(name[i], "-", symbol[i])
            found = True


        elif element in current_name:
            print(name[i], "-", symbol[i])
            found = True


    if not found:
        print("Element not found.")








#This function prints out every important information about the element that the study guide will focus on.
def review():
    for i in range(len(id)):
        print(id[i],":", "-", period[i], "-", name[i], "-", symbol[i], "-", atomic[i], "-", classify[i], "-", group[i])


#This function helps the user focus on a certain classification group for elements.
def define(metal):
    for i in range(len(classify)):
        current_class = str(classify[i]).strip().lower()
        user_input = str(metal).strip().lower()


        if user_input == "all":
            print(name[i], "-", classify[i])


        elif user_input == "metal":
            if "metal" in current_class and "nonmetal" not in current_class:
                print(name[i], "-", classify[i])


        elif current_class == user_input:
            print(name[i], "-", classify[i])


#This function prints elements along with their atomic number.
def num():
    for i in range(len(atomic)):
        print(name[i], "-", atomic[i])


#This function prints all elements and their group for the user to review before choosing to study.
def metal():
    for i in range(len(group)):
        print(name[i], "-", group[i])


#This function helps the user study Chemistry material involing the Periodic Table.
def quiz():
    print("---------MENU---------")
    print("Periodic table review")
    print("1. Period Number")
    print("2. Symbols")
    print("3. Atom Classification")
    print("4. Element Groups")
    print("5. Full Review")
    userchoice=input("Which would you like to focus on today?: ")
    if userchoice == "1":
        num_questions=int(input("How many questions would you like to do?: "))
        score = 0
        for i in range(num_questions):
            random_index = random.randint(0, len(name) -1)
            random_element = name[random_index]
            correct_period=str(period[random_index]).strip().replace('"', '').replace("'", "").lower()
            answer=input(f"Question {i+1}: What is the period for {random_element}?: ").strip().lower()
            if answer == correct_period:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer was {correct_period}.")
        print("RESULTS:")
        print("You got", score, "right.")
        print("Your score:", score / num_questions * 100, "%")


    elif userchoice == "2":
        num_questions=int(input("How many questions would you like to do?: "))
        score = 0
        for i in range(num_questions):
            random_index = random.randint(0, len(name) -1)
            random_element = name[random_index]
            correct_symbol=str(symbol[random_index]).strip().replace('"', '').replace("'", "").lower()
            answer=input(f"Question {i+1}: What is the symbol for {random_element}?: ").strip().lower()
            if answer == correct_symbol:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer was {correct_symbol}.")
        print("RESULTS:")
        print("You got", score, "right.")
        print("Your score:", score / num_questions * 100, "%")
    elif userchoice == "3":
        num_questions=int(input("How many questions would you like to do?: "))
        score = 0
        for i in range(num_questions):
            random_index = random.randint(0, len(name) -1)
            random_element = name[random_index]
            correct_classify=str(classify[random_index]).strip().replace('"', '').replace("'", "").lower()
            answer=input(f"Question {i+1}: What is the atom classification for {random_element}?: ").strip().lower()
            if answer == correct_classify:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer was {correct_classify}.")
        print("RESULTS:")
        print("You got", score, "right.")
        print("Your score:", score / num_questions * 100, "%")
    elif userchoice == "4":
        num_questions=int(input("How many questions would you like to do?: "))
        score = 0
        indices = random.sample(range(len(name)), num_questions)
        for i in range(num_questions):
            random_index = indices[i]
            random_element = name[random_index]
            correct_group=str(group[random_index]).strip().replace('"', '').replace("'", "").lower()
            answer=input(f"Question {i+1}: What group does {random_element} belong too?: ").strip().lower()
            if answer == correct_group:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer was {correct_group}.")
        print("RESULTS:")
        print("You got", score, "right.")
        print("Your score:", score / num_questions * 100, "%")
    elif userchoice == "5":
        num_questions = int(input("How many questions would you like to do?: "))
        score = 0
        for i in range(num_questions):
            random_index=random.randint(0, len(name) -1)
            random_element = name[random_index]


            question_type = random.randint(1,4)


            if question_type == 1:
                correct_answer = str(period[random_index]).strip().replace('"', '').replace("'", "").lower()
                answer = input(f"Question {i+1}: What period is {random_element} in?: ").strip().lower()


            elif question_type == 2:
                correct_answer = str(symbol[random_index]).strip().replace('"', '').replace("'", "").lower()
                answer = input(f"Question {i+1}: What is the symbol for {random_element}?: ").strip().lower()


            elif question_type == 3:
                correct_answer = str(classify[random_index]).strip().replace('"', '').replace("'", "").lower()
                answer = input(f"Question {i+1}: What is the atom classification of {random_element}?: ").strip().lower()


            elif question_type == 4:
                correct_answer = str(group[random_index]).strip().replace('"', '').replace("'", "").lower()
                answer = input(f"Question {i+1}: What group does {random_element} belong to?: ").strip().lower()


            if answer == correct_answer:
                print("Correct!")
                score +=1
            else:
                print(f"Wrong. The correct answer was {correct_answer}.")


        print("RESULTS:")
        print("You got", score, "right.")
        print("Your score:", score / num_questions * 100, "%")


def study():
    while True:
        print("---------MENU---------")
        print("Study Materials")
        print("1. Review elements by period")
        print("2. Look up symbol by element name")
        print("3. Review by classification")
        print("4. Review all atomic numbers")
        print("5. Review all element groups")
        print("6. Full review")
        print("7. Exit study menu")
        userchoice1=input("What would you like to study?: ").strip()


        if userchoice1 == "1":
            number=int(input("Enter a period number (1-7): "))
            periods(number)


        elif userchoice1 == "2":
            element = input("Enter an element name or type 'all': ").strip()
            symbols(element)


        elif userchoice1 == "3":
            metal_type = input("Enter a classification type or 'all': ").strip()
            define(metal_type)


        elif userchoice1 == "4":
            num()


        elif userchoice1 == "5":
            metal()


        elif userchoice1 == "6":
            review()


        elif userchoice1 == "7":
            print("Exiting study menu...")
            break


        else:
            print("Invalid choice. Try again.")
