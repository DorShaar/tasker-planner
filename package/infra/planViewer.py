import logging
import os
from infra.domain.consts import getPlansDirectory
from infra.domain.fileSaver import FileSaver

class PlanViewer:

    def __init__(self, fileSaver: FileSaver):
        self.fileSaver = fileSaver

    def showPlanInformation(self, planName: str):
        planPath = os.path.join(getPlansDirectory(), planName)
        planDict = self.fileSaver.loadPlan(planPath)

        for key, value in planDict.items():
            logging.debug('%s: %s', key, value)

    def showPlanTiming(self, planName: str):
        totalTimeRequired = 0
        planPath = os.path.join(getPlansDirectory(), planName)
        planDict = self.fileSaver.loadPlan(planPath)

        for key, value in planDict.items():
            if key.find("Time") > 0:
                totalTimeRequired += int(value)
                logging.debug('%s: %s', key, value)

        logging.debug('Total time required: %d', totalTimeRequired)