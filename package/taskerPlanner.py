import logging
import sys
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

    logging.info('Tasker Planner Started')

    print(userQuestioner.askQuestionsFromJsonFile('plan.json'))

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()