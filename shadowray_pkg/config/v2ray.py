import os

DEFAULT_CONFIG_VMESS = {
    "inbounds": [
        {
            "port": 1082,
            "protocol": "socks",
            "sniffing": {
                "enabled": True,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "auth": "noauth",
                "udp": True,
                "ip": None,
                "clients": None
            }
        }
    ],
    "outbounds": [
    ]
}


PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

V2RAY_FOLDER = os.path.join(PROJECT_PATH, "v2ray")
V2RAY_BINARY = os.path.join(V2RAY_FOLDER, "v2ray")
EXECUTE_ARGS = "-config=stdin:"

RESOURCES_FOLDER = os.path.join(PROJECT_PATH, "resources")
SUBSCRIBE_FILE = os.path.join(RESOURCES_FOLDER, "subscribes.json")
SERVER_FILE = os.path.join(RESOURCES_FOLDER, "servers.json")

SERVER_KEY_FROM_ORIGINAL = "servers_original"
SERVER_KEY_FROM_SUBSCRIBE = "servers_subscribe"
