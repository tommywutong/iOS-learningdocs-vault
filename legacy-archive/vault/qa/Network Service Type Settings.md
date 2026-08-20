---
title: Network Service Type Settings
apple_id: DTS40017544
resource_type: QA
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2016-09-14'
source_url: https://developer.apple.com/library/archive/qa/qa1934/_index.html
archived_at: '2026-07-18T02:37:14.804042Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1934

# Network Service Type Settings

## Q:  How do I ensure my iOS app's network traffic can be optimized across Cisco networks?

A: Networking hardware such as routers and switches may be configured to optimize various types of data traversing a network.

In iOS, specifying the appropriate network service type on the network connections used in your app will allow network administrators to configure their devices to optimize throughput of your data based on its type.

You set the service type property by using the following networking APIs:

- For `CFSocketStream` set `kCFStreamNetworkServiceType`.
- For `NSStream`, use `NSStreamNetworkServiceType`.
- For `Stream`, use `StreamNetworkServiceType`.
- For UDP sockets, use `SO_NET_SERVICE_TYPE`.

Choose the appropriate service type for your app:

- Specifying the `background` type allows your traffic for this connection to be delayed to yield to traffic of other types.
- Specifying `video` and `voice` types imply your app provides a telephony service of sorts where the type of traffic is interactive voice or interactive video.
- Specifying no service type means your traffic will be prioritized as best effort.

When choosing the right service type for your app, it is important to keep in mind the following:

- Since network equipment is optimized for best effort, the vast majority of your app traffic should use the default network service type.
- Choosing low latency service types like voice or video will not increase bandwidth.
- Choosing voice or video types for bulk transfer of data will cause packet loss.
- While setting a service type value doesn't guarantee it will optimized, it does ensure that it is able to be optimized at the determination of the network administrator.

For a more details on traffic optimization and the latest guidance on networking on iOS, be sure to check out the [Networking for the Modern Internet](https://developer.apple.com/videos/play/wwdc2016/714/) session from WWDC.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-09-14 | New document that describes how to set appropriate service types to ensure the possibility of network optimization. |

