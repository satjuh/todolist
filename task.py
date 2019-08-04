class Task:
    def __init__(self, name, id, deadline):
        self.description = "No description yet"
        self.id = id
        self.deadline = deadline
        self.name = name

    def getDescription(self):
        return self.description

    # Task id is
    def getId(self):
        return self.id

    def getDeadline(self):
        return self.deadline

    def getName(self):
        return self.name
