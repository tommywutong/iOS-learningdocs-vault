---
title: Sleep Queue Entry
apple_id: DTS10000019
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Sleep_Queue_Entry/Listings/SleepQ_c.html
archived_at: '2026-07-18T03:24:46.770067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sleep Queue Entry](Sleep%20Queue%20Entry.md)


[Next](Document%20Revision%20History.md)[Previous](Sleep%20Queue%20Entry.md)

# SleepQ.c

```c
/* This snippet demonstrates how to create a sleep queue entry under Think C */


#include "Power.h"
#include "SetUpa4.h"

pascal long MySleepQueueEntry(void);

SleepQRec gMySleepQStruct;

/*
  Here's where we install our sleep queue entry.  This is all
  by the book, as documented in Inside Mac volume VI.
*/
void InstallOurSleepQueueEntry()
{
    RememberA4();
    /* install our test routine in the sleep process queue */
    gMySleepQStruct.sleepQLink = 0;
    gMySleepQStruct.sleepQType = slpQType;
    gMySleepQStruct.sleepQProc = (ProcPtr) &MySleepQueueEntry;
    gMySleepQStruct.sleepQFlags = 0;

    SleepQInstall(&gMySleepQStruct);

}

/*  This routine can be called at any of four ways as indicated by D0.  
    When it's called, register A0 contains a pointer to our sleep queue record, 
    and register D0 contains a "what's happening" value:
    1 = sleep request (i.e. "Can I sleep?")
    2 = sleep demand (i.e. "You must sleep.")
    3 = wakeup demand (i.e. "You must wake up.")
    4 = sleep-request revocation (i.e. "I changed my mind about putting you to sleep.")

    Since Think C depends upon C calling conventions, you need special in-line
    assembly to handle this routine.
*/

pascal long MySleepQueueEntry(void)
{
    long        whatToDo;   /* passed to us in D0 */
    SleepQRec   *sqPtr;     /* passed to us in A0 */
    long        returnValue;

/* Important: These assembly instructions must be the first executable code
** in this routine, or you have the potential of changing D0 and/or A0 before
** you get a chance to save them.  Don't put any code before this asm statement!
*/
    asm {
            MOVE.L  D0, whatToDo
            MOVE.L  A0, sqPtr
    }

    SetUpA4();
    returnValue = 0;        /* 0 = okay whatever the system wants to do */

/* At this point, you'd do whatever you want to do at sleep time.
*/
    switch (whatToDo) {
        case sleepRequest:
            DebugStr("\pIn sleepRequest");
            break;
        case sleepDemand:
            DebugStr("\pIn sleepDemand");
            break;
        case sleepWakeUp:
            DebugStr("\pIn sleepWakeUp");
            break;
        case sleepRevoke:
            DebugStr("\pIn sleepRevoke");
            break;
    }

    RestoreA4();
/* Important: this asm statement must be the last executable code in this
** routine, or you won't return the proper value in D0.
*/
    asm {
            MOVE.L  returnValue, D0
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Sleep%20Queue%20Entry.md)

