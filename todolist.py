#!/usr/bin/python3
from manageList import ManageList
from regex import checkDate
import parser


if __name__ == "__main__":
    options, args = parser.parse()
    manager = ManageList()

    if (options.dotask):
        manager.completeTask(options.dotask)
    elif(options.addcourse):
        manager.addCourse(options.addcourse)
    elif (options.addtask):
        if (checkDate(options.addtask[1])):
            manager.addTask(options.addtask)
        else:
            print(options.addtask)
            print("Wrong date format")

    elif(options.list):
        manager.getTasks()
    elif(options.remove_course):
        manager.removeCourse(options.remove_course)
    else:
        parser.help()
        print("\n")
        manager.getTasks()

    manager.save()
