import logging
import sys
from consolemenu import *
from consolemenu.items import *
from domain.stringReplacer import StringReplacer
from infra.userQuestioner import UserQuestioner

def main():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)

    stringReplacer = StringReplacer()
    userQuestioner = UserQuestioner(stringReplacer)

    # Create the menu
    menu = ConsoleMenu("Tasker Planner", "By dorshaar")

    askQuestionsFromJsonFileItem = FunctionItem("Start new plan", userQuestioner.askQuestionsFromJsonFile, ['plan-short-version.json'])
    editPlanItem = FunctionItem("Edit exiting plan", userQuestioner.editPlan)

    menu.append_item(askQuestionsFromJsonFileItem)
    menu.append_item(editPlanItem)

    menu.show()

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()