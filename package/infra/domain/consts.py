import os

PLANS_DIRECTORY_LINUX = "data/plans/"
PLANS_DIRECTORY_WINDOWS = "C:/Dor/Apps/TaskerPlanner/plans"
PLAN_QUESTIONS_FILE_PATH_LINUX = "data/plan-questions/plan.json"
PLAN_QUESTIONS_FILE_PATH_WINDOWS = "C:/Dor/Apps/TaskerPlanner/plan-questions/plan.json"

def getPlansDirectory():
    if os.name == 'nt':
        return PLANS_DIRECTORY_WINDOWS
    else:
        return PLANS_DIRECTORY_LINUX

def getPlanQuestionsFilePathDirectory():
    if os.name == 'nt':
        return PLAN_QUESTIONS_FILE_PATH_WINDOWS
    else:
        return PLAN_QUESTIONS_FILE_PATH_LINUX
