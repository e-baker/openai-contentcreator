# openaiconnector.py
import httpx
from typing import Optional

class OpenAIConnector:
    """
    A class to interact with the OpenAI API for generating text from prompts asynchronously using httpx.

    Attributes:
        api_key (str): The API key for authenticating with the OpenAI API.
        client (httpx.AsyncClient): An httpx AsyncClient for making API calls.
    """

    def __init__(
            self, 
            api_key: str) -> None:
        """
        Initializes the OpenAIConnector with the necessary API key.

        Parameters:
            api_key (str): The API key for the OpenAI API.

        Returns:
                OpenAIConnector: An OpenAIConnector object.
        """
        self._api_key: str = api_key

    async def __aenter__(self) -> 'OpenAIConnector':
            """Create HTTP client on enter."""
            self._client = httpx.AsyncClient(headers={
                "Authorization": f"Bearer {self._api_key}"
            })
            return self
        
    async def __aexit__(self, exc_type, exc_value, traceback):
            await self._client.aclose()

    async def generate_text(
            self, 
            prompt: str, 
            model: str = "gpt-4-turbo-preview", 
            temperature: float = 0.7, 
            max_tokens_generated: int = 100,
            top_p: Optional[float] = None
        ) -> dict:
        """
        Asynchronously generates text based on a prompt using the OpenAI API.

        Parameters:
            prompt (str): The prompt to send to the OpenAI API.
            model (str): The model to use for generating text. Default is 'text-davinci-003'.
            temperature (float): Controls randomness. Lower values mean less random completions. Default is 0.7.
            max_tokens (int): The maximum number of tokens to generate. Default is 100.

        Returns:
            dict: The response from the OpenAI API, including the generated text.
        """

        try:
            response: httpx.Response = await self._client.post(
                "https://api.openai.com/v1/engines/{model}/completions",
                json={
                    "prompt": prompt,
                    "temperature": temperature,
                    "max_tokens": max_tokens_generated,
                    "top_p": top_p
                }
            )
            response.raise_for_status()  # Raises an exception for HTTP errors
            if response is not None:
                data: dict = response.json()
            return data
        except httpx.HTTPError as e:
            print(f"Error when making the request to OpenAI: {e}")
            return None



import asyncio

async def main() -> None:
    api_key = "test_api_key"
    async with OpenAIConnector(api_key) as connector:
        prompt = "Tell me a story about a rabbit in a forest."
        response = await connector.generate_text(prompt)
        print(response["choices"][0]["text"])

asyncio.run(main())
