import json
from shadowray.config.v2ray import SERVER_FILE
from shadowray.config.v2ray import SERVER_KEY_FROM_SUBSCRIBE, SERVER_KEY_FROM_ORIGINAL


class Server:
    def __init__(self, filename=None):
        self.__servers = json.loads('{"servers_subscribe": [] ,"servers_original": []}')

        self.__filename = SERVER_FILE
        if filename is not None:
            f = open(filename, 'r')
            self.__servers = json.load(f)
            f.close()
            self.__filename = filename

    def save(self, filename=None):
        if filename is None:
            filename = self.__filename

        f = open(filename, 'w')
        f.write(json.dumps(self.__servers))
        f.close()

    def add(self, protocol, config, ps, key):
        self.__servers[key].append({
            "protocol": protocol,
            "config": config,
            "ps": ps
        })

    def get(self, index):
        if self.__servers is None:
            return None
        return self.__servers[index]

    def get_servers(self):
        return self.__servers

    @property
    def original_servers_number(self):
        return len(self.__servers[SERVER_KEY_FROM_ORIGINAL])

    @property
    def subscribe_servers_number(self):
        return len(self.__servers[SERVER_KEY_FROM_SUBSCRIBE])

    @property
    def servers_number(self):
        return self.subscribe_servers_number + self.original_servers_number

    def get_server(self, index):
        if index >= self.servers_number:
            print("Index out of range.")
            return None

        if index < self.original_servers_number:
            return self.__servers[SERVER_KEY_FROM_ORIGINAL][index]
        else:
            return self.__servers[SERVER_KEY_FROM_SUBSCRIBE][index - self.original_servers_number]

    def get_config(self, index):
        if index >= self.servers_number:
            print("Index out of range.")
            return None

        if index < self.original_servers_number:
            return self.__servers[SERVER_KEY_FROM_ORIGINAL][index]['config']
        else:
            return self.__servers[SERVER_KEY_FROM_SUBSCRIBE][index - self.original_servers_number]['config']

    def clear(self, key):
        self.__servers[key].clear()
