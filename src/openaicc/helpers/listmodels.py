# listmodels.py

# Third-party imports
from openai import OpenAI as _openai
from dotenv import load_dotenv as _dotenv
import os as _os

# Local imports
from openaicc.helpers import OurLogger as _logger
from openaicc.helpers import OAICCErrors as _error

# Constants

# CLASSES

class ListModels:
    def __init__(self):
        """
        Description

        Init Parameters
        ---------------
        """
        _dotenv()

        # Configure logging
        self._log = _logger('ListModels')
        self._log.debug('Initializing ListModels')

        # Initialize the OpenAI API client
        self._api_key :str = _os.getenv("OPENAI_API_KEY")
        if self._api_key is None:
            raise _error('No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.')
    
    def list_models(self):
        """
        Description

        Parameters
        ----------
        """
        self._log.debug(f"Request for models from OpenAI API...")
        self.openai = _openai(api_key=self._api_key)

        try:
            models = self.openai.models.list()
            self._log.debug(f"Models returned by OpenAI API: {models}")

            model_list = []
            # Iterate through the paginated response to access models
            for model in models.data:
                model_list.append(model.id)

            return(model_list)
        except:
            raise _error("Error listing models", error_code=500)



# FUNCTIONS

def main():
    """
    Description
    """

    # Initialize the ListModels class
    _listmodels = ListModels()
    models = _listmodels.list_models()
    print(models)

# MAIN
if __name__ == '__main__':
    main()