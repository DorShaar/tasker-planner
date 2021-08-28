class UserQuestioner:
    def __init__(self):  
        self.shouldExit = False  

    def getTaskTypeInput(self) -> str:
        userInput = input("Is it bug or a feature?\n")
        userInput = userInput.lower()

        allowedInputs = {
            "bug" : "bug",
            "b" : "bug",
            "feature" : "feature",
            "f" : "feature",
            "q" : "exit",
            "exit" : "exit"
        }

        while userInput not in allowedInputs:
            userInput = input(f"\'{userInput}\' is invalid. Is it bug or a feature?\n")

        if allowedInputs[userInput] == "exit":
            self.shouldExit = True
            return ""

        return allowedInputs[userInput]

    def get_bug_or_feature_input(self, taskType: str) -> str:
        question = ""
        if taskType == "feature":
            question = "How will the user affected?"
        elif taskType == "bug":
            question = "How is the user affected?"

        return input(f"{question}\n")