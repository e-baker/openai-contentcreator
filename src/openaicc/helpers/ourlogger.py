# logger.py

import logging as _logging
from pathlib import Path as _Path

class OurLogger:

    def __init__(self, name):
        self.logger = _logging.getLogger(name)
        self.logger.setLevel(_logging.DEBUG)
        self.log_path = f'../logs/{name}.log'

        # Create log file, if needed
        _Path('../logs').mkdir(exist_ok=True)
        _Path(self.log_path).touch(exist_ok=True)

        # Create file handler
        fh = _logging.FileHandler(f'../logs/{name}.log')
        fh.setLevel(_logging.DEBUG)
        fh_format = _logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(fh_format)

        # Create console handler
        ch = _logging.StreamHandler() 
        ch.setLevel(_logging.INFO)
        ch_format = _logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(ch_format)

        # Add handlers
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)