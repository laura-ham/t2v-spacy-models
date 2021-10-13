from pydantic import BaseModel

class VectorInput(BaseModel):
    text: str

class Vectorizer:
    model: str

    def __init__(self, model: str):
        self.model = model

    async def vectorize(self, text: str):
        # print("raw: ", text)
        nlp_text = self.model(text)
        # print("processed: ", nlp_text)
        # print("length: ", len(nlp_text.vector))
        # print("vector: ", nlp_text.vector)
        return nlp_text.vector
