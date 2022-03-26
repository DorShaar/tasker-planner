import unittest
from package.domain.stringReplacer import StringReplacer


class TestUserQuestioner(unittest.TestCase):

    def test_replaceString_normalCase_Equal(self):
        string = "Is '{taskName}' is well defined? Is '{taskType}' is bug or feature?"
        variablesDict = { 
            "taskName": "Clean all backlog",
            "taskType": "feature"
        }

        stringReplacer = StringReplacer()
        replacedString = stringReplacer.replaceString(string, variablesDict)

        self.assertEqual("Is 'Clean all backlog' is well defined? Is 'feature' is bug or feature?", replacedString)

    def test_replaceString_abnormalCase_OnlyOneIsReplaced(self):
        string = "Is '{taskName}' is well defined? Is '{taskType' is bug or feature?"
        variablesDict = { 
            "taskName": "Clean all backlog",
            "taskType": "feature"
        }

        stringReplacer = StringReplacer()
        replacedString = stringReplacer.replaceString(string, variablesDict)

        self.assertEqual("Is 'Clean all backlog' is well defined? Is '{taskType' is bug or feature?",  replacedString)
