# TestMaker, Windows 10
# This program allows you to make and take tests
# Python Version 3.9.6
# A program by Tyler Serio

# Import necessary modules
import os
import random

# Ensure folder for Tests exists
if os.path.isdir("Tests") == False:
    os.makedirs("Tests")
    
# Begin the program loop   
running = 1
while running == 1:
    choice = "None"
    print("What would you like to do?")
    print("[1] - Take Tests!")
    print("[2] - Make or Edit Tests!")
    print("[3] - View Instructions.")
    print("[0] - Exit.")
    choice = input("Choice: ")
    print("")

    # Run if user chooses Exit option
    if choice == "0":
        print("Are you sure you want to exit?")
        print("[y] - Yes.")
        print("[n] - No.")
        exitchoice = str(input("Choice: "))
        if exitchoice == "y" or exitchoice == "Y":
            exit()
        if exitchoice == "n" or exitchoice == "N":
            choice = "None" 
            os.system("cls")
        if exitchoice != "y" and exitchoice != "Y" and exitchoice != "n" and exitchoice != "N":
            os.system("cls")
            print("You must choose from the list of options!")
            print("") 

    # Run if user chooses Take Test option
    if choice == "1":
        os.system("cls")
        taketest = 0
        step = 0
        testlist = []
        print("Which test would you like to take?")
        for x in os.listdir("Tests"):
            testlist.append(str(x))
            step += 1
            x = x.replace("_", " ")
            print("[" + str(step) + "] - " + x.replace(".txt", "."))
        print("[0] - Go Back.")
        testselect = input("Choice: ")
        print("")
        if testselect == "0":
            taketest = 0
            # are you sure?
            os.system("cls")
            pass
        else:
            os.system("cls")
            try:
                file = open("Tests/" + testlist[int(testselect) - 1], "r")
                taketest = 1
            except:
                print("You must choose from the list of options!")
                print("")

        if taketest == 1:
            q = []
            qas = []
            testing = 0
            questionnum = 0
            corrects = 0
            
            for line in file:
                if line == "#\n" or line == "#":
                    qas.append(q)
                    q = []
                else:
                    q.append(line)
                    
            random.shuffle(qas)
            testing = 1
            print(testlist[int(testselect) - 1].replace("_", " ").strip(".txt") + " Test")
            while testing == 1:
                total = len(qas)
                try:
                    current = qas[questionnum]
                except:
                    testing = 0
                    break
                question = current.pop(0)
                random.shuffle(current)
                a1 = current[0]
                a2 = current[1]
                a3 = current[2]
                a4 = current[3]
                print("Question " + str(questionnum + 1) + " of " + str(total) + ": " + question)
                print("[1] - " + a1.split(";")[0])
                print("[2] - " + a2.split(";")[0])
                print("[3] - " + a3.split(";")[0])
                print("[4] - " + a4.split(";")[0])
                print("[0] - Leave The Test!")
                print("")
                answer = input("Your Answer: ")
                answerdict = {
                        "1": a1,
                        "2": a2,
                        "3": a3,
                        "4": a4
                    }

                # Check for answers not in the dictionary ie. anything that isn't 0, 1, 2, 3, or 4
                # Force user to make a proper decision and stop being dumb.
                if answer != "0" and answer != "1" and answer != "2" and answer != "3" and answer != "4":
                    stopbeingdumb = 1
                    while stopbeingdumb == 1:
                        answer = input("You must choose an answer from the available options: ")
                        if answer != "0" and answer != "1" and answer != "2" and answer != "3" and answer != "4":
                            stopbeingdumb = 1
                        else:
                            stopbeingdumb = 0
                
                # Check to see if user selected to leave the test
                if answer == "0":
                    print("You flip the table and leave!")
                    print("")
                    break
                # Check to see if the user chose the incorrect answer
                elif answerdict[answer].split(";")[1] == " Incorrect!":
                    print("Incorrect!" + answerdict[answer].split(";")[2])
                # If the user chose the correct answer, increase their score
                else:
                    print("Correct!" + answerdict[answer].split(";")[2])
                    corrects += 1
                # Move on to the next question
                questionnum += 1

            # Print the user's score summary
            print("Summary:")
            print(f"You got {corrects} questions" + f" out of {total} questions correct.")
            score = round((corrects / total), 4) * 100
            exclamation = ""
            if score == 0:
                exclamation = " You got all of them wrong! Study more, please!"
            if score > 0:
                exclamation = " You got an F! You have to study more!"
            if score > 50:
                exclamation = " You need to study more! You didn't do well."
            if score > 60:
                exclamation = " Don't worry! If you study more, you will succeed!"
            if score > 70:
                exclamation = " You're getting there, but you still need to study more!"
            if score > 80:
                exclamation = " Good work! You're getting there!"
            if score > 90:
                exclamation = " Good job! You got most of them correct!"
            if score == 100:
                exclamation = " Perfect! Great job!"
            print(f"That means you got {score}% of the questions correct!" + exclamation)
            derp = input("Enter any key to continue: ")
            choice = "None"
            os.system("cls")

    # Run if user chooses Make or Edit Test option
    if choice == "2":
        print("Not available yet!")
        derp = input("Enter any key to continue: ")
        os.system("cls")
        ######## create or choose your test
        ######## edit questions of test
        ######## save test, delete test, or exit without saving

    # Run if user chooses View Instructions option
    if choice == "3":
        print("Not available yet!")
        derp = input("Enter any key to continue: ")
        os.system("cls")
        ########### explain choices
        ########### 

    # If the user made a selection not in the list of options, tell them
    if choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "None":
        os.system("cls")
        print("You must choose from the list of options!")
        print("")
        
