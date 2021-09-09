import json
import logging

class UserQuestioner:
    def __init__(self, stringReplacer):
        self.stringReplacer = stringReplacer
        self.stateDict = {}
        self.lastQuestion = ""
        self.userInput = ""
        self.exitInputs = {
            "q" : "exit",
            "exit" : "exit"
        }
        self.yesNoInputs = {
            "yes" : "yes",
            "y" : "yes",
            "no": "no",
            "n": "no"
        }

    def __askQuestion(self, question: str):
        self.lastQuestion = question
        formattedQuestion = self.stringReplacer.replaceString(question, self.stateDict)
        self.userInput = input(f"{formattedQuestion}\n")

    def __checkAllowedAnswers(self, allowedAnswers):
        if self.userInput in allowedAnswers:
            if isinstance(allowedAnswers, dict):
                logging.debug('User input "%s" is mapped to "%s" according to allowed answers', self.userInput, allowedAnswers[self.userInput])
                self.userInput = allowedAnswers[self.userInput]

            return
        
        logging.debug('%s is not an expected answer', self.userInput)
        self.__askQuestion(self.lastQuestion)
        self.__checkAllowedAnswers(allowedAnswers)

    def __checkAnswerRange(self, allowedAnswerRange):
        minValue = int(allowedAnswerRange[0])
        maxValue = int(allowedAnswerRange[1])

        try:
            userInputInteger = int(self.userInput)
            if userInputInteger in range(minValue, maxValue+1):
                return        

            logging.debug('%s is not in range %d - %d', self.userInput, minValue, maxValue)
            self.__askQuestion(self.lastQuestion)
            self.__checkAnswerRange(allowedAnswerRange)

        except Exception:
            logging.debug('%s is not an integer', self.userInput)
            self.__askQuestion(self.lastQuestion)
            self.__checkAnswerRange(allowedAnswerRange)

    def __checkYesAndNoAnswers(self, isYesNoAnswersEnabled):
        if isYesNoAnswersEnabled:
            if self.userInput in self.yesNoInputs:
                logging.debug('User input "%s" is mapped to "%s" according to "yes and no answers"', self.userInput, self.yesNoInputs[self.userInput])
                self.userInput = self.yesNoInputs[self.userInput]
                return
            
            logging.debug('%s is not an expected answer', self.userInput)
            self.__askQuestion(self.lastQuestion)
            self.__checkYesAndNoAnswers(isYesNoAnswersEnabled)
                

    def __setVariableName(self, variableName):
        logging.debug('Added key "%s" with value "%s" to state dictionary', variableName, self.userInput)
        self.stateDict[variableName] = self.userInput

    def __handlePredicat(self, predicat):
        predicateParameter = predicat["predicatParameter"]
        predicateParameterValue = self.stateDict[predicateParameter]
        if predicateParameterValue in predicat["predicatCases"]:
            section = predicat["predicatCases"][predicateParameterValue]
            for sectionKey in section:
                self.__handlePlanSectionByKey(section, sectionKey)

    def __handlePlanSectionByKey(self, planSection, key):
        if self.userInput in self.exitInputs:
            return

        try:
            if key == "question":
                self.__askQuestion(planSection[key])

            elif key == "allowedAnswers":
                self.__checkAllowedAnswers(planSection[key])

            elif key == "answerRange":
                self.__checkAnswerRange(planSection[key])

            elif key == "yesNoAnswers":
                self.__checkYesAndNoAnswers(planSection[key])

            elif key == "variableName":
                self.__setVariableName(planSection[key])

            elif key == "predicat":
                self.__handlePredicat(planSection[key])

            else:
                logging.error('Unexpected key: %s', key)

        except Exception as ex:
            logging.error('Exception raised during handling key "%s": %s', key, str(ex))

    def askQuestionsFromJsonFile(self, fileName: str):
        jsonFile = open(fileName)
        jsonData = json.load(jsonFile)
        
        for planSection in jsonData['plan']:
            for key in planSection:
                self.__handlePlanSectionByKey(planSection, key)
        
        jsonFile.close()
        return self.stateDict

    def editPlan(self):
        for key, value in self.stateDict.items():
            logging.debug('%s: %s', key, value)

        self.userInput = input("Which key would you like to edit?\n")
        if self.userInput not in self.stateDict:
            logging.debug('Key "%s" does not exist', self.userInput)
            return

        key = self.userInput
        self.userInput = input("Please type your changes\n")
        self.stateDict[key] = self.userInput
        logging.debug('Replaced key "%s" with new value: "%s"', key, self.stateDict[key])