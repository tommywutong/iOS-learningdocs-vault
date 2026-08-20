---
title: TCP Server
apple_id: DTS10000264
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP_Server/Listings/queues_h.html
archived_at: '2026-07-18T03:26:02.348583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP Server](TCP%20Server.md)


[Next](utils.c.md)[Previous](queues.c.md)

# queues.h

```
/*
    TCP Client/Server Queuing Example
    Steve Falkenburg, MacDTS, Apple Computer
    3/11/92
*/

void InitQueues(void);

MyQElemPtr GetUnusedPBlock(void);
void RecycleFreePBlock(MyQElemPtr pBlock);
MyQElemPtr GetCompletedPBlock(void);
void StoreCompletedPBlock(MyQElemPtr pBlock);
```

[Next](utils.c.md)[Previous](queues.c.md)

