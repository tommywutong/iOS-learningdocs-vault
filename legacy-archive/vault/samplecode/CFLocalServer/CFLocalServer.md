---
title: CFLocalServer
apple_id: DTS10003652
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: CoreFoundation
published: '2005-07-26'
source_url: https://developer.apple.com/library/archive/samplecode/CFLocalServer/Introduction/Intro.html
archived_at: '2026-07-18T03:02:26.709946Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Client.c.md)

# CFLocalServer

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2005-07-26 This sample code has been updated to include a project (for Xcode 2.1) to produce a universal binary and there were no code changes required for it to run correctly on the Developer Transition Systems. |
| __Build Requirements:__ | Xcode 1.5 or later |
| __Runtime Requirements:__ | Mac OS X |

CFLocalServer is a sample that shows how to use UNIX domain sockets to communicate between client and server programs running on the same machine. This sample was written specifically to show how a daemon can manage communication with multiple clients. It supports RPC communications (where the client makes a request to server and blocks waiting for a reply) and asynchronous notification (where the server sends messages to all clients). It wraps each UNIX domain socket in a CFSocket to demonstrate the integration of UNIX domain sockets with a run-loop based program.
CFLocalServer should work on all versions of Mac OS X, but it has been primarily tested on Mac OS X 10.4.x.

[Next](Client.c.md)

