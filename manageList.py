import savefile
from task import Task

class ManageList:
    def __init__(self):
        if savefile.fileExists():
            self.data = savefile.loadFromMemory()
        else:
            savefile.createFile()
            self.data = savefile.loadFromMemory()
    
    def save(self):
        savefile.saveToMemory(self.data)

    def getTasks(self):
        print("getTasks")      
        for Course in self.data:
            if (len(self.data[Course]) == 0):
                print("{} has no tasks.".format(Course))
            for task in self.data[Course]:
                print("{} |id: {} | {}".format(Course, task.getId(),task.getName()))

    def completeTask(self):
        print("CompleteTask")
 
    def addTask(self, CourseTaskDeadline):
        print("Add task")
        
        if CourseTaskDeadline[0] in self.data:
            task = Task(CourseTaskDeadline[1],CourseTaskDeadline[0]+ ":" + str(len(self.data[CourseTaskDeadline[0]])+1) ,  CourseTaskDeadline[2])
            self.data[CourseTaskDeadline[0]].append(task)
            return True
        else:
            return False
    
    def addCourse(self, course):
        print("Add course")
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
 
