__author__ = 'Hernan Y.Ke'
from contextlib import contextmanager
import logging

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(logging.DEBUG,'my-log') as logger:
    logging.debug('Global logger')
    logger.debug('my-log')


logger = logging.getLogger('my-log')
logger.debug('anything')
logger.error('error')