import ssl
import os
import requests
import uvicorn
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from fastapi import FastAPI


app = FastAPI()

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLSv1
        )

@app.get("/")
async def root():
    os.environ["HTTP_PROXY"] = "http://local_proxy:3128"
    os.environ["HTTPS_PROXY"] = "https://local_proxy:3128"
    url = "https://nginx.takap.dev/index.json"
    session = requests.Session()
    session.mount('https://', MyAdapter())
    try:
        res = session.get(url, verify=False)
    except Exception:
        return {"message": "error"}
    return res.json()
