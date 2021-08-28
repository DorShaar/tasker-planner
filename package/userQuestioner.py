class UserQuestioner:
    def __init__(self):  
        self.shouldExit = False
        self.exitInputs = {
            "q" : "exit",
            "exit" : "exit"
        }

    def getTaskTypeInput(self) -> str:
        userInput = input("Is it bug or a feature?\n")
        userInput = userInput.lower()

        allowedInputs = {
            "bug" : "bug",
            "b" : "bug",
            "feature" : "feature",
            "f" : "feature",
        }

        allowedInputs.update(self.exitInputs)

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

        userInput = input(f"{question}\n")

        if userInput in self.exitInputs:
            self.shouldExit = True

        return userInput