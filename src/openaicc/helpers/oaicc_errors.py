# oaicc_errors.py
#-----------------------------------------------------------------------------
#
#
#
# Imports
#-----------------------------------------------------------------------------

# Built-in imports from Python Standard Library
import logging

# Third-party imports



#-----------------------------------------------------------------------------
#
#
#
# Constants
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#
#
#
# CLASSES
#-----------------------------------------------------------------------------





#-----------------------------------------------------------------------------
#
#
#
# OpenAICC
#-----------------------------------------------------------------------------

# Configure logging
logging.basicConfig(level=logging.ERROR, filename='oaicc_errors.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class OAICCErrors(Exception):
    def __init__(self, message, error_code=None, additional_data=None):
        """
        Initialize the custom exception with the given parameters.

        Parameters:
        - message (str): A description of the error.
        - error_code (optional[int]): A code identifying the error.
        - additional_data (optional[dict]): Any additional data relevant to the error.
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.additional_data = additional_data
        # Log the error upon initialization
        self.log_error()

    def log_error(self):
        """
        Log the error details.
        """
        error_details = {
            'message': self.message,
            'error_code': self.error_code,
            'additional_data': self.additional_data
        }
        # Log the error with its details. Adjust the logging level as needed.
        logging.error(f"OAICC Error: {error_details}")