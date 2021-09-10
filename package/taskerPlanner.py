import logging
import sys
import os
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from infra.domain.consts import PLAN_QUESTIONS_FILE_PATH, getPlansDirectory
from infra.domain.stringReplacer import StringReplacer
from infra.domain.fileSaver import FileSaver
from infra.userQuestioner import UserQuestioner

def setLogger():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)

def getPlansList():
    return os.listdir(getPlansDirectory())

def createChoosePlanItem() -> SubmenuItem:
    showPlansItem = SelectionMenu(getPlansList())
    return SubmenuItem("Show all plans", showPlansItem)

def createMenu(userQuestioner: UserQuestioner) -> ConsoleMenu:
    menu = ConsoleMenu("Tasker Planner", "By dorshaar")
    menu.formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True).show_prologue_bottom_border(True)

    askQuestionsFromJsonFileItem = FunctionItem(
        "Start new plan", userQuestioner.askQuestionsFromJsonFile, [PLAN_QUESTIONS_FILE_PATH])
    editPlanItem = FunctionItem("Edit exiting plan", userQuestioner.editPlan)
    choosePlanItem = createChoosePlanItem()

    menu.append_item(askQuestionsFromJsonFileItem)
    menu.append_item(editPlanItem)
    menu.append_item(choosePlanItem)
    menu.add_exit()

    return menu

def handleChosenPlan(menu: ConsoleMenu, choosePlanItem: SubmenuItem, currentPlan: str):
    if choosePlanItem.get_return() is not None:
        plansList = getPlansList()
        currentPlan = plansList[choosePlanItem.get_return()]
        menu.prologue_text = f"Current plan: {currentPlan}"
        return currentPlan

    return currentPlan

def findIndexOfShowAllPlans(menu: ConsoleMenu):
    index = 0
    
    for item in menu.items:
        if str(item) == "Tasker Planner Show all plans":
            return index

        index = index + 1

def runMenu(menu: ConsoleMenu, userQuestioner: UserQuestioner):
    currentPlan = "None"
    indexOfShowAllPlans = findIndexOfShowAllPlans(menu)

    while not menu.is_selected_item_exit():
        menu.prologue_text = f"Current plan: {currentPlan}"
        
        choosePlanItem = menu.items[indexOfShowAllPlans]

        if menu.selected_item is choosePlanItem:
            currentPlan = handleChosenPlan(menu, choosePlanItem, currentPlan)
            userQuestioner.loadPlan(os.path.join(getPlansDirectory(), currentPlan))

        menu.remove_item(choosePlanItem)
        choosePlanItem = createChoosePlanItem()
        menu.append_item(choosePlanItem)

        menu.draw()
        menu.process_user_input()

def main():
    setLogger()

    stringReplacer = StringReplacer()
    fileSaver = FileSaver()
    userQuestioner = UserQuestioner(stringReplacer, fileSaver)

    menu = createMenu(userQuestioner)
    runMenu(menu, userQuestioner)

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()