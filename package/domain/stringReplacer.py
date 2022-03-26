import re as regex


class StringReplacer:
    def __init__(self):
        pass

    @staticmethod
    def getAllShouldBeReplacedStrings(string: str):
        stringsToReplace = []

        startWordsReplacer = []
        endWordsReplacer = []
        for match in regex.finditer('{', string):
            startWordsReplacer.append(match.start())

        for match in regex.finditer('}', string):
            endWordsReplacer.append(match.start())

        iterationLength = min(len(startWordsReplacer), len(endWordsReplacer))
        
        for i in range(0, iterationLength):
            substringToReplace = string[startWordsReplacer[i]:endWordsReplacer[i]+1]
            stringsToReplace.append(substringToReplace)

        return stringsToReplace
    
    def replaceString(self, string: str, variablesDict) -> str:
        replacedString = string
        stringsToReplace = self.getAllShouldBeReplacedStrings(string)

        for stringToReplace in stringsToReplace:
            variableName = stringToReplace.replace('{', '').replace('}', '')
            if variableName in variablesDict:
                replacedString = replacedString.replace(stringToReplace, variablesDict[variableName])

        return replacedString
