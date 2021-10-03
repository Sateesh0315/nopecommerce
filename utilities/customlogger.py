import logging
import os


class LogGen:
    @staticmethod
    def log_gen():
        file_name = os.path.abspath(os.path.dirname(".\\..\logs\."))
        logging.basicConfig(filename=file_name + "\logs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

