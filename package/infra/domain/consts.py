import os

PLANS_DIRECTORY_LINUX = "data/plans/"
PLANS_DIRECTORY_WINDOWS = "C:/Dor/Apps/TaskerPlanner/plans"
PLAN_QUESTIONS_FILE_PATH = "data/plan-questions/plan.json"

def getPlansDirectory():
    if os.name == 'nt':
        return PLANS_DIRECTORY_WINDOWS
    else:
        return PLANS_DIRECTORY_LINUX
