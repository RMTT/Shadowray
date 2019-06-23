VERSION_ID = "0.1.6"
AUTHOR = "RMT"
EMAIL = "d.rong@outlook.com"

COMMAND_LONG = ["version", "help", "subscribe-add=", "subscribe-update", "config-v2ray=", "config-subscribe=",
                "config-servers=", "autoconfig", "subscribe-update", "list", "start=", "config-file=", "port=",
                "servers-export=", "daemon", "stop", "v2ray-update", "ping"]
COMMAND_SHORT = "vhs:lf:d"

HELP_INFO = '''
    --help[-h]                                            print help message
    --version[-v]                                         show current version of shadowray
    --subscribe-add '<name>,<url>'                        add subscribe
    --subscribe-update                                    update subscribe
    --config-v2ray <path>                                 setup the path of v2ray binary
    --config-subscribe <path>                             setup the path of subscribe file
    --config-servers <path>                               setup the path of servers file
    --autoconfig                                          setup basic setting automatically
    --subscribe-update [--port <number>]                  update subscribe
    --list[-l]                                            show all servers
    --start[-s] <index> [-d|--daemon]                     start v2ray,the '-d or --daemon argument used to run v2ray as a daemon'
    --config-file[-f] <path>                              run v2ray use the config file that provided by yourself
    --servers-export <index>:<path>                       export the config of specified index
    --stop                                                stop v2ray
    --v2ray-update                                        update v2ray core to latest
    --ping                                                ping server
    '''
