import pickle
import os

fileName=os.path.join(os.path.os.path.expanduser('~'), ".todo_lists.txt")

def fileExists():
    if os.path.isfile(fileName):
        return True
    else:
        return False

# Load the list from memory
def loadFromMemory(self):
    if fileExists():
        file = open(self.__fileName, "rb")
        list = pickle.load(file)
        file.close()
        return list
    else:
        raise Exception("Todolist file doesn't exist.")

# Save the list to memory
def saveToMemory(self, list):
    if fileExists():
        file = open(self.__fileName, "wb")
        pickle.dump(list, file)
        file.close()        
    else:
        raise Exception("Todolist file doesn't exist.")
