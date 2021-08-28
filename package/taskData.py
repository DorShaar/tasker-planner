class TaskData:
    def __init__(self, type: str, name: str):  
        self.type = type
        self.name = name
        self.relatedTask = ""
        self.effectDescription = ""
        self.subTasks = []