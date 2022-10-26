from fastapi import FastAPI
from ast import Call
import CallApi
from datetime import datetime
import re
import json
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts="http://localhost:9200",
                   http_auth=('elastic', 'lgcuaanh'))


def PutToElas(index_name, id_mess):
    textOk = GetFromElas()
    result = CallApi.getResultFromApi(textOk)
    print(type(result))
    doc = {
        'spamOrNot': result,
    }
    es.index(index=index_name, id=id_mess, document=doc)
    # print(resp['result'])


def GetFromElas():
    resp = es.get(index="doan_test", id=1)
    es.indices.refresh(index="doan_test")
    data = str(resp['_source']["text"])
    return data


def main():
    PutToElas(index_name="doan_test_res", id_mess=1)


if __name__ == "__main__":
    main()
