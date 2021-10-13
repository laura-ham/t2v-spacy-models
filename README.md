# text2vec-spacy Weaviate module

This is an example of using a Spacy (with Transformer base model) as Weaviate vectorization module. This example can be used to show how the `text2vec-transformers` module code in Weaviate can be used to vectorize text with a SpaCy model. Documentation of [custom Weaviate modules, option A](https://www.semi.technology/developers/weaviate/current/modules/custom-modules.html#a-replace-parts-of-an-existing-module) is followed. 

## How to use

`pip install -r requirements.txt` (`pip3 install -r requirements.txt`)

For testing, you can start up the app with `./uvicorn app:app --host 0.0.0.0 --port 8081`

Building the docker image: `docker build -f Dockerfile -t text2vec-spacy .`
And then start up Weaviate like you're used to with `docker-compose up` (docker-compose configuration file is included in this repo). This docker-compose file includes importing a news articles demo dataset. 

## What to include in the tutorial article: 

* All steps mentioned here: https://www.semi.technology/developers/weaviate/current/modules/custom-modules.html#a-replace-parts-of-an-existing-module
* In the `docker-compose.yml`, replace `TRANSFORMERS_INFERENCE_API: 'http://t2v-transformers:8080'` by `TRANSFORMERS_INFERENCE_API: 'http://t2v-spacy:8080'` (or any other location and port where the inference model is running).
* How to build a docker image (this is not straightforward for data scientists)
* How to build an API wrapper with the required endpoints around the user's custom vectorizer
* Info about `POST /vectors` endpoint (when the `text2vec-transformers` module is used as basis):
    * `POST /vectors` in the `t2v-transformers` module  is essentially a “text 2 vec” black box. It is agnostic of Weaviate-specific things, such as schema, properties, configuration and at the same time it abstracts all vector-logic (e.g. how are multiple vectors pooled into one) from the caller. The expectation in this case is that it creates exactly one vector (or an error) from the given input. 
    * Final output is always one vector, input varies. This also means that if the module has the capability to understand e.g. sentences it can use that. For example in the contextionary `My name is foobar. I live in Spain` is just the mean of every word, because the contextionary has no concept of sentences. With transformers, however, which work at sentence level, the output vector would be the mean of the sentence vectors `My name is foobar` and `I live in Spain.` -> the caller is agnostic of how text is aggregated into a vector, but it needs to return a single one.
    * This endpoint is typically called once per object, so all text inputs that the Go-side of the module code decided to aggregate from the object is going to be the input for this endpoint. In the case of text2vec-transformers it adds a space (` `) between each independent unit, so if the source had two properties, since they need to be merged into one text input and transformers understand punctuation, it would use it here to combine multiple properties - even if the source didn’t have any punctuation.