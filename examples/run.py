# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/french-company-finder").call(run_input={
    "queries": [
        "logiciel"
    ],
    "departments": [
        "69"
    ],
    "minRevenue": 1000000,
    "maxItems": 25
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
