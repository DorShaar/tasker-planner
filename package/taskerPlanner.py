import logging
import sys
import os
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from domain.stringReplacer import StringReplacer
from infra.userQuestioner import UserQuestioner

PLANS_DIRECTORY = "data/plans/"
# PLANS_DIRECTORY = "C:/Dor/Apps/TaskerPlanner/plans"
PLAN_QUESTIONS_FILE_PATH = "data/plan-questions/plan.json"

def setLogger():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)

def getPlansList():
    return os.listdir(PLANS_DIRECTORY)

def createChoosePlanItem() -> SubmenuItem:
    showPlansItem = SelectionMenu(getPlansList())
    return SubmenuItem("Show all plans", showPlansItem)

def createMenu(userQuestioner: UserQuestioner) -> ConsoleMenu:
    menu = ConsoleMenu("Tasker Planner", "By dorshaar")
    menu.formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True).show_prologue_bottom_border(True)

    askQuestionsFromJsonFileItem = FunctionItem("Start new plan", userQuestioner.askQuestionsFromJsonFile, [PLAN_QUESTIONS_FILE_PATH])
    editPlanItem = FunctionItem("Edit exiting plan", userQuestioner.editPlan)
    choosePlanItem = createChoosePlanItem()

    menu.append_item(askQuestionsFromJsonFileItem)
    menu.append_item(editPlanItem)
    menu.append_item(choosePlanItem)
    menu.add_exit()

    return menu

def runMenu(menu: ConsoleMenu):
    currentPlan = "None"

    while not menu.is_selected_item_exit():
        menu.prologue_text = f"Current plan: {currentPlan}"
        
        if menu.selected_item is menu.items[2]:
            plansList = getPlansList()
            if menu.items[2].get_return() is not None:
                currentPlan = plansList[menu.items[2].get_return()]
                menu.prologue_text = f"Current plan: {currentPlan}"

        choosePlanItem = createChoosePlanItem()
        menu.remove_item(menu.items[2])
        menu.append_item(choosePlanItem)

        menu.draw()
        menu.process_user_input()

def main():
    setLogger()

    stringReplacer = StringReplacer()
    userQuestioner = UserQuestioner(stringReplacer)

    menu = createMenu(userQuestioner)
    runMenu(menu)

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()