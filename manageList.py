import savefile
from task import Task

class ManageList:
    # Load file previous todolist from memory or create it. 
    # The loaded file is a dict. Key is courseID and results is a list of task objects
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
        for Course in self.data:
            if (len(self.data[Course]) == 0):
                print("{} has no tasks.".format(Course))
            for task in self.data[Course]:
                print("{} | task number: {} | {}".format(Course, task.getId(), task.getName()))

    # Complete the given task with course name and task number 
    def completeTask(self, courseId):
        print("CompleteTask")
        if courseId[0] in self.data:
            i = int(courseId[1]) - 1
            self.data[courseId[0]].remove(self.data[courseId[0]][i])
            return True
        else:
            return False


    def addTask(self, CourseTaskDeadline):
        if CourseTaskDeadline[0] in self.data:
            task = Task(CourseTaskDeadline[1], str(len(self.data[CourseTaskDeadline[0]])+1) ,  CourseTaskDeadline[2])
            self.data[CourseTaskDeadline[0]].append(task)
            return True
        else:
            return False
    
    def doTask(self, courseIdNumber):
        if courseIdNumber[0] in self.data:
            if courseIdNumber[1] in self.data[courseIdNumber[0]]:
                self.data[courseIdNumber[0]].remove(courseIdNumber[1])
                return True
            else:
                return False
        else:
            return False
                    
         
    def addCourse(self, course):
        if (len(self.data) == 0):
            self.data = dict()
            self.data[course]=[]
            return True
        else:
            if course in self.data:
                return False
            else:
                self.data[course]=[] 
                return True


    def getTaskByCourse(self, course):
        print("Get Task By course")

    def getTaskByPriority(self):
        print("Get task by priority")
 
