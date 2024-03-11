# __main__.py
#-----------------------------------------------------------------------------
#
#
#
# Imports
#-----------------------------------------------------------------------------

# Built-in imports from Python Standard Library
import os as _os
import argparse as _argparse
from dotenv import load_dotenv as _dotenv

# Third-party imports
from openai import OpenAI
from .helpers.oaicc_errors import (
    OAICCErrors as _new_error,
    EmptyAPIKeyError,
    NoPromptError
)
from .helpers import OurLogger as _logger

#-----------------------------------------------------------------------------
#
#
#
# Constants
#-----------------------------------------------------------------------------

_log = _logger('OpenAICC')

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
class OpenAICC:
    def __init__(self):
        """
        Description

        Init Parameters
        ---------------
        feed_id : str
            The unique feed identifier the container will represent, taken from
            https://www.broadcastify.com/listen/feed/[feed_id].


        Other Attributes & Properties
        -----------------------------
        feed_url : str
            Full https URL for the feed's main "listen" page.
        
        """
        _dotenv()
        self._api_key :str = _os.getenv("OPENAI_API_KEY")
        self.openai = OpenAI(api_key=self._api_key)

    def generate_text(self, 
                      prompts: list[str] = None, 
                      model="gpt-4-turbo-preview", 
                      temperature=0.7, 
                      max_tokens_generated=1000, 
                      top_p=None):
        
        # Validate prompts input
        if not prompts:
            # This raises and logs the error in one step.
            raise  _new_error("Empty or None prompts list provided", error_code=400, 
                            additional_data={'function': 'generate_text'})
        elif type(prompts)!= list:
            try:
                prompts = [prompts]
            except:
                # This raises and logs the error in one step.
                raise  _new_error("Prompts must be a list", error_code=400,
                                additional_data={'function': 'generate_text'})


        _log.info(f"Parameters sent to OpenAI API: prompts={prompts}, model={model}, temperature={temperature}, max_tokens_generated={max_tokens_generated}, top_p={top_p}")

        messages = [{"role": "user", "content": prompt} for prompt in prompts]

        _log.info(f"Generating text with messages {messages}...")

        try:
            response = self.openai.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens_generated,
                temperature=temperature,
                top_p=top_p,
                user="OpenAICC",
            )

            _log.info(f"Response from OpenAI API: {response}")
        
            return(response)

        except Exception as e:
            # Handle API call errors
            raise  _new_error(f"API call failed: {e}", additional_data={'function': 'generate_text'}) 

def main():
    argparser = _argparse.ArgumentParser()
    argparser.add_argument("--prompt", type=str, required=True)
    args = argparser.parse_args()

    try:
        # Set the prompt from arguments if there are any.
        prompt = args.prompt if args.prompt else None
    except  _new_error.NoPromptError as e:
        print(f"A prompt is required and can't be blank: {e.message}")
    

    try:
        # Initialize the OpenAICC object
        _content = OpenAICC()

        # Generate the text
        generated_text = _content.generate_text([prompt])

        # Handle the response
        return(generated_text)  # Handle the response as needed, here we're simply printing it
        
    except  _new_error.CommandLineError as e:
        # Handle errors
        print(f"An error occurred: {e.message}")


if __name__ == "__main__":
    main()

    