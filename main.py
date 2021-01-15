#import SenseHat_TicTacToe
#import SenseHat_Clear
import importlib

def printActivityList():
    activityList = ["1: Tic Tac Toe \n2: Get Temperature"];
    print("Here's all the stuff I can do:")
    for activity in range(len(activityList)):
        print(activityList[activity])
        
while True:
    printActivityList()
    activity = input("What do you want to do: ")

    if activity == 1:
        print("Tic Tac Toe it is!")
        print("Let me know when you are done by pressing Ctrl+c")
        importlib.import_module('SenseHat_TicTacToe')
        print("That was fun! What else do you want to do?")
        
    elif activity == 2:
        importlib.import_module('SenseHat_GetTemperature')
        






