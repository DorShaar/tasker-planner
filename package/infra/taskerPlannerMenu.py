import os
from consolemenu import selection_menu, console_menu
from consolemenu.format.menu_borders import MenuBorderStyleType
from consolemenu.items import function_item, submenu_item
from consolemenu.menu_formatter import MenuFormatBuilder
from infra.domain.fileSaver import FileSaver
from infra.domain.consts import getPlanQuestionsFilePathDirectory, getPlansDirectory
from infra.planViewer import PlanViewer
from infra.userQuestioner import UserQuestioner


class TaskerPlannerMenu:
    def __getPlansList(self):
        return os.listdir(getPlansDirectory())

    def __createChoosePlanMenuItem(self) -> submenu_item.SubmenuItem:
        showPlansItem = selection_menu.SelectionMenu(self.__getPlansList())
        return submenu_item.SubmenuItem("Show all plans", showPlansItem)

    def __createMenu(self, userQuestioner: UserQuestioner) -> console_menu.ConsoleMenu:
        menu = console_menu.ConsoleMenu("Tasker Planner", "By dorshaar")
        menu.formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True).show_prologue_bottom_border(True)

        askQuestionsFromJsonFileItem = function_item.FunctionItem(
            "Start new plan", userQuestioner.askQuestionsFromJsonFile, [getPlanQuestionsFilePathDirectory()])
        editPlanItem = function_item.FunctionItem("Edit exiting plan", userQuestioner.editPlan)
        choosePlanItem = self.__createChoosePlanMenuItem()

        menu.append_item(askQuestionsFromJsonFileItem)
        menu.append_item(editPlanItem)
        menu.append_item(choosePlanItem)
        menu.add_exit()

        return menu

    def __init__(self, userQuestioner: UserQuestioner, planViewer: PlanViewer) -> None:
        self.userQuestioner = userQuestioner
        self.planViewer = planViewer
        self.currentPlan = "None"
        self.menu = self.__createMenu(userQuestioner)

    def __handlePlanWasChosen(self, choosePlanItem: submenu_item.SubmenuItem):
        if choosePlanItem.get_return() is not None:
            plansList = self.__getPlansList()
            self.currentPlan = plansList[choosePlanItem.get_return()]
            self.userQuestioner.loadPlan(os.path.join(getPlansDirectory(), self.currentPlan))

    def __findIndexOfMenuItem(self, itemText):
        index = 0
        
        for item in self.menu.items:
            if str(item) == "Tasker Planner " + itemText:
                return index

            index = index + 1
        
        return -1

    def __updateChoosePlanMenuItem(self, choosePlanItem: submenu_item.SubmenuItem):
        self.menu.remove_item(choosePlanItem)
        choosePlanItem = self.__createChoosePlanMenuItem()
        self.menu.append_item(choosePlanItem)

    def __updateViewChoosenPlanInformationMenuItem(self):
        viewPlanInformationMenuItemIndex = self.__findIndexOfMenuItem("View plan information")
        if viewPlanInformationMenuItemIndex != -1:
            self.menu.remove_item(self.menu.items[viewPlanInformationMenuItemIndex])

        viewPlanTimeInformationMenuItemIndex = self.__findIndexOfMenuItem("View plan time information")
        if viewPlanTimeInformationMenuItemIndex != -1:
            self.menu.remove_item(self.menu.items[viewPlanTimeInformationMenuItemIndex])

        viewChoosenPlanIformationMenuItem = function_item.FunctionItem(
                "View plan information",
                self.planViewer.showPlanInformation,
                [self.currentPlan])
        
        viewPlanTimeInformationMenuItem = function_item.FunctionItem(
                "View plan time information",
                self.planViewer.showPlanTiming,
                [self.currentPlan])

        self.menu.append_item(viewChoosenPlanIformationMenuItem)
        self.menu.append_item(viewPlanTimeInformationMenuItem)

    def runMenu(self):
        ShowAllPlansMenuItemIndex = self.__findIndexOfMenuItem("Show all plans")
        StartNewPlanMenuItemIndex = self.__findIndexOfMenuItem("Start new plan")

        self.menu.prologue_text = f"Current plan: {self.currentPlan}"

        while not self.menu.is_selected_item_exit():
            if self.menu.selected_option == ShowAllPlansMenuItemIndex:
                self.__handlePlanWasChosen(self.menu.items[ShowAllPlansMenuItemIndex])

            if self.menu.selected_option == StartNewPlanMenuItemIndex:
                startNewPlanItem = self.menu.items[StartNewPlanMenuItemIndex]
                self.currentPlan = startNewPlanItem.return_value["taskName"]
                self.__updateChoosePlanMenuItem(self.menu.items[ShowAllPlansMenuItemIndex])

            if self.currentPlan != "None":
                self.__updateViewChoosenPlanInformationMenuItem()

            self.menu.prologue_text = f"Current plan: {self.currentPlan}"
            self.menu.draw()
            self.menu.process_user_input()