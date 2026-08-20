---
title: Mixing link-local IP addresses and routable IP addresses
apple_id: DTS10003346
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2005-07-06'
source_url: https://developer.apple.com/library/archive/qa/qa1357/_index.html
archived_at: '2026-07-18T02:30:26.129558Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1357

# Mixing link-local IP addresses and routable IP addresses

## Q:  How can I configure my computer to communicate with devices which use link-local IP addresses when my computer is using a routable IP address? How can I configure my computer to communicate with devices which use routable IP addresses when my computer is using a link-local IP address?

A: How can I configure my computer to communicate with devices which use link-local IP addresses when my computer is using a routable IP address? How can I configure my computer to communicate with devices which use routable IP addresses when my computer is using a link-local IP address?

The answer depends on what operating system you're using.

__Mac OS X__

No configuration is necessary. Mac OS X already knows that 169.254/16 is defined to be link-local, and packets addressed to destinations in that range will be sent directly to the device on the local link, not sent to a gateway for forwarding off-link. When Mac OS X is using a link-local address, it ARPs for everything, so a Mac OS X machine using link-local can also communicate with devices using non-link-local addresses. Note however that if you are using multiple interfaces at the same time, link-local addressing is only active on the primary interface (the one that appears first in the list in the Network Preference Panel). This restriction may be lifted in the future, but if the world moves to adopt IPv6 as rapidly as we'd like, questions about IPv4 may become moot, because IPv6 already supports link-local addresses on every interface.

__Windows__

Windows has supported IPv4 link-local addressing since Windows 98, but communication between link-local and routable IP addresses is not automatically enabled as required by [RFC 3927](http://www.ietf.org/rfc/rfc3927.txt). The following commands, typed at a DOS prompt, will enable mixed-network communication on Windows. In place of "put_my_address_here" and "put_my_link_local_address_here", put the Windows machine's own IP addresses.


```
route add 169.254.0.0 mask 255.255.0.0 put_my_address_here route add 0.0.0.0 mask 0.0.0.0 put_my_link_local_address_here
```

Note that because these commands need to include your current routable or link-local IP address, you would have to re-do the commands every time your IP address changes. Therefore, the commands listed here are most useful for developers creating hardware products that use [Bonjour](https://developer.apple.com/networking/bonjour/index.html), not for end users. When you install [Bonjour for Windows](http://www.apple.com/support/downloads/bonjourforwindows.html), these routing table settings are automatically installed and maintained for you.

__Linux__

Most modern Linux distributions already include full IPv4 link-local support. Older Linux distributions (and similar Unix systems) that don't know how to route to link-local can be manually configured to send link-local packets directly to local devices with two simple commands, as shown below. If your primary interface is not "eth0" then substitute the name of your primary interface instead.


```
route add -net 169.254.0.0 netmask 255.255.0.0 dev eth0 metric 99 route add default dev eth0 metric 99
```

The first command says "if you don't know better, route link-local directly to Ethernet", and the second says, "if you don't know better, then route everything directly to Ethernet". The "metric 99" means that these routes are low priority. If there's any routing table entry with a higher priority (for example, metric 0), it takes precedence. That means it's safe to add these to rc.local and have them \*always\* be active, because they only take effect when there is no higher priority routing table entry to tell the kernel what to do. You can put these two commands in your `/etc/rc.local` file to execute at startup time.

For Linux distributions that use the `/etc/sysconfig/static-routes` file, you can put the following two lines in that file instead of using the route commands above.


```
eth0 net 169.254.0.0 netmask 255.255.0.0 metric 99 eth0 net 0.0.0.0 netmask 0.0.0.0 metric 99
```

These two lines tell the Linux kernel that 169.254/16 is defined to always be on the local link, no matter what, and if there's some other address that you have no idea how to reach, then it's at least worth a try to see if it's reachable on the local link.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-07-06 | New document that explains how to enable communication between devices with link-local addresses and devices with routable addresses. |

