---
title: DispatchLife
apple_id: DTS40007759
resource_type: Sample Code
platform: macOS
topic: Performance
technology: null
published: '2009-05-29'
source_url: https://developer.apple.com/library/archive/samplecode/DispatchLife/Introduction/Intro.html
archived_at: '2026-07-18T03:07:01.141806Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# DispatchLife

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2009-05-29 Updated for new libdispatch APIs |
| __Build Requirements:__ | Mac OS X version 10.6 Snow Leopard |
| __Runtime Requirements:__ | Mac OS X version 10.6 Snow Leopard |

The classic game of Life showing use of dispatch queues as lightweight threads (each cell is a queue), and an example of how to avoid overloading a slow queue (OpenGL or curses screen updates) with many requests (cell updates) by using a timer to drive the screen updates and allowing the cells to update as fast as they can.

[Next](ReadMe.txt.md)

