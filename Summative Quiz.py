##Variable/Function area
topicsList =["Animals", "Video games", "Memes", "Languages", "Science", "Music", "Technology"]
playerScore = 0
playerWrongCount = 0
questionNumber = 1
options = ["A", "a", "B", "b", "C", "c", "D", "d"]

def actionAfterRight():
    global playerScore
    global questionNumber
    playerScore = playerScore + 1
    print("Your current score is:", playerScore)
    questionNumber = questionNumber + 1
    print("\n")

def actionAfterWrong():
    global playerWrongCount
    global questionNumber
    playerWrongCount = playerWrongCount + 1
    questionNumber = questionNumber + 1
    print("Wrong answer.")
    print("\n")

def easyQuiz():
    global playerScore
    global playerWrongCount
    global questionNumber
    global options
    print("Welcome to the easy quiz!" , "\n")
    loop = 1

    with open("quizEasy.txt", "r") as text_file_easy:
            for line in itertools.islice(text_file_easy, 0, 5):
                cleanedLine = line.strip()
                print(cleanedLine)


    while loop < 2:
        print("\n")
        q1R = input("Please choose an answer.")
        q1R = q1R.upper()
        if q1R == q1EA:
            actionAfterRight()

        elif q1R not in options:
            print("Enter a valid input.")
            continue
        else:
            actionAfterWrong()


        if questionNumber == 2:
            with open("quizEasy.txt", "r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 6, 11):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q2R = input("Please choose an answer.")
                q2R = q2R.upper()
                if q2R == q2EA:
                    actionAfterRight()

                elif q2R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 3:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 12, 17):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q3R = input("Please choose an answer.")
                q3R = q3R.upper()
                if q3R == q3EA:
                    actionAfterRight()

                elif q3R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 4:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 18, 23):
                    cleanedLine = line.strip()
                    print(cleanedLine)

            print("\n")
            q4R = input("Please choose an answer.")
            q4R = q4R.upper()
            if q4R == q4EA:
                actionAfterRight()

            elif q4R not in options:
                print("Enter a valid input.")
                continue

            else:
                actionAfterWrong()

        if questionNumber == 5:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 24, 29):
                    cleanedLine = line.strip()
                    print(cleanedLine)

            print("\n")
            q5R = input("Please choose an answer.")
            q5R = q5R.upper()
            if q5R == q5EA:
                actionAfterRight()

            elif q5R not in options:
                print("Enter a valid input.")
                continue

            else:
                actionAfterWrong()

        if questionNumber == 6:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 30, 35):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q6R = input("Please choose an answer.")
                q6R = q6R.upper()
                if q6R == q6EA:
                    actionAfterRight()

                elif q6R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 7:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 36, 41):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q7R = input("Please choose an answer.")
                q7R = q7R.upper()
                if q7R == q7EA:
                    actionAfterRight()

                elif q7R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 8:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 42, 47):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q8R = input("Please choose an answer.")
                q8R = q8R.upper()
                if q8R == q8EA:
                    actionAfterRight()

                elif q8R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 9:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 48, 53):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q9R = input("Please choose an answer.")
                q9R = q9R.upper()
                if q9R == q9EA:
                    actionAfterRight()

                elif q9R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 10:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 54, 59):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q10R = input("Choose an answer.")
                q10R = q10R.upper()
                if q10R == q10EA:
                    actionAfterRight()

                elif q10R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 11:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 60, 65):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q11R = input("Choose an answer.")
                q11R = q11R.upper()
                if q11R == q11EA:
                    actionAfterRight()

                elif q11R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 12:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 66, 69):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q12R = input("Chooose an answer.")
                q12R = q12R.upper()
                if q12R == q12EA:
                    actionAfterRight()

                elif q12R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 13:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 70, 75):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q13R = input("Please choose an answer.")
                q13R = q13R.upper()
                if q13R == q13EA:
                    actionAfterRight()

                elif q13R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 14:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 76, 81):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q14R = input("Please choose an answer.")
                q14R = q14R.upper()
                if q14R == q14EA:
                    actionAfterRight()

                elif q14R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 15:
            with open("quizEasy.txt","r") as text_file_easy:
                for line in itertools.islice(text_file_easy, 82, 87):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q15R = input("Please choose an answer.")
                q15R = q15R.upper()
                if q15R in options:
                    actionAfterRight()
                    print("Congratulation on completing the quiz with the score of:", playerScore, ".")
                    print("You chose the difficulty:", playerDifficulty, "and got", playerWrongCount, "incorrect response(s).")
                    w = open("quizEasyResult.txt","a")
                    w.write("\n")
                    w.write("Player name: ")
                    w.write(str(playerName))
                    w.write("\n")
                    w.write("Difficulty: ")
                    w.write(str(playerDifficulty))
                    w.write("\n")
                    w.write("Points: ")
                    w.write(str(playerScore))
                    w.write("\n")
                    w.write("Wrong answers: ")
                    w.write(str(playerWrongCount))
                    w.write("\n")
                    w.close()
                    break


                elif q15R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()
                    print("Congratulation on completing the quiz with the score of:", playerScore, ".")
                    print("You chose the difficulty:", playerDifficulty, "and got", playerWrongCount, "incorrect response(s).")
                    w = open("quizEasyResult.txt","a")
                    w.write("\n")
                    w.write("Player name: ")
                    w.write(str(playerName))
                    w.write("\n")
                    w.write("Difficulty: ")
                    w.write(str(playerDifficulty))
                    w.write("\n")
                    w.write("Points: ")
                    w.write(str(playerScore))
                    w.write("\n")
                    w.write("Wrong answers: ")
                    w.write(str(playerWrongCount))
                    w.write("\n")
                    w.close()
                    break
def hardQuiz():
    global playerScore
    global playerWrongCount
    global questionNumber
    global options

    print("Welcome to the hard quiz!", "\n")
    loop = 1

    with open("quizHard.txt", "r") as text_file_hard:
            for line in itertools.islice(text_file_hard, 0, 5):
                cleanedLine = line.strip()
                print(cleanedLine)

    while loop < 2:
        print("\n")
        q1R = input("Choose an answer.")
        q1R = q1R.upper()
        if q1R == q1HA:
            actionAfterRight()

        elif q1R not in options:
            print("Enter a valid input.")
            continue
        else:
            actionAfterWrong()

        if questionNumber == 2:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 6, 11):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q2R = input("Choose an answer.")
                q2R = q2R.upper()
                if q2R == q2HA:
                    actionAfterRight()

                elif q2R not in options:
                    print("Choose an valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 3:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 12, 17):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q3R = input("Choose an answer.")
                q3R = q3R.upper()
                if q3R == q3HA:
                    actionAfterRight()

                elif q3R not in options:
                    print("Enter a valid input.")
                    continue

                else:
                    actionAfterWrong()

        if questionNumber == 4:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 18, 23):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q4R = input("Choose an answer.")
                q4R = q4R.upper()
                if q4R == q4HA:
                    actionAfterRight()
                elif q4R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 5:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 24, 29):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q5R = input("Choose an answer.")
                q5R = q5R.upper()
                if q5R == q15HA:
                    actionAfterRight()

                elif q5R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 6:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 30, 35):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q6R = input("Choose an answer.")
                q6R = q6R.upper()
                if q6R == q6HA:
                    actionAfterRight()
                elif q6R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 7:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 36, 40):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q7R = input("Choose an answer.")
                q7R = q7R.upper()
                if q7R == q7HA:
                    actionAfterRight()
                elif q7R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 8:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 41, 46):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q8R = input("Choose an answer.")
                q8R = q8R.upper()
                if q8R == q8HA:
                    actionAfterRight()
                elif q8R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 9:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 47, 52):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q9R = input("Choose an answer.")
                q9R = q9R.upper()
                if q9R == q9HA:
                        actionAfterRight()
                elif q9R not in options:
                        print("Enter a valid input.")
                        continue
                else:
                        actionAfterWrong()

        if questionNumber == 10:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 53, 58):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q10R = input("Choose an answer.")
                q10R = q10R.upper()
                if q10R == q10HA:
                        actionAfterRight()
                elif q10R not in options:
                        print("Enter a valid input.")
                        continue
                else:
                        actionAfterWrong()
        if questionNumber == 11:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 59, 62):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q11R = input("Choose an answer.")
                q11R = q11R.upper()
                if q11R == q11HA:
                        actionAfterRight()
                elif q11R not in options:
                        print("Enter a valid input.")
                        continue
                else:
                        actionAfterWrong()

        if questionNumber == 12:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 63, 68):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q12R = input("Choose an answer.")
                q12R = q12R.upper()
                if q12R == q12HA:
                        actionAfterRight()
                elif q12R not in options:
                        print("Enter a valid")
                        continue
                else:
                        actionAfterWrong()

        if questionNumber == 13:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 69, 74):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q13R = input("Choose an answer.")
                q13R = q13R.upper()
                if q13R == q13HA:
                    actionAfterRight()
                elif q13R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 14:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 75, 80):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q14R = input("Choose an answer.")
                q14R = q14R.upper()
                if q14R == q14HA:
                    actionAfterRight()
                elif q14R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()

        if questionNumber == 15:
            with open("quizHard.txt", "r") as text_file_hard:
                for line in itertools.islice(text_file_hard, 81, 86):
                    cleanedLine = line.strip()
                    print(cleanedLine)

                print("\n")
                q15R = input("Choose an answer.")
                q15R = q15R.upper()
                if q15R in options:
                    actionAfterRight()
                    print("Congratulation on completing the quiz with the score of:", playerScore, ".")
                    print("You chose the difficulty:", playerDifficulty, "and got", playerWrongCount, "incorrect response(s).")
                    w = open("quizHardResult.txt","a")
                    w.write("\n")
                    w.write("Player name: ")
                    w.write(str(playerName))
                    w.write("\n")
                    w.write("Difficulty: ")
                    w.write(str(playerDifficulty))
                    w.write("\n")
                    w.write("Points: ")
                    w.write(str(playerScore))
                    w.write("\n")
                    w.write("Wrong answers: ")
                    w.write(str(playerWrongCount))
                    w.write("\n")
                    w.close()
                    break
                elif q15R not in options:
                    print("Enter a valid input.")
                    continue
                else:
                    actionAfterWrong()
                    print("Congratulation on completing the quiz with the score of:", playerScore, ".")
                    print("You chose the difficulty:", playerDifficulty, "and got", playerWrongCount, "incorrect response(s).")
                    w = open("quizHardResult.txt","a")
                    w.write("\n")
                    w.write("Player name: ")
                    w.write(str(playerName))
                    w.write("\n")
                    w.write("Difficulty: ")
                    w.write(str(playerDifficulty))
                    w.write("\n")
                    w.write("Points: ")
                    w.write(str(playerScore))
                    w.write("\n")
                    w.write("Wrong answers: ")
                    w.write(str(playerWrongCount))
                    w.write("\n")
                    w.close()
                    break
#----------------------------------------------------------------
#Answer for all easy questions
q1EA = "D"
q2EA = "A"
q3EA = "B"
q4EA = "D"
q5EA = "A"
q6EA = "D"
q7EA = "A"
q8EA = "B"
q9EA = "D"
q10EA = "C"
q11EA = "B"
q12EA = "A"
q13EA = "A"
q14EA = "D"
q15EA = "A" or "B" or "C" or "D"
#Answer for all hard questions
q1HA = "A"
q2HA = "C"
q3HA = "A"
q4HA = "B"
q5HA = "A"
q6HA = "B"
q7HA = "C"
q8HA = "D"
q9HA = "A"
q10HA = "B"
q11HA = "B"
q12HA = "D"
q13HA = "B"
q14HA = "B"
q15HA = "A" or "B" or "C" or "D"
#-----------------------------------------------------------------
##Running the quiz
import time
import itertools

from datetime import datetime
now = datetime.now()
print('%s/%s/%s %s:%s:%s'% (now.day, now.month, now.year, now.hour, now.minute, now.second))

playerName = input("Please enter your name.")
print("Welcome to the quiz!", playerName, "!", "There are 7 topics:", topicsList)
time.sleep(2)
print("""And there are 15 questions from those topics above and they are chosen at random depending on the difficulty you choose.""")
print("You will receive 1 point for each correct answer.")
print("""\n
Please wait for a few seconds to enter an answer after a problem is displayed, typing during the process of
displaying a problem might result in an incomplete problem or even recognized as an answer to a different answer by the
console. """)


loop = 1
while loop < 5:
    print("\n")
    playerDifficulty = input("Please choose your difficulty: Easy or Hard.")
    playerDifficulty = playerDifficulty.lower()
    if playerDifficulty == "easy":
        print("You chose to do the Easy quiz, which will start now.")
        time.sleep(2)
        easyQuiz()
        break

    elif playerDifficulty == "hard":
        print("You chose to do the Hard quiz, which will start now.")
        time.sleep(2)
        hardQuiz()
        break

    else:
        print("Choose a valid input(Easy or Hard).")
        continue
