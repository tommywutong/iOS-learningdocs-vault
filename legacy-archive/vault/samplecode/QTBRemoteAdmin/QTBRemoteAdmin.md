---
title: QTBRemoteAdmin
apple_id: DTS10001045
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTBRemoteAdmin/Introduction/Intro.html
archived_at: '2026-07-18T03:19:59.627273Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Source-BroadcasterAdminCGI-BroadcasterAdminHTML.h.md)

# QTBRemoteAdmin

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how one might write a remote administration tool for QuickTime Broadcaster. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS X |

This sample code demonstrates how one might write a remote administration tool for QuickTime Broadcaster. QuickTime Broadcaster uses Cocoa's distributed objects to support remote administration. It uses Mach ports which, for security reasons, require the remote admin tool to run in the same user context as QuickTime Broadcaster. This example uses a daemon (which must be run in the same user context as QuickTime Broadcast) to communicate to a cgi which runs in a different user context. The daemon acts as a proxy and passes messages between the cgi and QuickTime Broadcaster. The connection between QuickTime Broadcaster and the daemon is secure, the connection between the daemon and the cgi is not, however. A real world implementation to be used by customers would have to provide some form of security so that anyone can't connect to the daemon and control QuickTime Broadcaster. Requirements: Mac OS X Keywords: QuickTime Broadcaster Remote Administration

[Next](Source-BroadcasterAdminCGI-BroadcasterAdminHTML.h.md)

