---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL3/NSL3.html
archived_at: '2026-07-15T08:18:17.574724Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](NSL32.md)[Previous](Tasks.md)

# Introduction to Network Services Location Manager

|  |  |
| --- | --- |
| __Declared in__ | NSL.h NSLCore.h |

The Network Services Location Manager is an API that allows applications to locate network services. The high-level function, `NSLStandardGetURL`, automatically searches services, displays the search results in a dialog box, and allows the user to select a URL. The other high-level functions, `NSLStandardRegisterURL` and `NSLStandardDeregisterURL`, register and deregister services so they can be located by applications that search for them. Unlike the high-level Network Services Location Manager functions, the low-level Network Services Location Manager functions require you to open an session with the Network Services Location Manager, prepare search requests, check for search results, and, close the Network Services Location Manager session. The Network Services Location Manager also provides utility functions for manipulating Network Services Location Manager data types.

[Next](NSL32.md)[Previous](Tasks.md)

