import json
import logging
import os
from package.domain.consts import getPlansDirectory
from typing import Dict

class FileSaver:
    def savePlan(self, stateDict: Dict):
        fileName = stateDict["taskName"]
        fileName = fileName.replace(" ", "_").lower()
        filePath = os.path.join(getPlansDirectory(), fileName)

        if os.path.isfile(filePath):
            logging.warning("File %s already exist", filePath)
            return

        json_object = json.dumps(stateDict, indent = 4)
        file = open(filePath, "a")
        file.write(json_object)
        file.close()

        logging.debug("Plan %s saved into %s", fileName, filePath)