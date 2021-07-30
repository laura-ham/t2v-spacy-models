from pydantic import BaseModel

class VectorInput(BaseModel):
    text: str

class Vectorizer:
    model: str

    def __init__(self, model: str):
        self.model = model

    async def vectorize(self, text: str):
        print("raw: ", text)
        nlp_text = self.model(text)
        print("processed: ", nlp_text)
        print("vector: ", nlp_text._.trf_data.tensors[-1].mean(axis=0)[:10])
        return nlp_text._.trf_data.tensors[-1].mean(axis=0)