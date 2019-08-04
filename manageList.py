import savefile
from task import Task


class ManageList:
    # Load file previous todolist from memory or create it.
    # The loaded file is a dict. Key is courseID and results is
    # a list of task objects
    def __init__(self):
        if savefile.fileExists():
            self.data = savefile.loadFromMemory()
        else:
            savefile.createFile()
            self.data = savefile.loadFromMemory()

    # Save data to memory
    def save(self):
        savefile.saveToMemory(self.data)

    # Print tasks that are in the todolist
    def getTasks(self):
        lines_names = ["Course", "Name", "Deadline", "ID"]
        print("{: ^10} | {: ^35} | {: ^13} | {: ^3}".format(*lines_names))
        for Course in self.data:
            if (len(self.data[Course]) == 0):
                print("{} has no tasks.".format(Course))
            for task in self.data[Course]:
                print(
                    "{: ^10} | {: ^35} | {: ^13} | {: ^3}".format(
                                                        Course,
                                                        task.getName(),
                                                        task.getDeadline(),
                                                        task.getId()
                                                       )
                )

    # Complete the given task with course name and task number
    def completeTask(self, courseId):
        print("CompleteTask")
        if courseId[0] in self.data:
            i = int(courseId[1]) - 1
            self.data[courseId[0]].remove(self.data[courseId[0]][i])
            print("Completed given task.")
            return True
        else:
            print("No such course or tasknumber.")
            return False

    # Add a course with to given course with "task" as description
    #   and given deadline
    def addTask(self, taskDeadline):
        print("Which course to add task to")
        i = 1
        for course in self.data:
            print("{} | {}".format(i, course))
            i = i + 1

        while True:
            number = int(input("\t:"))
            if 0 < number <= len(self.data):
                break

        courseName = list(self.data.keys())[number-1]

        task = Task(
                    taskDeadline[0],
                    str(len(self.data[courseName])+1),
                    taskDeadline[1]
                )
        self.data[courseName].append(task)

        print("Successfully added new task \"{}\" ({})".format(

                                                            taskDeadline[0],
                                                            taskDeadline[1]
                                                        ))

    # Complete the given task
    def doTask(self, courseIdNumber):
        if courseIdNumber[0] in self.data:
            if courseIdNumber[1] in self.data[courseIdNumber[0]]:
                self.data[courseIdNumber[0]].remove(courseIdNumber[1])
                return True
            else:
                return False
        else:
            return False

    # Adds a new course to the dict
    def addCourse(self, course):
        if (len(self.data) == 0):
            self.data = dict()

        if course in self.data:
            print("Course already in todolist.")
            return False
        else:
            self.data[course] = []
            print("Successfully added", course)
            return True

    def removeCourse(self, course):
        if course in self.data:
            self.data.pop(course)
            print("Removed course \"{}\" and all it's tasks".format(course))
        else:
            print("No such course")

    def getTaskByCourse(self, course):
        print("Get Task By course")

    def getTaskByPriority(self):
        print("Get task by priority")
