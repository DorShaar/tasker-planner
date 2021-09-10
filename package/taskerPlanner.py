import logging
import sys
from infra.domain.stringReplacer import StringReplacer
from infra.domain.fileSaver import FileSaver
from infra.userQuestioner import UserQuestioner
from infra.planViewer import PlanViewer
from infra.taskerPlannerMenu import TaskerPlannerMenu

def setLogger():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)

def main():
    setLogger()

    stringReplacer = StringReplacer()
    fileSaver = FileSaver()
    userQuestioner = UserQuestioner(stringReplacer, fileSaver)
    planViewer = PlanViewer(fileSaver)

    taskerPlannerMenu = TaskerPlannerMenu(userQuestioner, planViewer)
    taskerPlannerMenu.runMenu()

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()