import logging
from typing import Dict

class PlanViewer:

    def __init__(self, planDict: Dict):
        self.planDict = planDict

    def showPlanInformation(self):
        for key, value in self.planDict.items():
            logging.debug('%s: %s', key, value)

    def showPlanTiming(self):
        totalTimeRequired = 0

        for key, value in self.planDict.items():
            if key.find("Time"):
                totalTimeRequired += int(value)
                logging.debug('%s: %s', key, value)

        logging.debug('Total time required: %d', totalTimeRequired)