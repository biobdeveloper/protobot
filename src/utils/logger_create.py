import logging
import os
import logging.handlers
from config.system import project_root_dir


def logger_create(name):
    try:
        os.mkdir(str(project_root_dir) + '/logs')
    except FileExistsError:
        pass
    level = logging.DEBUG
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(filename=f"{str(project_root_dir)}/logs/{name}.log",
                                                   when='d')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
