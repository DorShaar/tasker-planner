import logging
import os
from package.domain.fileSaver import FileSaver
from package.domain.settings import Settings


class PlanViewer:
    def __init__(self, fileSaver: FileSaver):
        self.fileSaver = fileSaver
        self.settings = Settings()

    def showPlanInformation(self, planName: str):
        planPath = os.path.join(self.settings.getPlansDirectory(), planName)
        planDict = self.fileSaver.loadPlan(planPath)

        for key, value in planDict.items():
            logging.debug(f'{key}: {value}')

    def showPlanTiming(self, planName: str):
        totalTimeRequired = 0
        planPath = os.path.join(self.settings.getPlansDirectory(), planName)
        planDict = self.fileSaver.loadPlan(planPath)

        for key, value in planDict.items():
            if key.find("Time") > 0:
                totalTimeRequired += int(value)
                logging.debug('%s: %s', key, value)

        logging.debug('Total time required: %d', totalTimeRequired)
