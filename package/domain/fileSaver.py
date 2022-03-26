import json
import logging
import os
from typing import Dict
from package.domain.settings import Settings


class FileSaver:

    def __init__(self):
        pass

    @staticmethod
    def savePlan(stateDict: Dict):
        settings = Settings()

        if "taskName" not in stateDict:
            logging.debug("Not saving since no task name was given")
            return

        fileName = stateDict["taskName"]
        fileName = fileName.replace(" ", "_").lower()
        filePath = os.path.join(settings.getPlansDirectory(), fileName)

        if os.path.isfile(filePath):
            logging.debug("Overwriting %s", filePath)

        json_object = json.dumps(stateDict, indent=4)
        file = open(filePath, "w")
        file.write(json_object)
        file.close()

        logging.debug("Plan %s saved into %s", fileName, filePath)

    @staticmethod
    def loadPlan(planPath: str) -> Dict:
        with open(planPath) as jsonFile:
            logging.debug("Loaded %s", planPath)
            return json.load(jsonFile)
