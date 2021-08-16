import requests
import os
import time
import json

from google.cloud import pubsub_v1

class Publish:
    def __init__(self):
        self.project_id = "swaradatraining"
        self.topic_id = "Stocks_poly"

    def fetch_stock(self):
        url = "https://api.polygon.io/v3/reference/tickers?active=true&sort=ticker&order=asc&limit=10&apiKey=JokBgG_dq3Lvpcxd0etFPOJ9FX1ZNnoC"

        data = requests.get(url)
        
        result_string = data.json()['results'][0]
        result_string['active']= str(result_string['active'])

        json_string = json.dumps(result_string)
        print("Equivalent JSON string of dictionary =",json_string)

        return str(json_string)

    def publish_msg(self):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id,self.topic_id)

        # fetch_stock should be byte string
        stock_data = self.fetch_stock()
        stock_data = stock_data.encode("utf-8")

        future = publisher.publish(topic_path,stock_data)
        print(future.result())





pub = Publish()
pub.publish_msg()
pub.fetch_stock()

