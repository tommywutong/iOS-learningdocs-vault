---
title: DNSServiceMetaQuery
apple_id: DTS10003330
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/DNSServiceMetaQuery/Introduction/Intro.html
archived_at: '2026-07-18T03:05:50.219677Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](DNSServiceMetaQuery.c.md)

# DNSServiceMetaQuery

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2005-06-01 Added "#include <sys/socket.h>" to fix compiler errors in Mac OS X 10.4. |
| __Build Requirements:__ | Xcode 1.0 or later |
| __Runtime Requirements:__ | Mac OS X 10.3 or later |

This sample uses DNSServiceQueryRecord to send a Multicast DNS query that returns a list of Bonjour service types being advertised on the local network. Machines must be running mDNSResponder-58.6 (Mac OS X 10.3.4) or later in order to respond to this query.

[Next](DNSServiceMetaQuery.c.md)

