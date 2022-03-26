import os
import json
import shutil
import logging


class Settings:
    databasePath = "data"
    plansDirectoryName = "plans"
    plansQuestionsDirectoryName = "plan-questions"
    plansQuestionsFileName = "plan.json"
    settingsFileName = "settings.json"

    def __init__(self):
        pass

    def copyFilesToMountedDirectory(self):
        databasePath = self.__getDatabasePath()
        plansQuestionsDirectoryPath = os.path.join(databasePath, self.plansQuestionsDirectoryName)
        if os.path.exists(plansQuestionsDirectoryPath):
            shutil.rmtree(plansQuestionsDirectoryPath)

        os.makedirs(plansQuestionsDirectoryPath)

        shutil.copy(self.plansQuestionsFileName,
                    os.path.join(plansQuestionsDirectoryPath, self.plansQuestionsFileName))

        plansDirectoryPath = os.path.join(databasePath, self.plansDirectoryName)

        try:
            os.mkdir(plansDirectoryPath)
        except FileExistsError:
            logging.debug(f'{plansDirectoryPath} already exists, no need to create new directory')

    def getPlansDirectory(self) -> str:
        databasePath = self.__getDatabasePath()
        return os.path.join(databasePath, self.plansDirectoryName)

    def getPlanQuestionsFilePath(self) -> str:
        databasePath = self.__getDatabasePath()
        return os.path.join(databasePath, self.plansQuestionsDirectoryName, self.plansQuestionsFileName)

    def __getDatabasePath(self) -> str:
        if os.name == 'nt':
            return self.__readSettingsFile()["databasePathWindows"]
        else:
            return self.databasePath

    @staticmethod
    def __readSettingsFile():
        with open(Settings.settingsFileName, "r") as jsonFile:
            return json.load(jsonFile)
