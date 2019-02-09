#!/usr/bin/python3
from manageList import ManageList
from regex import checkDate 
import parser


if __name__ == "__main__":
    options, args = parser.parse()    
    manager = ManageList()

    if (options.dotask):
        manager.completeTask()
    elif(options.addcourse):
        if manager.addCourse(options.addcourse):
            print("Successfully added", options.addcourse)
        else:
            print("Course already in todolist")
    elif (options.addtask):
        if (checkDate(options.addtask[2])):
            if manager.addTask(options.addtask):
                print("Succesfully added")
            else:
                print("No course called {}.".format(options.addtask[0]))
        else:
            print(options.addtask)
            print("Wrong date format")
    elif (options.list):
        manager.getTasks()
    
    manager.save()
     
