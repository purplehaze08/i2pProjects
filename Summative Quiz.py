##Variable area
topicsList =["Animals", "Video games", "Memes", "Languages", "Science", "Music", "Technology"]
playerScore = 0
textfile = open("quizEasy.txt")
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

##open text file
#textfile = "Quiz.txt"
#file = open("Quiz.txt", "r")
#print(file.read(0,4))
#probably needs loop as the shell

#Answer for all hard questions
q1HA = ""
q2HA = ""
q3HA = ""
q4HA = ""
q5HA = ""
q6HA = ""
q7HA = ""
q8HA = ""
q9HA = ""
q10HA = ""
q11HA = ""
q12HA = ""
q13HA = ""
q14HA = ""
q15HA = ""

def easyQuiz():
    print("Welcome to the easy quiz!")
    global textfile
    for line in range(1,6):
        file = open(textfile, "r")
        print(file.read())


def hardQuiz():
    print("Welcome to the hard quiz!")
##Running the quiz
import time
from datetime import datetime
now = datetime.now()
print('%s/%s/%s %s:%s:%s'% (now.day, now.month, now.year, now.hour, now.minute, now.second))

playerName = input("Please enter your name.")
print("Welcome to the quiz!", playerName, "There are 7 topics:", topicsList)
time.sleep(2)
print("""And there are 15 questions from those topics above and they are chosen at random depending on the difficulty you choose.""")
print("You will receive 1 point for each correct answer.")


loop = 1
while loop < 5:
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

