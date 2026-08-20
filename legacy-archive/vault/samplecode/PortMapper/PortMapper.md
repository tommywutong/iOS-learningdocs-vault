---
title: PortMapper
apple_id: DTS40007879
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2008-07-25'
source_url: https://developer.apple.com/library/archive/samplecode/PortMapper/Introduction/Intro.html
archived_at: '2026-07-18T03:19:23.379705Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# PortMapper

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2008-07-25 Demonstrates Bonjour's NAT port-mapping API, and provides a higher-level Objective-C interface to it. |
| __Build Requirements:__ | Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

Bonjour (in Mac OS X 10.5 or later) provides a "port-mapping" facility, which allows a computer behind a Network Address Translator (NAT), such as a typical home router, to request a public TCP or UDP port number that can accept connections from outside. This allows the client to join peer-to-peer networks, or to provide a publicly-available service such as a Web server.

In 10.5 this facility is only available via the low-level <dnssd.h> header, and as such, using it requires familiarity with POSIX networking APIs (socket descriptors, sockaddrs, etc.) It also has no formal documentation, although there are extensive comments in the header file.

This sample code demonstrates how to use the API. It provides a complete Objective-C wrapper class that can be used as-is in Cocoa applications; or the innards of the class can be taken as snippets to use in other contexts.

[Next](main.m.md)

