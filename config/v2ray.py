DEFAULT_CONFIG_VMESS = {
    "inbounds": [
        {
            "port": 1080,
            "protocol": "socks",
            "sniffing": {
                "enabled": True,
                "destOverride": ["http", "tls"]
            },
            "settings": {
                "auth": "noauth"
            }
        }
    ],
    "outbounds": [
    ]
}

V2RAY_FOLDER = "../v2ray"
V2RAY_BINARY = "../v2ray/v2ray"
EXECUTE_ARGS = "-config=stdin:"
