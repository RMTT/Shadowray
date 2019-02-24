import requests
import json
from common.B64 import decode
from config.v2ray import *
from config.v2ray import SUBSCRIBE_FILE
from core.configuration import Configuration


class Parse:
    def __init__(self, filename=None):
        self.servers = []
        self.filename = None

        self.subscribes = json.loads("{}")
        if filename is not None:
            f = open(filename, "r")
            self.subscribes = json.load(f)
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

            config = Configuration()

            inbound = Configuration.Inbound(1082, "127.0.0.1", "socks")
            socks = Configuration.ProtocolSetting.Inbound.Socks()
            inbound.set_settings(socks)
            config.add_inbound(inbound)

            if t[0] == "vmess":
                print(t[1])
                outbound = Configuration.Outbound("vmess")
                vmess = Configuration.ProtocolSetting.Outbound.VMess()
                vmess_server = Configuration.ProtocolSetting.Outbound.VMess.Server(addr=t[1]['add'],
                                                                                   port=int(t[1]['port']))
                vmess_server.add_user(id=t[1]['id'], aid=t[1]['aid'], security=t[1]['type'],
                                      level=t[1]['v'])
                vmess.add_server(vmess_server)
                outbound.set_settings(vmess)
                config.add_ontbound(outbound)

                self.servers.append({
                    "protocol": t[0],
                    "config": config.json_obj,
                    "ps": t[1]['ps']
                })

    def update(self, name=None):
        self.servers.clear()
        if name is None:
            for j in self.subscribes:
                self.get_url(self.subscribes[j])
        else:
            self.get_url(self.subscribes[name])

    def save(self, filename=None):
        if filename is None:
            filename = SUBSCRIBE_FILE
        f = open(filename, 'w')
        f.write(json.dumps(self.subscribes))
        f.close()

    def add(self, name, url):
        self.subscribes[name] = url

    def delete(self, name):
        del self.subscribes[name]

    def get_servers(self):
        return self.servers
