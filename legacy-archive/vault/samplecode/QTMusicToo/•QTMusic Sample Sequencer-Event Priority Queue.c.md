---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_QTMusic_Sample_Sequencer_Event_Priority_Queue_c.html
archived_at: '2026-07-18T03:21:07.631337Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-Event%20Priority%20Queue.h.md)[Previous](%E2%80%A2QTMusic%20Sample%20Keyboards-QTMusic%20Sample%20Keyboards.r.md)

# •QTMusic Sample Sequencer/Event Priority Queue.c

```c
/*
    File:       Event Priority Queue.c

    Contains:   Event-ordering routines

    Written by: dvb, based on classic algorithms. read the book, see the movie.

    Copyright:  © 1992-1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <10>     24-8-94    dvb     Fix write to nil.
         <9>      9-8-94    dvb     zero out new queues, use longs only
         <8>      6/4/94    PH      return an error
         <7>     7/13/93    dvb     Test... again.
         <6>     7/13/93    dvb     
         <5>     7/13/93    dvb     -d
         <4>     7/13/93    dvb     -d < Death By Seven:System Folder:OldComment
        <2+>     5/19/93    dvb     New calls for sorting.
         <2>     9/17/92    dvb     Flush call
         <1>     5/10/92    dvb     first checked in
         <0+>    5/10/92    dvb     first checked in

*/


/*
 * file: Event Priority Queue.c
 *
 * This is an "ascending" priority queue,
 * only the smallest event will be extracted.
 *
 * Started 6 May 1992, David Van Brink
 */



/*
 * Quick C. S. refresher...
 *
 * This is implemented as a balanced tree
 * with the Property that every node is
 * marked with an earlier time than its
 * descendants. The tree is stored as
 * an array, with the relationships of
 * Parent and Child as #defined below.
 *
 * To insert a new event, we add it at
 * the end of the array (the bottom of
 * the tree) and bubble it up as needed
 * to maintain the Property. Time: lg2(n).
 *
 * To extract the next event, we take
 * the root of the tree (event[0]) and
 * then bubble around the innards as
 * needed. Time: lg2(n).
 *
 * I figure we can juggle a few hundred or
 * thousand events this way with reasonable performance.
 */



/*--------------------------
    Inclusions
--------------------------*/

#include <Memory.h>

#include "Event Priority Queue.h"

/*--------------------------
    Local Prototypes
--------------------------*/

#define LeftChild(x) ((x)+(x)+1)
#define RightChild(x) (LeftChild(x)+1)
#define Parent(x) (((x) - 1)>>1)


/*--------------------------
    Them Routines
--------------------------*/


EPQ *NewEPQ(long maxSize)
    {
    EPQ *q;

    q = (void *)NewPtrClear(sizeof(EPQ) + maxSize * sizeof(EPQEvent));
    if(q)
        {
        q->size = 0;
        q->maxSize = maxSize;
        }

    return q;
    }

short DisposeEPQ(EPQ *q)
    {
    if(q)
        DisposePtr((void *)q);
    return noErr;
    }


short AddEventEPQ(EPQ *q, const EPQEvent *inEvent)
/*
 * This routine must be indivisible, since Events
 * will be extracted at interrupt level.
 *
 * This routine could be nicely optimized.
 */
    {
    long index, parent;
    EPQEvent e;
    register long time;
    register EPQEvent *pptr,*iptr;

    if(q->size == q->maxSize)
        return -1;                  /* error */

    time = inEvent->time;
    index = q->size;

    if(index)
        {
        iptr = &q->e[index];
        goto x;
        }
loop:
    if(index != 0)
        {
    x:
        parent = Parent(index);
        pptr = &q->e[parent];
        if(time < pptr->time)
            {
            q->e[index] = *pptr;
            index = parent;
            iptr = pptr;
            goto loop;
            }
        }

    q->e[index] = *inEvent;
    ++ q->size;

    return 0;
    }

long PeekTopEPQ(EPQ *q)
    {
    if(q->size)
        return q->e[0].time;
    else
        return kEPQEmpty;
    }

long GetSizeEPQ(EPQ *q)
    {
    return q->size;
    }



void ExtractEventEPQ(EPQ *q, EPQEvent *outEvent)
    {
    register long index,left,right;
    register long size;
    register long temp;
    register EPQEvent *i,*l,*r;
//  EPQEvent tempE;

    *outEvent = q->e[0];

    size = --q->size;

    if(!size)
        goto done;

    q->e[0] = q->e[size];

    index = 0;
    i = &q->e[0];

    while(index < size)
        {
        left = LeftChild(index);

        /*
         * step 1: put the smaller of left or right into L ptrs
         */
        if(left >= size)
            goto done;

        right = left + 1;
        l = &q->e[left];
        r = l+1;

        if( (right <= size)
                && (r->time < l->time) )
            {
            left = right;
            l = r;
            }

        /*
         * step 2: is i smaller than either of them? if so, done.
         */
        if(i->time < l->time)
            goto done;

        #define swapit(a) \
            temp = i->a; \
            i->a = l->a; \
            l->a = temp

        swapit(time);
        swapit(data1);
        swapit(data2);
        swapit(data3);

        i = l;
        index = left;
        }

done:;
    }



void FlushEPQ(EPQ *q)
    {
    if(q)
        q->size = 0;
    }


void SortEPQ(EPQ *q)
/*
 * Sort the elements and
 * put in the top of the
 * event array.
 */
    {
    EPQEvent e;
    EPQEvent *w;

    w = &q->e[q->maxSize];

    while(q->size)
        {
        ExtractEventEPQ(q,&e);
        --w;
        *w = e;
        }
    }

EPQEvent *PeekIndexedEPQ(EPQ *q,long index)
/*
 * Positive index 0-max, or
 * negative index to look at elements
 * after sorting.
 */
    {
    if(index >= 0)
        return &q->e[index];
    else
        return &q->e[q->maxSize + index];
    }
```

[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-Event%20Priority%20Queue.h.md)[Previous](%E2%80%A2QTMusic%20Sample%20Keyboards-QTMusic%20Sample%20Keyboards.r.md)

