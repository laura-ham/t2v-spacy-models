FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get -y install curl build-essential
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="$PATH:/root/.cargo/bin"

COPY requirements.txt .
RUN pip3 install -r requirements.txt
# RUN pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_scibert-0.4.0.tar.gz
RUN pip3 install spacy-transformers
RUN python3 -m spacy download en_core_web_trf

COPY . .

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["uvicorn app:app --host 0.0.0.0 --port 8080"]
