---
title: VMSify
apple_id: DTS10000271
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/VMSify/Introduction/Intro.html
archived_at: '2026-07-18T03:27:40.838114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](VMSify.c.md)

# VMSify

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

VMSify is a sample STREAMS module that actually does something useful (well, noticable). VMSify is largely derived from the StreamNOP source, but it is extended to demonstrate simple address detection and data munging. VMSify's functionality is relatively silly. It detects whether the stream is a telnet session (looking for outgoing connections on port 23) and, if it is, upper cases all the data returned from the server. The upshot is that if you install the software and log into a UNIX machine using a Mac OS telnet application, all the returned text is in upper case, just like it would be if you were logging into a VMS machine. Open Transport 1.1.1 or higher STREAMS plug-in, STREAMS module, Open Transport, autopush

[Next](VMSify.c.md)

