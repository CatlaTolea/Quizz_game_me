import logging

import coloredlogs

logger = logging.getLogger(__name__)
# logging.basicConfig(filename="quiz_log.log", filemode="w", format=' %(asctime)s| %(filename)s | %(levelname)s | line: %(lineno)d | %(message)s', level=logging.DEBUG)
logging.basicConfig(format=' %(asctime)s| %(filename)s | %(levelname)s | line: %(lineno)d | %(message)s', level=logging.DEBUG)
coloredlogs.install(level='DEBUG', logger=logger)

if __name__ == '__main__':
    logger.debug("Aici eu un debug00")
    logger.info("Aici e un infor print ")
    logger.warning("Aici este un warning")
    logger.error("aici e o eroare")