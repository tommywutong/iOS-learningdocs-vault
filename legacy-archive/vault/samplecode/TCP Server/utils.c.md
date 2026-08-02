---
title: TCP Server
apple_id: DTS10000264
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP_Server/Listings/utils_c.html
archived_at: '2026-07-18T03:26:02.377672Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP Server](TCP%20Server.md)


[Next](utils.h.md)[Previous](queues.h.md)

# utils.c

```c
/*
    TCP Client/Server Queuing Example
    Steve Falkenburg, MacDTS, Apple Computer
    3/11/92

    this client/server sample uses MacTCP to implement a simple "greeting" server.  the server
    opens up several listeners on kGreetingPort (1235).  when a client connects, the data entered
    in the greeting dialog is sent to the remote connection, and the connection is closed.

    connection management is done through the use of Operating System queues to simplify tracking
    and usage.
*/


#include "const.h"
#include "globals.h"
#include "utils.h"


/* called in response to errors.  we just do a debugstr here */

void DoError(OSErr err)
{
    Str255 errStr;

    NumToString(err,errStr);
    DebugStr(errStr);
}
```

[Next](utils.h.md)[Previous](queues.h.md)

