# FedRAG: Federated Retrieval Augmented Generation

> The Retrieval Augmented Generation (RAG) approach offers a straightforward and efficient method for integrating new information into existing large language models (LLMs) without requiring additional training. However, when applying this RAG-based LLM in a distributed data source environment, there arises a need to either centralize the data or make it externally accessible. This poses potential challenges related to data ownership rights and the inconvenience of preprocessing sensitive information. In this research, we propose a novel approach to construct a RAG-based LLM pipeline within a federated environment, thus eliminating the necessity for data transfer. Our solution leverages global-local question-answering technology, an expedited engineering strategy aimed at extracting comprehensive answers from limited data sources.


## Demo Video

https://github.com/thejungwon/FedRAG/assets/12247655/27ae067c-23e9-4e70-8f7a-b94e21ee8454

(Should the video above fail to play, click [here](https://github.com/thejungwon/FedRAG/blob/main/materials/demo-video.mp4) to view it directly.)

## How it Works
![Picture1](https://github.com/thejungwon/FedRAG/assets/12247655/79546a2e-c976-4a2f-8c06-e17024d53b52)




## Prerequisite
- OpenAI API Key
- Python 3.9
## Install

```
pip install -U pip
pip install -r requirements.txt
```

## Run

### Streamlit

```
streamlit run client.py
```

### Global Server

```
python global_server.py
```

### Local Servers

```
python server.py --user_id 0
python server.py --user_id 1
python server.py --user_id 2
```
