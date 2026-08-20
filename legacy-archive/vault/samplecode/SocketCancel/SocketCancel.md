---
title: SocketCancel
apple_id: DTS10000717
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/SocketCancel/Introduction/Intro.html
archived_at: '2026-07-18T03:24:56.626388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Read%20Me%20About%20SocketCancel.txt.md)

# SocketCancel

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-08-10 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS X |

SocketCancel is a sample that shows how to use safely cancel threads that are blocked within BSD sockets calls. It uses a simple sockets abstraction layer that wraps a non-blocking data socket, a UNIX domain socket pair that's used to signal cancellation, and creative use of the select system call.

[Next](Read%20Me%20About%20SocketCancel.txt.md)

