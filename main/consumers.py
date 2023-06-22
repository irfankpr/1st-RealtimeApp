from  channels.generic.websocket import WebsocketConsumer
import json
from  random import randint
from time import sleep


class WSconsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        for i in range(100):
            self.send(json.dumps( {"message": randint(1,1000)} ))
            sleep(1)