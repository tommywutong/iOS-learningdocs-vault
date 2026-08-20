---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_QTMusic_Sample_Sequencer_Event_Priority_Queue_h.html
archived_at: '2026-07-18T03:21:07.721437Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-Sequencer%20Test%20Movies.c.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-Event%20Priority%20Queue.c.md)

# •QTMusic Sample Sequencer/Event Priority Queue.h

```c
/*
    File:       Event Priority Queue.h

    Contains:   xxx put contents here xxx

    Written by: xxx put writers here xxx

    Copyright:  © 1992 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <3+>     5/19/93    dvb     New calls for sorting.
         <3>     9/17/92    dvb     Flush call
        <1+>     5/11/92    dvb     It's mine, and I'm going to work on it.
         <1>     5/10/92    dvb     first checked in

*/

/*
 * file: Event Priority Queue.h
 *
 *
 */


#ifndef _EventPriorityQueue_
#define _EventPriorityQueue_



/*--------------------------
    Inclusions
--------------------------*/

#include <types.h>

/*--------------------------
    Structures
--------------------------*/
typedef struct
    {
    long time;
    long data1;
    long data2;
    long data3;
    } EPQEvent;

typedef struct
    {
    long size;      /* number of Events in queue */
    long maxSize;   /* number of Events possible */
    EPQEvent e[1];
    } EPQ;

#define kEPQEmpty 0x7fffFFFF

/*--------------------------
    Prototypes
--------------------------*/

EPQ *NewEPQ(long maxSize);
short DisposeEPQ(EPQ *q);

short AddEventEPQ(EPQ *q, const EPQEvent *inEvent);
long PeekTopEPQ(EPQ *q);
EPQEvent *PeekIndexedEPQ(EPQ *q,long index);
long GetSizeEPQ(EPQ *q);
void ExtractEventEPQ(EPQ *q, EPQEvent *outEvent);
void FlushEPQ(EPQ *q);
void SortEPQ(EPQ *q);



#endif _EventPriorityQueue_
```

[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-Sequencer%20Test%20Movies.c.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-Event%20Priority%20Queue.c.md)

