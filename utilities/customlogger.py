import logging
import os


class LogGen:
    @staticmethod
    def log_gen():
        file_path_base = os.path.abspath(os.path.dirname(".\\..\logs\."))
        file_path = file_path_base+"\logs.log"
        logging.basicConfig(filename=file_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
