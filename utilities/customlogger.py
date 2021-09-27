import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename='E:/Videos/Courses/Practice/GIT/automation-framework/logs/TestLogs.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p',
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
