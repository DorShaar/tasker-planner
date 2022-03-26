import unittest
from package.domain.fileSaver import FileSaver


class TestFileSaver(unittest.TestCase):
    def test_loadPlan_planIsLoaded(self):
        fileSaver = FileSaver()
        dict = fileSaver.loadPlan("tests/domain/test_files/add_more_logs")

        self.assertEqual("80% of the methods will have logs", dict["dod"])
        assert dict["shouldPresentDoneWork"] == "no"
        assert len(dict) == 13
