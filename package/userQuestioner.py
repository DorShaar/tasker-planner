class UserQuestioner:
    def __init__(self):  
        self.shouldExit = False
        self.exitInputs = {
            "q" : "exit",
            "exit" : "exit"
        }
        self.yesInputs = {
            "yes" : "yes",
            "y" : "yes",
        }

    def checkIfUserChoseToExit(self, userInput: str):
        if userInput in self.exitInputs:
            self.shouldExit = True

    def askTaskTypeInput(self) -> str:
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

        self.checkIfUserChoseToExit(userInput)

        return allowedInputs[userInput]

    def askUserExperienceInput(self, taskType: str) -> str:
        question = ""
        if taskType == "feature":
            question = "How will the user affected?"
        elif taskType == "bug":
            question = "How is the user affected?"

        userInput = input(f"{question}\n")

        self.checkIfUserChoseToExit(userInput)

        return userInput

    def askForTaskName(self) -> str:
        return input(f"What is the task name?\n")

    def askForAnalytics(self, taskName: str) -> int:
        userInput = input(f"Does '{taskName}' requires analytics?\n")
        if userInput.lower() not in self.yesInputs:
            return -1

        userInput = input(f"Does '{taskName}' has analytics?\n")
        if userInput.lower() in self.yesInputs:
            return -1

        userInput = input(f"How much analytics work is requires for task'{taskName}'?\n")
        return userInput