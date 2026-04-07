from elasticsearch import Elasticsearch

# Keep Elasticsearch calls fail-fast when ES is offline.
DEFAULT_ES_URL = "http://localhost:9200"
DEFAULT_REQUEST_TIMEOUT = 1

# All SpectraLog indices will look like: spectralog-YYYY.MM.DD
INDEX_PREFIX = "spectralog"


def get_es_client():
    return Elasticsearch(
        DEFAULT_ES_URL,
        request_timeout=DEFAULT_REQUEST_TIMEOUT,
        retry_on_timeout=False,
        max_retries=0,
    )