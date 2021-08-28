import unittest
from unittest import mock
from package.userQuestioner import UserQuestioner

class TestUserQuestioner(unittest.TestCase):

    @mock.patch('package.userQuestioner.input', return_value='q')
    def test_getTaskTypeInput_exitInput(self, mocked_input):
        userQuestioner = UserQuestioner()

        assert not userQuestioner.shouldExit

        taskTypeInput = userQuestioner.getTaskTypeInput()
        self.assertEqual(taskTypeInput, "exit")

        assert userQuestioner.shouldExit

    @mock.patch('package.userQuestioner.input', return_value='Bug')
    def test_getTaskTypeInput_bugInpug(self, mocked_input):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.getTaskTypeInput()
        self.assertEqual(taskTypeInput, "bug")

    @mock.patch('package.userQuestioner.input', return_value='f')
    def test_getTaskTypeInput_featureInpug(self, mocked_input):
        userQuestioner = UserQuestioner()

        taskTypeInput = userQuestioner.getTaskTypeInput()
        self.assertEqual(taskTypeInput, "feature")

if __name__ == '__main__':
    unittest.main()