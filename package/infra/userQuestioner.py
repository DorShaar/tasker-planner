import json
import logging
import sys
from domain.stringReplacer import StringReplacer

class UserQuestioner:
    def __init__(self):
        self.stringReplacer = StringReplacer()
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

    def askQuestions(self, question: str):
        self.lastQuestion = question
        formattedQuestion = self.stringReplacer.replaceString(question, self.stateDict)
        self.userInput = input(f"{formattedQuestion}\n")

    def checkAllowedAnswers(self, allowedAnswers):
        if self.userInput in allowedAnswers:
            return
        
        logging.debug('%s is not an expected answer', self.userInput)
        self.askQuestions(self.lastQuestion)
        self.checkAllowedAnswers(allowedAnswers)

    def setVariableName(self, variableName):
        self.stateDict[variableName] = self.userInput

    def handlePredicat(self, predicat):
        predicateParameter = predicat["predicatParameter"]
        print (predicateParameter)
        for key in predicat:
            print(key)

    def askQuestionsFromJson(self):
        jsonFile = open('plan.json')
        jsonData = json.load(jsonFile)
        
        for planSection in jsonData['plan']:
            for key in planSection:
                if self.userInput in self.exitInputs:
                    return

                if key == "question":
                    self.askQuestions(planSection[key])

                if key == "allowedAnswers":
                    self.checkAllowedAnswers(planSection[key])

                if key == "variableName":
                    self.setVariableName(planSection[key])

                if key == "predicat":
                    self.handlePredicat(planSection[key])
        
        jsonFile.close()