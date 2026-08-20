---
title: LocalServer
apple_id: DTS10000701
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/LocalServer/Introduction/Intro.html
archived_at: '2026-07-18T03:13:44.732495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](LocalServerTCP-LocalServerClient-Carbon.r.md)

# LocalServer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Sample demonstrates how a Classic process can communicate with a Mac OS X process using IP networking protocols. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon (both 9 and X) Mac OS X 10.0.x, 10.1.5 and greater. This sample will not work properly with Mac OS X 10.1 through 10.1.4. |

This sample code demonstrates how a Classic process can communicate with a Mac OS X process using both TCP and UDP networking protocols. The UDP/TCP server is launched under Mac OS X and waits for a communication request (which the Classic client will initiate.) In order for the Classic client to know which port to use, it issues an AppleEvent request, which the server responds to with the port number to be used. Requirements: Mac OS X 10.0.x, 10.1.5 and greater. This sample will not work properly with Mac OS X 10.1 through 10.1.4. Keywords: Interprocess communications IPC Classic Server Client AppleEvents LocalServer

[Next](LocalServerTCP-LocalServerClient-Carbon.r.md)

