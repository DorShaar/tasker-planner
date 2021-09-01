import json

class UserQuestioner:
    def __init__(self):
        self.stateDict = [],
        self.shouldExit = False
        self.exitInputs = {
            "q" : "exit",
            "exit" : "exit"
        }
        self.yesInputs = {
            "yes" : "yes",
            "y" : "yes",
        }

    def replaceString(self, string: str) -> str:
        return string # TODO # Also add logs

    def askQuestions(self, question: str) -> str:
        userInput = input(question)
        self.stateDict[question] = userInput

    def askQuestionsFromJson(self):
        jsonFile = open('plan.json')
        jsonData = json.load(jsonFile)
        
        for planSection in jsonData['plan']:
            for key in planSection:
                if key == "question":
                    self.askQuestions(planSection[key])
                

                #         print (planSection[key])
                # elif key == "allowedAnswers":
                #     print (planSection[key])

        # for majorkey, subdict in jsonData.items():
            # print (section)
            # print (subdict)
            # for subkey, value in subdict.items():
            #         print (subkey, value)
        
        jsonFile.close()



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