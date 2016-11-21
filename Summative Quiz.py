##Variable area
topicsList =["Animals", "Video games", "Memes", "Languages", "Science", "Music"]
playerScore = 0

def easyQuiz():
    #Local variable in easyQuiz
    q1E = input("")
    q1EA = ""
    q2E = input("")
    q2EA = ""
    q3E = input("")
    q3EA = ""
    q4E = input("")
    q4EA = ""
    q5E = input("")
    q5EA = ""
    q6E = input("")
    q6EA = ""
    q7E = input("")
    q7EA = ""
    q8E = input("")
    q8EA = ""
    q9E = input("")
    q9EA = ""
    q10E = input("")
    q10EA = ""
    q11E = input("")
    q11EA = ""
    q12E = input("")
    q12EA = ""
    q13E = input("")
    q13EA = ""
    q14E = input("")
    q14EA = ""
    q15E = input("")
    q15EA = ""
    sadf = 0
    while sadf == 0:
        q1E = input()

##open text file
#textfile = "Quiz.txt"
#file = open("Quiz.txt", "r")
#print file.read()

def hardQuiz():
    #Local variable in hardQuiz
    q1H = input("")
    q1HA = ""
    q2H = input("")
    q2HA = ""
    q3H = input("")
    q3HA = ""
    q4H = input("")
    q4HA = ""
    q5H = input("")
    q5HA = ""
    q6H = input("")
    q6HA = ""
    q7H = input("")
    q7HA = ""
    q8H = input("")
    q8HA = ""
    q9H = input("")
    q9HA = ""
    q10H = input("")
    q10HA = ""
    q11H = input("")
    q11HA = ""
    q12H = input("")
    q12HA = ""
    q13H = input("")
    q13HA = ""
    q14H = input("")
    q14HA = ""
    q15H = input("")
    q15HA = ""

##Running the quiz
import time
playerName = input("Please enter your name.")
print("Welcome to the quiz!", playerName, "There are 6 topics:", topicsList)
time.sleep(2)
print("""And there are 15 questions from those topics above and they are chosen at random depending on the difficulty you choose.""")
print("You will receive 1 point for each correct answer.")

playerDifficulty = input("Please choose your difficulty: Easy or Hard.")
playerDifficulty = playerDifficulty.lower()
loop = 1
while loop < 5:
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
        print("Choose a valid input(easy or hard).")
