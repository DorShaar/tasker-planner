import unittest
from unittest import mock
from unittest.mock import Mock
from package.domain.stringReplacer import StringReplacer
from package.infra.userQuestioner import UserQuestioner

class TestUserQuestioner(unittest.TestCase):

    input_mock = Mock()
    input_mock.side_effect = [
        "k", "b",
        "Pdf null reference exception",
        "blocked file",
        "file will not be blocked",
        "j", "y",
        "-5", "3",
        "2",
        "y",
        "3",
        "yes",
        "10.1.5.3",
        "10",
        "n",
        "1",
        "5",
        "2",
        "no"
        ]
    @mock.patch('package.infra.userQuestioner.input', input_mock)
    def test_askQuestionsFromJsonFile_bug_asExpected(self):
        stringReplacer = StringReplacer()

        userQuestioner = UserQuestioner(stringReplacer)

        planDict = userQuestioner.askQuestionsFromJsonFile('plan.json')
        value = planDict.pop("taskType")
        self.assertEqual("bug", value)

        value = planDict.pop("taskName")
        self.assertEqual("Pdf null reference exception", value)

        value = planDict.pop("userExperience")
        self.assertEqual("blocked file", value)

        value = planDict.pop("dod")
        self.assertEqual("file will not be blocked", value)

        value = planDict.pop("requiresLearning")
        self.assertEqual("yes", value)

        value = planDict.pop("learningTime")
        self.assertEqual("3", value)

        value = planDict.pop("knowledgeSharingTime")
        self.assertEqual("2", value)

        value = planDict.pop("requiresAnalytics")
        self.assertEqual("yes", value)

        value = planDict.pop("analyticsTime")
        self.assertEqual("3", value)

        value = planDict.pop("isTaskShouldBeForSpecificVersion")
        self.assertEqual("yes", value)

        value = planDict.pop("clientVersion")
        self.assertEqual("10.1.5.3", value)

        value = planDict.pop("testOnSpecificVersionTime")
        self.assertEqual("10", value)

        value = planDict.pop("shouldCollectSamples")
        self.assertEqual("no", value)

        value = planDict.pop("reproduceTime")
        self.assertEqual("1", value)

        value = planDict.pop("writingTestsTime")
        self.assertEqual("5", value)

        value = planDict.pop("qaSyncTime")
        self.assertEqual("2", value)

        value = planDict.pop("shouldPresentDoneWork")
        self.assertEqual("no", value)

        print(planDict)
        self.assertEqual(0, len(planDict))

    input_mock = Mock()
    input_mock.side_effect = [
        "k", "f",
        "Add more logs",
        "User will be able to know where failure has happend",
        "80% of the methods will have logs",
        "j", "n",
        "y",
        "1",
        "n",
        "y",
        "2",
        "5",
        "y",
        "2",
        "no"
        ]
    @mock.patch('package.infra.userQuestioner.input', input_mock)
    def test_askQuestionsFromJsonFile_feature_asExpected(self):
        stringReplacer = StringReplacer()

        userQuestioner = UserQuestioner(stringReplacer)

        planDict = userQuestioner.askQuestionsFromJsonFile('plan.json')
        value = planDict.pop("taskType")
        self.assertEqual("feature", value)

        value = planDict.pop("taskName")
        self.assertEqual("Add more logs", value)

        value = planDict.pop("userExperience")
        self.assertEqual("User will be able to know where failure has happend", value)

        value = planDict.pop("dod")
        self.assertEqual("80% of the methods will have logs", value)

        value = planDict.pop("requiresLearning")
        self.assertEqual("no", value)

        value = planDict.pop("requiresAnalytics")
        self.assertEqual("yes", value)

        value = planDict.pop("analyticsTime")
        self.assertEqual("1", value)

        value = planDict.pop("isTaskShouldBeForSpecificVersion")
        self.assertEqual("no", value)

        value = planDict.pop("shouldCollectSamples")
        self.assertEqual("yes", value)

        value = planDict.pop("collectSamplesTime")
        self.assertEqual("2", value)
        
        value = planDict.pop("writingTestsTime")
        self.assertEqual("5", value)

        value = planDict.pop("qaSyncTime")
        self.assertEqual("2", value)

        value = planDict.pop("shouldPresentDoneWork")
        self.assertEqual("no", value)

        print(planDict)
        self.assertEqual(0, len(planDict))

if __name__ == '__main__':
    unittest.main()