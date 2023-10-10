# FedRAG: Federated Retrieval Augmented Generation



https://github.com/thejungwon/FedRAG/assets/12247655/27ae067c-23e9-4e70-8f7a-b94e21ee8454



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
