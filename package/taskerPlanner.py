import logging
import sys
from infra.userQuestioner import UserQuestioner

def main():
    logging.basicConfig(filename='taskerPlanner.log', level=logging.DEBUG)
    # format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    streamHandler = logging.StreamHandler(sys.stdout)
    # streamHandler.setFormatter(format)
    logging.getLogger().addHandler(streamHandler)

    logging.info('Tasker Planner Started')

    userQuestioner = UserQuestioner()
    userQuestioner.askQuestionsFromJson()

    logging.info('Tasker Planner Finished')

if __name__ == '__main__':
    main()