# Shadowray
A useful client of v2ray for linux

## Simple use
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

## Usage
### Basic config
+ subscribe.json : the file used to save subscribes,you can specify it by using `shadowray --config-subscribe <path>`,but the file must be created by yourself
+ servers.json : the file used to save servers,you can specify it by using `shadowray --config-servers <path>`,but the file must be created by yourself
+ v2ray : you should specify the folder of v2ray-core,using `shadowray --config-v2ray <path>

### For simplicity
Using `shadowray --autoconfig`,then it will complete the basic config automatically,include the downloading the lasted v2ray-core

### Subscribe
#### Add a subscribe
you can use `shadowray --subscribe-add '<name>,<url>'` to add a subscribe.
> Don't forget the `''`

#### Update subscribes
Using `shadowray --subscribe-update` to update all subscribes.

### Proxy
#### List server
To see all available servers(proxies),using `shadowray [--list|-l]`.Then you will see some index,name of proxies,protocol of proxies,the index of proxies used to start a proxy

#### Start a proxy
For starting a proxy,you can use 'shadowray [--start|-s] <index>'
