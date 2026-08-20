---
title: PPPoE Server for Testing
apple_id: DTS10002288
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2011-07-27'
source_url: https://developer.apple.com/library/archive/qa/qa1252/_index.html
archived_at: '2026-07-18T02:30:17.906275Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1252

# PPPoE Server for Testing

## Q:  I'm writing some Internet setup assistant software. I would like to test my PPPoE setup code, but I don't have access to a PPPoE concentrator. Can I use Mac OS X as a PPPoE server for testing?

A: Yes you can. Enter the following two command lines into a Terminal window on the machine you want to act as a PPPoE server.


```
sudo sysctl -w net.inet.ip.forwarding=1 sudo pppd plugin PPPoE.ppp noauth debug nodetach persist holdoff 1 \ mru 1492 mtu 1492 proxyarp pppoemode listen 10.0.0.32:10.0.0.64 \ ms-dns 17.128.100.9
```

The first command line enables IP forwarding on your machine. Without this, the PPPoE client will only be able to talk to the PPPoE server itself.

Each element of the second command line is explained below:

- The `sudo` command causes `pppd` to run with privileges, which is necessary to start a PPPoE server in this way.
- `pppd` is the name of the PPP daemon program on Mac OS X.
- The `plugin PPPoE.ppp` option causes `pppd` to load the PPPoE plug-in.
- The `noauth` option allows any client to connect to your PPPoE server without authentication. Take heed of the warning above.
- The `debug` option causes `pppd` to log the contents of control packets to the Terminal window.
- Normally `pppd` will detach from its controlling terminal and run in the background. The `nodetach` option prevents this, which is useful because you can then quit `pppd` by typing ^C.
- The `persist` option prevents `pppd` from terminating when the client disconnects. This is useful when debugging because you can connect and disconnect the client as many times as you like without having to touch the server.
- The `holdoff 1` option causes `pppd` to resume listening for connections one second after the connection terminates.
- The Maximum Receive Unit (MRU) and Maximum Transmit Unit (MTU) values are set using the options `mru 1492 mtu 1492`. These are the standard values for PPPoE.
- The `proxyarp` option will allow the client to communicate with machines other than the PPPoE server itself. You need this if you want to connect to other machines on the Internet from the PPPoE client.
- The `pppoemode listen` option forces `pppd` to listen for incoming connections.
- The `10.0.0.32:10.0.0.64` option specifies the local and remote IP addresses for the PPP connection. Both should be unused IP addresses on the local subnet of the PPPoE server. The first will be used as the local address of the PPP connection. The second forms the remote address of the PPP connection; it will be handed out to the PPP client. This example uses 10.0.0.z addresses, which would be appropriate if you were behind a NAT router.
- The `ms-dns 17.128.100.9` option allows you to specify the IP address of a DNS server that `pppd` will pass to the client (using IPCP options 129 and 131 as documented in RFC 1877). This eliminates the need for you to configure DNS on the client by hand. You should replace 17.128.100.9 with the IP address of a DNS server appropriate for your network.

After you have run this command line on the server, you should be able to create a basic PPPoE configuration on the client, run Internet Connect, and connect to your server.

For more details about these `pppd` options, enter `man pppd` into Terminal.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-27 | Reformatted content and made minor editorial changes. |
| 2003-04-11 | New document that describes how to configure Mac OS X as a PPPoE server for testing purposes. |

