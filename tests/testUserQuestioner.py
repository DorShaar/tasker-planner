import unittest
from unittest import mock
from unittest.mock import Mock
from package.userQuestioner import UserQuestioner

class TestUserQuestioner(unittest.TestCase):

    @mock.patch('package.userQuestioner.input', return_value='q')
    def test_askTaskTypeInput_exitInput(self, mocked_input):
        userQuestioner = UserQuestioner()

        assert not userQuestioner.shouldExit

        taskTypeInput = userQuestioner.askTaskTypeInput()
        self.assertEqual(taskTypeInput, "exit")

        assert userQuestioner.shouldExit

    @mock.patch('package.userQuestioner.input', return_value='Bug')
    def test_askTaskTypeInput_bugInput(self, mocked_input):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.askTaskTypeInput()
        self.assertEqual(taskTypeInput, "bug")

    @mock.patch('package.userQuestioner.input', return_value='f')
    def test_askTaskTypeInput_featureInput(self, mocked_input):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.askTaskTypeInput()
        self.assertEqual(taskTypeInput, "feature")

    mocked_input = Mock()
    mocked_input.side_effect = ["kuku", "feature",]
    @mock.patch('package.userQuestioner.input', return_value='f')
    def test_askTaskTypeInput_wrongFirstInput_featureSecondInput(self, mocked_input):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.askTaskTypeInput()
        self.assertEqual(taskTypeInput, "feature")

    input_mock = Mock()
    input_mock.side_effect = ["yes", "no", 7]
    @mock.patch('package.userQuestioner.input', input_mock)
    def test_askForAnalytics_shouldPlanAnalytics_returnsExpectedNumber(self):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.askForAnalytics('taskName')
        self.assertEqual(taskTypeInput, 7)

if __name__ == '__main__':
    unittest.main()