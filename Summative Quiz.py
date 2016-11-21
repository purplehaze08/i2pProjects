##Variable area
topicsList =["Animals", "Video games", "Memes", "Languages", "Science", "Music"]
playerScore = 0

def easyQuiz():
    q1E = input("")


def hardQuiz():
    print("asdf")

##Running the quiz
import time
playerName = input("Please enter your name.")
print("Welcome to the quiz!", playerName, "There are 6 topics:", topicsList)
time.sleep(2)
print("""And there are 20 questions from those topics above and they are chosen at random depending on the difficulty you choose.""")


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
