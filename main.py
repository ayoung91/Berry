#import SenseHat_TicTacToe
#import SenseHat_Clear
from SenseHat_TicTacToe import RunTicTacToe 
from SenseHat_GetTemperature import GetTemperature 

def printActivityList():
    activityList = ["1: Tic Tac Toe \n2: Get Temperature \n3: Quit"];
    print("Here's all the stuff I can do:")
    for activity in range(len(activityList)):
        print(activityList[activity])

while True:
    printActivityList()
    activity = input("What do you want to do: ")

    if activity == "1" or activity == 1:
        print("Tic Tac Toe it is!")
        print("Let me know when you are done by pressing Ctrl+c")
        RunTicTacToe()
        print("That was fun! What else do you want to do?")
        
    elif activity == "2" or activity == 2:
        GetTemperature()
    elif activity == "3" or activity == 3:
        print("K bye")
        exit()
        






