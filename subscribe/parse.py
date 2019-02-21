import requests
from common.B64 import decode


class Parse:
    def __init__(self, url):
        self.url = url
        self.servers = []

    def update(self):
        r = requests.get(self.url).text
        text = decode(r)

        text = text.split('\n')

        for t in text:
            if len(t) is 0:
                continue
            t = t.split("://")

            self.servers.append({
                "protocol": t[0],
                "content": decode(t[1])
            })
