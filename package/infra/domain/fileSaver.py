import json
import logging
import os
from typing import Dict
from .consts import getPlansDirectory

class FileSaver:

    def savePlan(self, stateDict: Dict):
        if "taskName" not in stateDict:
            logging.debug("Not saving since no task name was given")
            return

        fileName = stateDict["taskName"]
        fileName = fileName.replace(" ", "_").lower()
        filePath = os.path.join(getPlansDirectory(), fileName)

        if os.path.isfile(filePath):
            logging.debug("Overwritting %s", filePath)

        json_object = json.dumps(stateDict, indent = 4)
        file = open(filePath, "w")
        file.write(json_object)
        file.close()

        logging.debug("Plan %s saved into %s", fileName, filePath)

    def loadPlan(self, planPath: str) -> Dict:
        with open(planPath) as jsonFile:
            logging.debug("Loaded %s", planPath)
            return json.load(jsonFile)