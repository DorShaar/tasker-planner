import unittest
from package.infra.domain.fileSaver import FileSaver

class TestFileSaver(unittest.TestCase):

    def test_loadPlan_planIsLoaded(self):
        fileSaver = FileSaver()
        dict = fileSaver.loadPlan("tests/domain/test_files/add_more_logs")

        assert dict["dod"] == "80% of the methods will have logs"
        assert dict["shouldPresentDoneWork"] == "no"
        assert len(dict) == 13