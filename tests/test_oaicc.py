# test_oaicc.py

import pytest
from openaicc.helpers import OurLogger as _Logger
from openaicc import OpenAICC

_log = _Logger('Test OpenAICC')

def test_openaicc():
    oaicc = OpenAICC()
    assert isinstance(oaicc, OpenAICC), "OpenAICC should be an instance of OpenAICC"

def test_random_request():
    oaicc = OpenAICC()
    request = "The curious monkey climbed to the top of the tall oak tree to get a better view of the winding river below."
    response = oaicc.generate_text(prompts=request, max_tokens_generated=100)
    _log.info(f"Response: {response}")
    assert response is not None, "Response should not be None"
    assert isinstance(response, str), "Response should be a string"
    assert response != request, "Response should not be the same as the request"
    assert request in response, "Response should contain the request"

def test_multiple_requests():
    oaicc = OpenAICC()
    requests = [
        "Hello World",
        "How are you today?"
    ]
    for request in requests:
        response = oaicc.generate_text(prompts=request, max_tokens_generated=100)
        _log.info(f"Response: {response}")
        assert response is not None, "Response should not be None"
        assert isinstance(response, str), "Response should be a string"
        assert len(response) > 0, "Response should not be empty"
        assert response != request, "Response should not be the same as the request"
        assert request in response, "Response should contain the request"
