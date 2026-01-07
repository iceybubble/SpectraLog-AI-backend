from elasticsearch import Elasticsearch

# Connect to local Elasticsearch
# If you changed port/host, update here
es = Elasticsearch(["http://localhost:9200"])

# All SpectraLog indices will look like: spectralog-YYYY.MM.DD
INDEX_PREFIX = "spectralog"

def get_es_client():
    return Elasticsearch("http://localhost:9200")