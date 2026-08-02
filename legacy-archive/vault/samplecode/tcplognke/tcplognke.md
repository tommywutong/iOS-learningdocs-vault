---
title: tcplognke
apple_id: DTS10003669
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-11-27'
source_url: https://developer.apple.com/library/archive/samplecode/tcplognke/Introduction/Intro.html
archived_at: '2026-07-26T19:53:51.294173Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](tcplog.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# tcplognke

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2006-11-27 Provide IPv6 support [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrwhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.4 or greater and Xcode 2.2 or greater |
| __Runtime Requirements:__ | Mac OS X 10.4 or greater |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

The tcplognke demonstrates the implementation of a network socket filter for processing incoming and outgoing http packets using the new Kernel Programming Interfaces provided in OS X 10.4. The sample demonstrates the following
1. use of the fine grain locking API's to serialize access to data queues,
2. the mbuf tag calls for tracking processing of mbufs by kernel extension code,
3. how the kernel process can "swallow" a packet and re-inject the packet at a later time,
4. the implementation of each of the intercept functions for a socket filter kernel process,
5. the use of the system control socket for communications between a kernel process and user level process,
6. produces a Universal Binary.

[Next](tcplog.c.md)

