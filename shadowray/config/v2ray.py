import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

USER_HOME = os.path.expanduser("~")

SHADOWRAY_CONFIG_FOLDER = os.path.join(USER_HOME, ".shadowray")

V2RAY_FOLDER = os.path.join(SHADOWRAY_CONFIG_FOLDER, "v2ray")
V2RAY_BINARY = os.path.join(V2RAY_FOLDER, "v2ray")
V2CTL_BINARY = os.path.join(V2RAY_FOLDER, "v2ctl")
EXECUTE_ARGS = "-config=stdin:"

RESOURCES_FOLDER = os.path.join(SHADOWRAY_CONFIG_FOLDER, "resources")
SUBSCRIBE_FILE = os.path.join(RESOURCES_FOLDER, "subscribes.json")
SERVER_FILE = os.path.join(RESOURCES_FOLDER, "servers.json")

PROJECT_CONFIG_FILE = os.path.join(SHADOWRAY_CONFIG_FOLDER, "config.json")

SERVER_KEY_FROM_ORIGINAL = "servers_original"
SERVER_KEY_FROM_SUBSCRIBE = "servers_subscribe"
