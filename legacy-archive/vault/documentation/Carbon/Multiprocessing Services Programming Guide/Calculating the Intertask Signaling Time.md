---
title: Multiprocessing Services Programming Guide
apple_id: TP40000853
resource_type: Guide
platform: macOS
topic: null
technology: CoreServices
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Multitasking_MultiproServ/appendixb/appendixb.html
archived_at: '2026-07-15T05:23:37.848442Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Multiprocessing Services Programming Guide](Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md)


[Next](Changes%20From%20Previous%20Versions%20of%20Multiprocessing%20Services.md)[Previous](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md)

# Calculating the Intertask Signaling Time

When using Multiprocessing Services tasks, the amount of time used by the task should be much greater than the time taken to pass notifications to the task. This intertask signaling time is generally between 20 and 50 microseconds. If you want to explicitly calculate the signaling time, you can use the code in Listing B-1 to do so.

__Listing B-1__  Calculating the intertask signaling time

```c
#include <Multiprocessing.h>

#include <Types.h>
#include <stdio.h>
#include <stdlib.h>
#include <sioux.h>
#include <math64.h>
#include <DriverServices.h>


enum  {
    aQueue = 0,
    aSemaphore,
    anEvent
} reflectOP;

MPOpaqueID waiterID, postID;


static OSStatus Reflector ( )
{
    void    *p1,*p2,*p3;
    MPEventFlags events;

    while (true)
    {
        switch (reflectOP)
        {
            case aQueue:
                MPWaitOnQueue((MPQueueID) waiterID, &p1, &p2, &p3, kDurationForever);
                break;

            case aSemaphore:
                MPWaitOnSemaphore((MPSemaphoreID) waiterID, kDurationForever);
                break;

            case anEvent:
                MPWaitForEvent((MPEventID) waiterID, &events, kDurationForever);
                break;

            default:
                return -123;
        }

        switch (reflectOP)
        {
            case aQueue:
                MPNotifyQueue((MPQueueID) postID, &p1, &p2, &p3);
                break;

            case aSemaphore:
                MPSignalSemaphore((MPSemaphoreID) postID);
                break;

            case anEvent:
                MPSetEvent((MPEventID) postID, 0x01010101);
                break;

            default:
                return -123;
        }
    }

    return -123;
}


static float HowLong(
    AbsoluteTime endTime,
    AbsoluteTime bgnTime
    )
{
    AbsoluteTime absTime;
    Nanoseconds  nanosec;

    absTime = SubAbsoluteFromAbsolute(endTime, bgnTime);
    nanosec = AbsoluteToNanoseconds(absTime);
    return (float) UnsignedWideToUInt64( nanosec ) / 1000.0;
}


void main ( void )
{
    OSStatus            err;
    MPTaskID            task;
    UInt32              i, count;
    void                *p1,*p2,*p3;
    MPEventFlags events;
    AbsoluteTime nowTime, bgnTime;
    float               uSec;
    char                buff[10];


    /* Set the console window defaults */
    /* (this is a Metrowerks CodeWarrior thing). */
    SIOUXSettings.autocloseonquit    = true;
    SIOUXSettings.asktosaveonclose  = false;
    SIOUXSettings.showstatusline    = false;
    SIOUXSettings.columns           = 100;
    SIOUXSettings.rows              = 20;
    SIOUXSettings.fontsize          = 10;
//  SIOUXSettings.fontid             = monaco;
    SIOUXSettings.standalone         = true;


//  DebugStr ( "\pStarting" );

    /*  Can't get very far without this one. */
    if  (!MPLibraryIsLoaded())
    {
        printf("The MP library did not load.\n");
        return;
    }


    /*  Find the overhead up UpTime. Perform a bunch of calls to average out */
    /*   cache effects. */
    printf("\n");

    bgnTime = UpTime();
    for (i=0; i<16; i++)
    {
        nowTime = UpTime();
    }

    uSec  = HowLong(nowTime, bgnTime);
    uSec /=  16.0;
    printf(" UpTime overhead: %.3f usec \n", uSec);

    /*  Time intertask communication. */
    printf("\n Queues\n");

    reflectOP = aQueue;
    MPCreateQueue((MPQueueID*) &waiterID);
    MPCreateQueue((MPQueueID*) &postID);

    bgnTime = UpTime();
    err = MPCreateTask( Reflector,
                  NULL,
                  0,
                  NULL,
                  0,
                  0,
                  kNilOptions,
                  &task );
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    printf(" MPCreateTask overhead: %.3f usec (may vary significantly) \n", uSec);
    if (err != noErr)
    {
        printf(" Task not created!\n");
        return;
    }

    count = 100000;
    bgnTime = UpTime();
    for (i=0; i<count; i++)
    {
        MPNotifyQueue((MPQueueID) waiterID, 0, 0, 0);
        while (true)
        {
            err = MPWaitOnQueue((MPQueueID) postID, &p1, &p2, &p3, kDurationImmediate);
            if (err != kMPTimeoutErr) break;
        }
    }
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    uSec  /= ((float) count / 2.0); // Two trips.
    printf(" Intertask signaling using queues overhead: %.3f usec \n", uSec);

    /*  Time intertask communication.
    */
    MPTerminateTask(task, 123);
    printf("\n Semaphores\n");

    reflectOP = aSemaphore;

    MPCreateSemaphore(1, 0, (MPSemaphoreID*) &waiterID);
    MPCreateSemaphore(1, 0, (MPSemaphoreID*) &postID);

    bgnTime = UpTime();
    err = MPCreateTask( Reflector,
                  NULL,
                  0,
                  NULL,
                  0,
                  0,
                  kNilOptions,
                  &task );
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    printf(" MPCreateTask overhead: %.3f usec (may vary significantly) \n", uSec);
    if (err != noErr)
    {
        printf(" Task not created!\n");
        return;
    }

    count = 100000;
    bgnTime = UpTime();
    for (i=0; i<count; i++)
    {
        MPSignalSemaphore((MPSemaphoreID) waiterID);
        while (true)
        {
            err = MPWaitOnSemaphore((MPSemaphoreID) postID, kDurationImmediate);
            if (err != kMPTimeoutErr) break;
        }
    }
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    uSec  /= ((float) count / 2.0); // Two trips.
    printf(" Intertask signaling using semaphores overhead: %.3f usec \n", uSec);


    /*  Time intertask communication. */
    MPTerminateTask(task, 123);
    printf("\n Event Groups\n");

    reflectOP = anEvent;
    MPCreateEvent((MPEventID*) &waiterID);
    MPCreateEvent((MPEventID*) &postID);

    bgnTime = UpTime();
    err = MPCreateTask( Reflector,
                  NULL,
                  0,
                  NULL,
                  0,
                  0,
                  kNilOptions,
                  &task );
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    printf(" MPCreateTask overhead: %.3f usec (may vary significantly) \n", uSec);
    if (err != noErr)
    {
        printf(" Task not created!\n");
        return;
    }

    count = 100000;
    bgnTime = UpTime();
    for (i=0; i<count; i++)
    {
        MPSetEvent((MPEventID) waiterID, 0x01);
        while (true)
        {
            err = MPWaitForEvent((MPEventID) postID, &events, kDurationImmediate);
            if (err != kMPTimeoutErr) break;
        }
    }
    nowTime = UpTime();
    uSec  = HowLong(nowTime, bgnTime);
    uSec  /= ((float) count / 2.0); // Two trips.
    printf(" Intertask signaling using events overhead: %.3f usec \n", uSec);

    gets(buff);

}
```

[Next](Changes%20From%20Previous%20Versions%20of%20Multiprocessing%20Services.md)[Previous](Preemptive%20Task%E2%80%93Safe%20Mac%20OS%20System%20Software%20Functions.md)

