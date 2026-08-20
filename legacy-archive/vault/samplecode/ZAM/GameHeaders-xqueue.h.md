---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_xqueue_h.html
archived_at: '2026-07-18T03:28:32.820746Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-xthing.h.md)[Previous](GameHeaders-TankSprite.h.md)

# GameHeaders/xqueue.h

```c
#pragma once
#include <Retrace.h>

typedef struct xQHdr {      
    long            qFlags;
    struct xthing   *qHead;
    struct xthing   *qTail;
    short           qEntries;
} xQHdr;

typedef Boolean (*updateProc)(struct xthing *xtp);

typedef struct xthing {
    VBLTask         timer;          /* update time */
    QElem           *xqel;          /* link in xthing queue */
    short           prime;          /* number of miliseconds between runs */
    xQHdr           *uQueueRef;     /* handy place to put your gum */
    long            flags;          /* indicating stuff */
    long            refcon;
    updateProc      updtProc;
    ProcPtr         vTaskPtr;
} xthing;


void xInitQueueHeader(xQHdr *queue);
void xEnqueue(xthing *qel, xQHdr *queue);
void xDequeue(xthing *qel, xQHdr *queue);

#ifndef nil
#define nil ((void*)0L)
#endif
```

[Next](GameHeaders-xthing.h.md)[Previous](GameHeaders-TankSprite.h.md)

