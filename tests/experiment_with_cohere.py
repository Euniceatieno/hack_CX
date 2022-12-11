"""
Class to experiment with the capabilities of cohere.
Configure .env with COHERE_API_KEY and run this file.
"""

from hackCX_app.cohere.cohere_client import CohereClient

co = CohereClient()

# Experiment with using prompts
print("Completing sentences")
prompts = ["In a world far away", "Look, Up in the sky"]
for prompt in prompts:
    print(prompt, '\n'.join(co.predict_response_with_prompt(prompt)), "...")

print("")
print("Answering questions")
questions = ["How do I logon?", "I got response '500 server error'. How do I fix it?"]

for question in questions:
    print("Q. "+question)
    print(co.query(question))
    print()

