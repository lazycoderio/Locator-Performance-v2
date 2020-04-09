from elasticsearch import Elasticsearch
from datetime import datetime

from config import Config

c = Config()


es = Elasticsearch(
    c.env_vars["ELASTICSEARCH"]["URL"],
    http_auth=(c.env_vars["ELASTICSEARCH"]["USERNAME"], c.env_vars["ELASTICSEARCH"]["PASSWORD"]),
    scheme="https",
    port=443,
)

index = 'browser-' + str(datetime.now().strftime("%Y-%m-%d-%H"))
doc_type = "browser_locator"
user_agent = self.to_dict(ua)
body = {}
body['user_agent'] = user_agent
body["locator"] = locator
body["exec_time"] = stats
body["datetime"] = datetime.now()
if str(type(driver)).__contains__("remote"):
    body["driver_type"]  = 'remote'
else:
    body["driver_type"] = 'local'
es.index(index, doc_type, body)