import json


class BaseConfig:
    def __init__(self, obj, **kwargs):
        self.__obj = obj

        for key in kwargs:
            self.__obj[key] = kwargs[key]

    def __str__(self):
        return json.dumps(self.__obj)

    @property
    def json(self):
        return str(self)

    @property
    def json_obj(self):
        return self.__obj


class Configuration(BaseConfig):
    def __init__(self):
        self.__configuration = {
            "inbounds": [],
            "outbounds": []
        }

        super().__init__(self.__configuration)

    def set_log(self, log_obj):
        self.__configuration['log'] = log_obj.json_obj

    def set_api(self, api_obj):
        self.__configuration['api'] = api_obj.json_obj

    def add_inbound(self, inbound_obj):
        self.__configuration['inbounds'].append(inbound_obj.json_obj)

    def add_ontbound(self, outbound_obj):
        self.__configuration['outbounds'].append(outbound_obj.json_obj)

    class Log(BaseConfig):
        DEBUG = "debug"
        INFO = "info"
        WARNING = "warning"
        ERROR = "error"
        NONE = "none"

        def __init__(self, access, error, level):
            self.__log = {
                "access": access,
                "error": error,
                "level": level
            }

            super().__init__(self.__log)

    class Inbound(BaseConfig):
        def __init__(self, port, listen, protocol, tag=None):
            self.__inbound = {
                "port": port,
                "listen": listen,
                "protocol": protocol,
                "settings": {},
                "streamSettings": {},
                "sniffing": {
                    "enabled": True,
                    "destOverride": ["http", "tls"]
                }
            }

            if tag is not None:
                self.__inbound['tag'] = tag
            super().__init__(self.__inbound)

        def set_settings(self, setting_boj):
            self.__inbound['settings'] = setting_boj.json_obj

        def set_tag(self, tag):
            self.__inbound['tag'] = tag

        def set_stream(self, stream_obj):
            self.__inbound['streamSettings'] = stream_obj.json_obj

        def set_sniffing(self, sniffing_obj):
            self.__inbound['sniffing'] = sniffing_obj.json_obj

        def set_allocate(self, allocate_obj):
            self.__inbound['allocate'] = allocate_obj.json_obj

        class Allocate:
            def __init__(self, strategy="always", refresh=5, concurrency=3):
                self.__allocate = {
                    "strategy": strategy,
                    "refresh": refresh,
                    "concurrency": concurrency
                }

            def __str__(self):
                return json.dumps(self.__allocate)

            @property
            def json(self):
                return str(self)

            @property
            def json_obj(self):
                return self.__allocate

        class Sniffing:
            def __init__(self, enable, dest_override=None):
                if dest_override is None:
                    dest_override = ["http", "tls"]

                self.__sniffing = {
                    "enabled": enable,
                    "destOverride": dest_override
                }

            def add_dest_override(self, p):
                self.__sniffing['destOverride'].append(p)

            def __str__(self):
                return json.dumps(self.__sniffing)

            @property
            def json(self):
                return str(self)

            @property
            def json_obj(self):
                return self.__sniffing

    class Outbound(BaseConfig):
        def __init__(self, protocol, tag=None, proxy_tag=None, send_through="0.0.0.0"):
            self.__outbound = {
                "sendThrough": send_through,
                "protocol": protocol,
                "settings": {},
                "streamSettings": {},
            }

            if tag is not None:
                self.__outbound['tag'] = tag
            if proxy_tag is not None:
                self.__outbound['proxySettings'] = proxy_tag
            super().__init__(self.__outbound)

        def set_settings(self, setting_boj):
            self.__outbound['settings'] = setting_boj.json_obj

        def set_tag(self, tag):
            self.__outbound['tag'] = tag

        def set_stream(self, stream_obj):
            self.__outbound['streamSettings'] = stream_obj.json_obj

        def set_mux(self, mux_obj):
            self.__outbound['mux'] = mux_obj.json_obj

        class Mux(BaseConfig):
            def __init__(self, enable, concurrency=8):
                self.__mux = {
                    "enabled": enable,
                    "concurrency": concurrency
                }
                super().__init__(self.__mux)

    class Api(BaseConfig):
        def __init__(self, tag):
            self.__api = {
                "tag": tag,
                "services": []
            }
            super().__init__(self.__api)

        def add_service(self, service):
            self.__api['services'].append(service)

    class Dns(BaseConfig):
        def __init__(self, client_ip, tag):
            self.__dns = {
                "hosts": {},
                "servers": [],
                "clientIp": client_ip,
                "tag": tag
            }
            super().__init__(self.__dns)

        def add_host(self, key, value):
            self.__dns['host'][key] = value

        def add_server(self, server_obj):
            self.__dns['servers'].append(server_obj.json_obj)

        class Server(BaseConfig):
            def __init__(self, addr, port):
                self.__server = {
                    "address": addr,
                    "port": port,
                    "domains": []
                }

                super().__init__(self.__server)

            def add_domain(self, domain):
                self.__server['domains'].append(domain)

    class Stats(BaseConfig):
        def __init__(self):
            self.__stats = {}
            super().__init__(self.__stats)

    class Routing(BaseConfig):
        def __init__(self, strategy):
            self.__routing = {
                "domainStrategy": strategy,
                "rules": [],
                "balancers": []
            }
            super().__init__(self.__routing)

        def add_rule(self, rule_obj):
            self.__routing['rules'].append(rule_obj.json_obj)

        def add_balancer(self, balancer_obj):
            self.__routing['balancers'].append(balancer_obj.json_obj)

        class Rule(BaseConfig):
            def __init__(self, port, outbound_tag=None, balancer_tag=None, network=None, type="field"):
                self.__rule = {
                    "type": type,
                    "domain": [],
                    "ip": [],
                    "port": port,
                    "network": network,
                    "source": [],
                    "user": [],
                    "inboundTag": [],
                    "protocol": [],
                    "outboundTag": outbound_tag,
                    "balancerTag": balancer_tag
                }
                super().__init__(self.__rule)

            def add_domain(self, domain):
                self.__rule['domain'].append(domain)

            def add_ip(self, ip):
                self.__rule['ip'].append(ip)

            def add_source(self, source):
                self.__rule['source'].append(source)

            def add_user(self, user):
                self.__rule['user'].append(user)

            def add_protocol(self, protocol):
                self.__rule['protocol'].append(protocol)

            def add_inbound_tag(self, tag):
                self.__rule['inboundTag'].append(tag)

        class Balancer(BaseConfig):
            def __init__(self, tag):
                self.__balancer = {
                    "tag": tag,
                    "selector": []
                }
                super().__init__(self.__balancer)

            def add_selector(self, selector):
                self.__balancer['selector'].append(selector)

    class Policy(BaseConfig):
        def __init__(self):
            self.__policy = {
                "levels": {},
                "system": {}
            }
            super().__init__(self.__policy)

        def add_level_policy(self, level, policy_obj):
            self.__policy['levels'][str(level)] = policy_obj.json_obj

        def set_system_policy(self, policy_obj):
            self.__policy['system'] = policy_obj.json_obj

        class LevelPolicy(BaseConfig):
            def __init__(self, stats_user_uplink, stats_user_downlink, handshake=4, conn_idle=300, uplink_only=2,
                         downlink_only=5, buffer_size=None):
                self.__level_policy = {
                    "handshake": handshake,
                    "connIdle": conn_idle,
                    "uplinkOnly": uplink_only,
                    "downlinkOnly": downlink_only,
                    "statsUserUplink": stats_user_uplink,
                    "statsUserDownlink": stats_user_downlink,
                }
                if buffer_size is not None:
                    self.__level_policy['bufferSize'] = buffer_size
                super().__init__(self.__level_policy)

        class SystemPolicy(BaseConfig):
            def __init__(self, stats_inbound_uplink, stats_inbound_downlink):
                self.__system_policy = {
                    "statsInboundUplink": stats_inbound_uplink,
                    "statsInboundDownlink": stats_inbound_downlink
                }
                super().__init__(self.__system_policy)

    class Reverse(BaseConfig):
        def __init__(self):
            self.__reverse = {
                "bridges": [],
                "portals": []
            }

            super().__init__(self.__reverse)

        def add_bridge(self, bridge_obj):
            self.__reverse['bridges'].append(bridge_obj.json_obj)

        def add_portal(self, portal_obj):
            self.__reverse['portals'].append(portal_obj.json_obj)

        class Bridge(BaseConfig):
            def __init__(self, tag, domain):
                self.__bridge = {
                    "tag": tag,
                    "domain": domain
                }
                super().__init__(self.__bridge)

        class Portal(BaseConfig):
            def __init__(self, tag, domain):
                self.__bridge = {
                    "tag": tag,
                    "domain": domain
                }
                super().__init__(self.__bridge)

    class ProtocolSetting:
        class Inbound:
            class DokodemoDoor(BaseConfig):
                def __init__(self, port, network="tcp", timeout=300, **kwargs):
                    self.__dokodemo_door = {
                        "port": port,
                        "network": network,
                        "timeout": timeout
                    }

                    for key in kwargs:
                        self.__dokodemo_door[key] = kwargs[key]

                    super().__init__(self.__dokodemo_door)

                def set_address(self, addr):
                    self.__dokodemo_door['address'] = addr

                def set_follow_redirect(self, f):
                    self.__dokodemo_door['followRedirect'] = f

                def set_user_level(self, level):
                    self.__dokodemo_door['userLevel'] = level

            class Http(BaseConfig):
                def __init__(self, user_level, timeout=300, allow_transparent=False, **kwargs):
                    self.__http = {
                        "timeout": timeout,
                        "allowTransparent": allow_transparent,
                        "userLevel": user_level,
                        "account": []
                    }

                    for key in kwargs:
                        self.__http[key] = kwargs[key]
                    super().__init__(self.__http)

                def add_account(self, username, password):
                    self.__http['account'].append({
                        "user": username,
                        "pass": password
                    })

            class Shadowsocks(BaseConfig):
                def __init__(self, method, password, level=0, network="tcp", **kwargs):
                    self.__shadowsocks = {
                        "method": method,
                        "password": password,
                        "level": level,
                        "network": network
                    }

                    for key in kwargs:
                        self.__shadowsocks[key] = kwargs[key]

                    super().__init__(self.__shadowsocks)

                def set_email(self, email):
                    self.__shadowsocks['email'] = email

                def set_ota(self, f):
                    self.__shadowsocks['ota'] = f

            class VMess(BaseConfig):
                def __init__(self, disable_insecure_encryption=False, **kwargs):
                    self.__vmess = {
                        "disableInsecureEncryption": disable_insecure_encryption,
                        "clients": []
                    }

                    for key in kwargs:
                        self.__vmess[key] = kwargs[key]

                    super().__init__(self.__vmess)

                def set_detour(self, to):
                    self.__vmess['detour'] = {
                        "to": to
                    }

                def set_default(self, level, aid):
                    self.__vmess['default'] = {
                        "level": level,
                        "alterId": aid
                    }

                def add_client(self, id, level, aid, email):
                    self.__vmess['clients'].append({
                        "id": id,
                        "level": level,
                        "alterId": aid,
                        "email": email
                    })

            class Socks(BaseConfig):
                def __init__(self, auth="noauth", udp=False, **kwargs):
                    self.__socks = {
                        "auth": auth,
                        "udp": udp,
                        "accounts": []
                    }

                    for key in kwargs:
                        self.__socks[key] = kwargs[key]
                    super().__init__(self.__socks)

                def set_ip(self, addr):
                    self.__socks['ip'] = addr

                def set_user_level(self, level):
                    self.__socks['userLevel'] = level

                def add_user(self, username, password):
                    self.__socks['accounts'].append({
                        "user": username,
                        "pass": password
                    })

        class MTProto(BaseConfig):
            def __init__(self, **kwargs):
                self.__mt_proto = {
                    "users": []
                }

                for key in kwargs:
                    self.__mt_proto[key] = kwargs[key]
                super().__init__(self.__mt_proto)

            def add_user(self, email, level, secret):
                self.__mt_proto['users'].append({
                    "email": email,
                    "level": level,
                    "secret": secret
                })

        class Outbound:
            class Blackhole(BaseConfig):
                def __init__(self, response_type):
                    self.__blackhole = {
                        "response": {
                            "type": response_type
                        }
                    }
                    super().__init__(self.__blackhole)

            class Dns(BaseConfig):
                def __init__(self, network, address, port):
                    self.__dns = {
                        "network": network,
                        "address": address,
                        "port": port
                    }

                    super().__init__(self.__dns)

            class Freedom(BaseConfig):
                def __init__(self, domain_strategy, redirect, user_level):
                    self.__freedom = {
                        "domainStrategy": domain_strategy,
                        "redirect": redirect,
                        "userLevel": user_level
                    }

                    super().__init__(self.__freedom)

            class ShadowSocks(BaseConfig):
                def __init__(self):
                    self.__shadowsocks = {
                        "servers": []
                    }

                    super().__init__(self.__shadowsocks)

                def add_server(self, address, port, method, password, level, ota=False, email=None):
                    self.__shadowsocks['servers'].append({
                        "email": email,
                        "address": address,
                        "port": port,
                        "method": method,
                        "password": password,
                        "ota": ota,
                        "level": level
                    })

            class Socks(BaseConfig):
                def __init__(self):
                    self.__socks = {
                        "servers": []
                    }
                    super().__init__(self.__socks)

                def add_server(self, server_obj):
                    self.__socks['servers'].append(server_obj.json_obj)

                class Server(BaseConfig):
                    def __init__(self, addr, port):
                        self.__server = {
                            "address": addr,
                            "port": port,
                            "users": []
                        }
                        super().__init__(self.__server)

                    def add_user(self, username, password, level):
                        self.__server['users'].append({
                            "user": username,
                            "pass": password,
                            "level": level
                        })

            class VMess(BaseConfig):
                def __init__(self):
                    self.__vmess = {
                        "vnext": []
                    }
                    super().__init__(self.__vmess)

                def add_server(self, server_obj):
                    self.__vmess['vnext'].append(server_obj.json_obj)

                class Server(BaseConfig):
                    def __init__(self, addr, port):
                        self.__server = {
                            "address": addr,
                            "port": port,
                            "users": []
                        }
                        super().__init__(self.__server)

                    def add_user(self, id, aid, security, level):
                        self.__server['users'].append({
                            "id": id,
                            "alterId": aid,
                            "security": security,
                            "level": level
                        })

    class StreamSetting(BaseConfig):
        STREAMSETTING = "StreamSetting"
        TRANSPORT = "Transport"

        def __init__(self, type, network="tcp", security="none", **kwargs):
            if type == Configuration.StreamSetting.STREAMSETTING:
                self.__stream_setiing = {
                    "network": network,
                    "security": security,
                    "tlsSettings": {},
                    "tcpSettings": {},
                    "kcpSettings": {},
                    "wsSettings": {},
                    "httpSettings": {},
                    "dsSettings": {},
                    "quicSettings": {},
                    "sockopt": {
                        "mark": 0,
                        "tcpFastOpen": False,
                        "tproxy": "off"
                    }
                }
            elif type == Configuration.StreamSetting.TRANSPORT:
                self.__stream_setiing = {
                    "tcpSettings": {},
                    "kcpSettings": {},
                    "wsSettings": {},
                    "httpSettings": {},
                    "dsSettings": {},
                    "quicSettings": {}
                }

            super().__init__(self.__stream_setiing, **kwargs)

        def set_tls(self, tls_obj):
            self.__stream_setiing['tlsSettings'] = tls_obj.json_obj

        def set_kcp(self, kcp_obj):
            self.__stream_setiing['kcpSettings'] = kcp_obj.json_obj

        def set_tcp(self, tcp_obj):
            self.__stream_setiing['tcpSettings'] = tcp_obj.json_obj

        def set_web_socket(self, ws_obj):
            self.__stream_setiing['wsSettings'] = ws_obj.json_obj

        def set_http(self, http_obj):
            self.__stream_setiing['httpSettings'] = http_obj.json_obj

        def set_domain_socket(self, ds_obj):
            self.__stream_setiing['dsSettings'] = ds_obj.json_obj

        def set_quic(self, quic_obj):
            self.__stream_setiing['quicSettings'] = quic_obj.json_obj

        def set_sockopt(self, sockopt_obj):
            self.__stream_setiing['sockopt'] = sockopt_obj.json_obj

        class TLS(BaseConfig):
            def __init__(self, alpn=None):
                if alpn is None:
                    alpn = ["http/1.1"]

                self.__tls = {
                    "alpn": alpn,
                    "certificates": []
                }

                super().__init__(self.__tls)

            def add_alpn(self, alpn):
                self.__tls['alpn'].append(alpn)

            def set_server_name(self, name):
                self.__tls['serverName'] = name

            def set_allow_insecure(self, f):
                self.__tls['allowInsecure'] = f

            def add_certificate(self, usage="encipherment", **kwargs):
                cer = {
                    "usage": usage,
                }

                for key in kwargs:
                    cer[key] = kwargs[key]

                self.__tls['certificates'].append(cer)

        class TCP(BaseConfig):
            def __init__(self, masquerading=False, type=None, **kwargs):
                if masquerading is False:
                    self.__tcp = {
                        "type": "none"
                    }
                else:
                    self.__tcp = {
                        "type": type,
                        "request": {},
                        "response": {}
                    }
                super().__init__(self.__tcp, **kwargs)

            def set_request(self, request_obj):
                self.__tcp['request'] = request_obj.json_obj

            def set_response(self, response_obj):
                self.__tcp['response'] = response_obj.json_obj

            class HttpRequest(BaseConfig):
                def __init__(self, version="1.1", method="GET", path=None, headers=None, **kwargs):
                    self.__request = {
                        "version": version,
                        "method": method,
                        "path": [],
                        "headers": {}
                    }

                    if path is not None:
                        self.__request['path'].append(path)

                    if headers is not None:
                        self.__request['headers'] = headers

                    super().__init__(self.__request, **kwargs)

                def add_path(self, path):
                    self.__request['path'].append(path)

                def set_header(self, headers):
                    self.__request['headers'] = headers

            class HttpResponse(BaseConfig):
                def __init__(self, version="1.1", status="200", reason="OK", headers=None, **kwargs):
                    self.__response = {
                        "version": version,
                        "status": status,
                        "reason": reason,
                        "headers": {}
                    }

                    if headers is not None:
                        self.__response['headers'] = headers

                    super().__init__(self.__response, **kwargs)

        class KCP(BaseConfig):
            def __init__(self, mtu=1350, tti=50, uplink_capacity=5, download_capacity=20, congestion=False,
                         read_buffer_size=2, write_buffer_size=2, header_type="none"):
                self.__kcp = {
                    "mtu": mtu,
                    "tti": tti,
                    "uplinkCapacity": uplink_capacity,
                    "downlinkCapacity": download_capacity,
                    "congestion": congestion,
                    "readBufferSize": read_buffer_size,
                    "writeBufferSize": write_buffer_size,
                    "header": {
                        "type": header_type
                    }
                }
                super().__init__(self.__kcp)

        class WebSocket(BaseConfig):
            def __init__(self, path="/", headers=None):
                if headers is None:
                    headers = {}

                self.__web_socket = {
                    "path": path,
                    "headers": headers
                }

                super().__init__(self.__web_socket)

            def add_header(self, key, value):
                self.__web_socket['headers'][key] = value

        class Http(BaseConfig):
            def __init__(self, path="/"):
                self.__http = {
                    "host": [],
                    "path": path
                }
                super().__init__(self.__http)

            def add_host(self, host):
                self.__http['host'].append(host)

        class DomainSocket(BaseConfig):
            def __init__(self, filename):
                self.__domain_socket = {
                    "path": filename
                }

                super().__init__(self.__domain_socket)

        class Quic(BaseConfig):
            def __init__(self, security="none", key="", header_type=""):
                self.__quic = {
                    "security": security,
                    "key": key,
                    "header": {
                        "type": header_type
                    }
                }

                super().__init__(self.__quic)

        class Sockopt(BaseConfig):
            def __init__(self, mark=0, tcp_fast_open=False, tproxy="off"):
                self.__sockopt = {
                    "mark": mark,
                    "tcpFastOpen": tcp_fast_open,
                    "tproxy": tproxy
                }

                super().__init__(self.__sockopt)
