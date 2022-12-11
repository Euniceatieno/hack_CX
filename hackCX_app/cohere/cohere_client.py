import cohere
import pandas as pd
import numpy as np
from annoy import AnnoyIndex
from datasets import load_dataset

from HackCX.settings import COHERE_API_KEY


class CohereClient:
    def __init__(self):
        self.cohere_client = cohere.Client(COHERE_API_KEY)
        self.df = pd.DataFrame(load_dataset("trec", split="train"))[:1000]
        embeds = self.cohere_client.embed(texts=list(self.df['text']), model="large", truncate="LEFT").embeddings
        embeds = np.array(embeds)
        self.search_index = AnnoyIndex(embeds.shape[1], 'angular')

        for i in range(len(embeds)):
            self.search_index.add_item(i, embeds[i])
        self.search_index.build(10)
        self.search_index.save("test.ann")

    def predict_response_with_prompt(self, prompt):
        responses = self.cohere_client.generate(prompt=prompt)
        return list(map(lambda response: response.text.lstrip(), responses))

    def query(self, question):
        query_embed = self.cohere_client.embed(texts=[question], model="large", truncate="LEFT").embeddings
        similar_item_ids = self.search_index.get_nns_by_vector(query_embed[0], 10, include_distances=False)

        results = pd.DataFrame(data={'texts': self.df.iloc[similar_item_ids[0]]['text']})
        print(results)
