---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_xthing_h.html
archived_at: '2026-07-18T03:28:32.848927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-ZAM.h.md)[Previous](GameHeaders-xqueue.h.md)

# GameHeaders/xthing.h

```c
#pragma once
#include <Timer.h>

#define TaskActiveFlag 0x8000

typedef struct xQHdr {      
    long            qFlags;
    struct xthing   *qHead;
    struct xthing   *qTail;
    short           qEntries;
} xQHdr;

typedef Boolean (*updateProc)(struct xthing *xtp, long dataRef);

typedef struct xthing {
    TMTask          timer;          /* update time */
    struct xthing   *next;          /* link in xthing queue */
    long            prime;          /* number of miliseconds between runs */
    Boolean         taskFlag;       /* flag set when task is ready to fire */
    Boolean         waiting;        /* true if put in list with a task launched */
    Boolean         inList;         /* set after task is first added */
    long            dataRef;        /* handy place to put your gum */
    long            interval;       /* the interval between runs */
    updateProc      actionProc;     /* pointer to task service routine */
} xthing;


void xInitQueueHeader(xQHdr *queue);
void xEnqueue(xthing *qel, xQHdr *queue);
void xDequeue(xthing *qel, xQHdr *queue);

xthing *StartXThing(xthing *xtp, long prime, updateProc updtProc, long dataRef);
void ProcessXThingTask(short numTasksToProcess);
void InitXThingTask(void);
void KillAllXThingTasks(void);

void AddXThing(xthing *xtp, long prime, updateProc updtProc, long dataRef);
void EnqueueXThing(xthing *xtp);
```

[Next](GameHeaders-ZAM.h.md)[Previous](GameHeaders-xqueue.h.md)

