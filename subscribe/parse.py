import requests
import json
from common.B64 import decode
from config.v2ray import *


class Parse:
    def __init__(self, filename=None):
        self.servers = []

        self.subscribes = None
        if filename is not None:
            f = open(filename, "r")
            self.subscribes = json.loads(f.read())
            f.close()

            self.filename = filename

    def get_url(self, url):
        r = requests.get(url).text
        text = decode(r)

        text = text.split('\n')

        for t in text:
            if len(t) is 0:
                continue
            t = t.split("://")
            t[1] = json.loads(decode(t[1]))

            if t[0] == "vmess":
                config = DEFAULT_CONFIG_VMESS
                config['outbounds'].append({
                    "protocol": "vmess",
                    "settings": {
                        "vnext": [
                            {
                                "address": t[1]['add'],
                                "port": t[1]['port'],
                                "users": [
                                    {
                                        "id": t[1]['id'],
                                        "alterId": t[1]['aid']
                                    }
                                ]
                            }
                        ]
                    }
                })
                self.servers.append({
                    "protocol": t[0],
                    "config": config,
                    "ps": t[1]['ps']
                })

    def update(self, name=None):
        self.servers.clear()
        if name is None:
            for j in self.subscribes:
                self.get_url(self.subscribes[j])
        else:
            self.get_url(self.subscribes[name])

    def save(self, filename):
        f = open(filename, 'w')
        f.write(str(self.subscribes))
        f.close()

    def add(self, name, url):
        self.subscribes[name] = url
        self.save(self.filename)


if __name__ == '__main__':
    p = Parse("https://mosucloud.info/modules/servers/V2raySocks/osubscribe.php?sid=22&token=kbaiisxd")
    p.update()
    print(p.servers)
