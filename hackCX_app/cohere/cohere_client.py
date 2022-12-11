import cohere
from HackCX.settings import COHERE_API_KEY


class CohereClient:
    def __init__(self):
        self.cohere_client = cohere.Client(COHERE_API_KEY)

    def predict_response_with_prompt(self, prompt):
        responses = self.cohere_client.generate(prompt=prompt)
        return list(map(lambda response: response.text.lstrip(), responses))
