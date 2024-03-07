import pytest
import responses
from openaiconnector import OpenAIConnector  # Adjust the import path based on your project structure

@responses.activate
def test_send_request_success():
    api_key = "test_api_key"
    connector = OpenAIConnector(api_key)
    model = "text-davinci-003"
    prompt = "Hello, world!"
    mock_response = {
        "choices": [
            {"text": "Hello, world! response"}
        ]
    }

    responses.add(
        responses.POST,
        "https://api.openai.com/v1/completions",
        json=mock_response,
        status=200
    )

    result = connector.send_request(model=model, prompt=prompt)
    assert result == mock_response, "The response should match the mock response on successful API call."

@responses.activate
def test_send_request_failure():
    api_key = "test_api_key"
    connector = OpenAIConnector(api_key)
    model = "text-davinci-003"
    prompt = "Hello, world!"
    error_response = {"error": "Invalid API key"}

    responses.add(
        responses.POST,
        "https://api.openai.com/v1/completions",
        json=error_response,
        status=401
    )

    result = connector.send_request(model=model, prompt=prompt)
    assert result["error"] == "Failed to get response from OpenAI API", "The method should handle API errors correctly."
    assert result["status_code"] == 401, "The status code should reflect the error status code."

