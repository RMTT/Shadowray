from subscribe.parse import Parse
from core.server import Server
from config.v2ray import V2RAY_BINARY
from core.execute import Execute
from config.v2ray import SERVER_KEY_FROM_ORIGINAL, SERVER_KEY_FROM_SUBSCRIBE
import json


class Manager:
    def __init__(self, subscribe_file_name=None, server_file_name=None, binary=V2RAY_BINARY):
        self.subscribe = Parse(filename=subscribe_file_name)
        self.server = Server(filename=server_file_name)
        self.execute = Execute(binary=binary)

    def add_subscribe(self, name, url):
        self.subscribe.add(name, url)

    def update_subscribe(self):
        self.subscribe.update()

        self.server.clear(SERVER_KEY_FROM_SUBSCRIBE)

        s = self.subscribe.get_servers()

        for i in s:
            self.server.add(protocol=i['protocol'], config=i['config'], ps=i['ps'], key=SERVER_KEY_FROM_SUBSCRIBE)

    def delete_subscribe(self, name):
        self.subscribe.delete(name)

    def show_servers(self):
        servers = self.server.get_servers()

        count = 0
        for s in servers[SERVER_KEY_FROM_ORIGINAL]:
            count += 1
            print(str(count) + " ---- " + s['ps'] + " ---- " + s['protocol'])

        for s in servers[SERVER_KEY_FROM_SUBSCRIBE]:
            count += 1
            print(str(count) + " ---- " + s['ps'] + " ---- " + s['protocol'])

    def proxy(self, index):
        self.execute.exec(bytes(json.dumps(self.server.get_config(index)), encoding='utf8'))

    def save(self):
        self.server.save()
        self.subscribe.save()
