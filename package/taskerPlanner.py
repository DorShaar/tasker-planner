import logging
import sys
import os
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from infra.domain.consts import getPlanQuestionsFilePathDirectory, getPlansDirectory
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
        "Start new plan", userQuestioner.askQuestionsFromJsonFile, [getPlanQuestionsFilePathDirectory()])
    editPlanItem = FunctionItem("Edit exiting plan", userQuestioner.editPlan)
    choosePlanItem = createChoosePlanItem()

    menu.append_item(askQuestionsFromJsonFileItem)
    menu.append_item(editPlanItem)
    menu.append_item(choosePlanItem)
    menu.add_exit()

    return menu

def handleChosenPlan(choosePlanItem: SubmenuItem, userQuestioner:UserQuestioner, currentPlan: str):
    if choosePlanItem.get_return() is not None:
        plansList = getPlansList()
        currentPlan = plansList[choosePlanItem.get_return()]
        userQuestioner.loadPlan(os.path.join(getPlansDirectory(), currentPlan))
        return currentPlan

    return currentPlan

def findIndexOfMenuItem(menu: ConsoleMenu, itemText):
    index = 0
    
    for item in menu.items:
        if str(item) == "Tasker Planner " + itemText:
            return index

        index = index + 1

def updateChoosePlanItem(menu: ConsoleMenu, choosePlanItem: SubmenuItem):
    menu.remove_item(choosePlanItem)
    choosePlanItem = createChoosePlanItem()
    menu.append_item(choosePlanItem)

def runMenu(menu: ConsoleMenu, userQuestioner: UserQuestioner):
    currentPlan = "None"
    indexOfShowAllPlansItem = findIndexOfMenuItem(menu, "Show all plans")
    indexOfStartNewPlanItem = findIndexOfMenuItem(menu, "Start new plan")

    menu.prologue_text = f"Current plan: {currentPlan}"

    while not menu.is_selected_item_exit():
        if menu.selected_option == indexOfShowAllPlansItem:
            currentPlan = handleChosenPlan(menu.items[indexOfShowAllPlansItem], userQuestioner, currentPlan)

        if menu.selected_option == indexOfStartNewPlanItem:
            startNewPlanItem = menu.items[indexOfStartNewPlanItem]
            currentPlan = startNewPlanItem.return_value["taskName"]

        updateChoosePlanItem(menu, menu.items[indexOfShowAllPlansItem])
        
        menu.prologue_text = f"Current plan: {currentPlan}"
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