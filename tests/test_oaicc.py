# test_oaicc.py

import pytest
from openai.resources.chat.completions import ChatCompletion
from openaicc.helpers import OurLogger as _Logger
from openaicc import OpenAICC

_log = _Logger('Test OpenAICC')


def test_openaicc():
    oaicc = OpenAICC()
    assert isinstance(oaicc, OpenAICC), "OpenAICC should be an instance of OpenAICC"

def test_random_request():
    oaicc = OpenAICC()
    request = "Hello World"
    response = oaicc.generate_text(prompts=request, max_tokens_generated=100)
    assert response is not None, "Response should not be None"
    assert isinstance(response, ChatCompletion), "Response should be a ChatCompletion object"
    assert response != request, "Response should not be the same as the request"

def test_multiple_requests():
    
    requests = [
        "Hello World",
        "How are you today?"
    ]
    for request in requests:
        oaicc = OpenAICC()
        response = oaicc.generate_text(prompts=request, max_tokens_generated=100)
        assert response is not None, "Response should not be None"
        assert isinstance(response, ChatCompletion), "Response should be a ChatCompletion object"
        assert response.choices[0].message != "", "Response should not be empty"
        assert response != request, "Response should not be the same as the request"

def test_bad_request():
    request = 1234
    oaicc = OpenAICC()
    response = oaicc.generate_text(prompts=request, max_tokens_generated=100)
    assert response is not None, "Response should not be None"
    assert isinstance(response, ChatCompletion), "Response should be a ChatCompletion object"
    assert response.choices[0].message != "", "Response should not be empty"
    assert response != request, "Response should not be the same as the request"

