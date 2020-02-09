# Notice
This project has stopped. You can use [Clash](https://github.com/Dreamacro/clash) and [subconverter](https://github.com/tindy2013/subconverter) to implement the same effect, and they can do better.
# Shadowray
An useful client of v2ray for linux

## Simple usage
```bash
pip install shadowray
shadowray --autoconfig
shadowray --subscribe-add 'name,url'
shadowray --list
shadowray -s 1
```
for more detail about command:
```bash
shadowray --help
```
### Default config
#### Inbound:
+ protocol : socks5
+ port: 1082
+ auth: noauth
#### Outbound:
+ Traffic camouflage : tcp
## Usage
### Basic config
+ subscribe.json : the file used to save subscribes,you can specify it by using `shadowray --config-subscribe <path>`,but the file must be created by yourself
+ servers.json : the file used to save servers,you can specify it by using `shadowray --config-servers <path>`,but the file must be created by yourself
+ v2ray : you should specify the folder of v2ray-core,using `shadowray --config-v2ray <path>`

### For simplicity
Using `shadowray --autoconfig`,then it will complete the basic config automatically,include that downloading the lasted v2ray-core

### Subscribe
#### Add a subscribe
you can use `shadowray --subscribe-add '<name>,<url>'` to add a subscribe.
> Don't forget the `''`

#### Update subscribes
Using `shadowray --subscribe-update` to update all subscribes.Meanwhile,you can use `--port <number>` to specify a port of inbound.

### Proxy
#### List server
To see all available servers(proxies),using `shadowray [--list|-l]`.Then you will see some index,name of proxies,protocol of proxies,the index of proxies used to start a proxy

#### Start a proxy
For starting a proxy,you can use `shadowray [--start|-s] <index>`
> For running v2ray as a daemon,by using `--daemon` or `-d`
#### Stop daemon
Using  `shadowray --stop`
### Specify a config file of v2ray
You can use your config file via `[--config-self|-f] <path>`.For example,
`shadowray --config-self ~/config.json` or `shadowray -f ~/config.json`
### Export config
Using `shadowray --servers-export <index>:<path>` to export the specified config to file that specified by <path>
