import pickle
import os

fileName = os.path.join(os.path.os.path.expanduser('~'), ".todo_lists.txt")


def fileExists():
    if os.path.isfile(fileName):
        return True
    else:
        return False


def createFile():
    try:
        file = open(fileName, "x")
        file.close()
        return True
    except FileExistsError:
        return False


# Load the list from memory
def loadFromMemory():
    if fileExists():
        if os.path.getsize(fileName) > 0:
            file = open(fileName, "rb")
            list = pickle.load(file)
            file.close()
            return list
        else:
            return []


# Save the list to memory
def saveToMemory(list):
    if fileExists():
        file = open(fileName, "wb")
        pickle.dump(list, file)
        file.close()
        return True
    else:
        return False
