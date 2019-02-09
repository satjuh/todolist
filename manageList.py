import savefile

class ManageList:
    def __init__(self):
        if savefile.fileExists():
            self.__data = savefile.loadFromMemory()
        else:
            raise Exception("Failed to load lists from memory.")
    
    def __del__(self):
        savefile.saveToMemory(self.__data)

    def getTasks(self):
        print("getTasks")      

    def completeTask(self):
        print("CompleteTasks")
    
    def addTask(self):
        print("Add task")

    def getTaskByCourse(self):
        print("Get Task By course")

    def getTaskByPriority(self):
        print("Get task by priority")
 
