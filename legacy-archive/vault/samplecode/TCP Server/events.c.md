---
title: TCP Server
apple_id: DTS10000264
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP_Server/Listings/events_c.html
archived_at: '2026-07-18T03:26:01.759889Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP Server](TCP%20Server.md)


[Next](events.h.md)[Previous](const.h.md)

# events.c

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
#include "interface.h"
#include "network.h"
#include "queues.h"
#include "events.h"

/*  event handling routine for dispatching non-null events.
    we don't have much of a human interface, so we only handle
    mousedowns.
*/

void HandleEvent(EventRecord *ev)
{
    if (HandleDialogEvents(ev))
        return;

    switch (ev->what) {
        case mouseDown:
            HandleMouseDown(ev->where);
            break;
    }
}


/*  event handling routine for null-events.  this is where we check the queues
    to see if we have anything in the "completed" queue.  if so, we call
    ProcessConnection with the queue element parameter block which we receive,
    and update our queue counter display.
*/

void HandleIdleTime(EventRecord *ev)
{
    MyQElemPtr pBlock;

    HandleDialogEvents(ev);
    UpdateNumberList();

    while (pBlock = GetCompletedPBlock()) {
        ProcessConnection(pBlock);
    }

    UpdateNumberList();
}
```

[Next](events.h.md)[Previous](const.h.md)

