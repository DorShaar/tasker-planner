import logging
import os
import sys
from package.domain.settings import Settings
from package.domain.stringReplacer import StringReplacer
from package.domain.fileSaver import FileSaver
from package.infra.userQuestioner import UserQuestioner
from package.infra.planViewer import PlanViewer
from package.infra.taskerPlannerMenu import TaskerPlannerMenu


def main():
    setLogger()
    settings = Settings()
    settings.copyFilesToMountedDirectory()

    stringReplacer = StringReplacer()
    fileSaver = FileSaver()
    userQuestioner = UserQuestioner(stringReplacer, fileSaver)
    planViewer = PlanViewer(fileSaver)

    taskerPlannerMenu = TaskerPlannerMenu(userQuestioner, planViewer)
    taskerPlannerMenu.runMenu()

    logging.info('Tasker Planner Finished')


def setLogger():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)


if __name__ == '__main__':
    main()
