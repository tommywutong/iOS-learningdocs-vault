---
title: Wake100
apple_id: DTS10000021
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Wake100/Listings/Wake100_c.html
archived_at: '2026-07-18T03:28:07.034618Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Wake100](Wake100.md)


[Next](WakeINIT.c.md)[Previous](Wake100.md)

# Wake100.c

```c
//
//
// © Copyright 1991 Apple Computer, Inc.  All Rights Reserved
//
// By Ricardo Batista
//
// This is an INIT which reads the wake up time in the PowerBook 100 and
// old Portable, if the wake up date has elapsed then we add a day to it
// so that the machine wakes up at the same time every day.
// By request of Neal Macklin.  Maybe we can make something useful from
// this later on.
//
//  This file is a code resource that gets added to the sleep queue.


#include <Types.h>
#include <Power.h>
#include <OSUtils.h>

typedef unsigned long       ulong;



long main()
{
    DateTimeRec d;
    ulong wTime, now;
    Boolean wake = false;
    short err;
    short hour, minute;

    err = GetWUTime((long*) &wTime, (Byte*) &wake);
    if (err)
        return(0L);
    GetDateTime(&now);
    now += 2L;                  // add 2 secs to make sure we just woke up
    if (now > wTime) {
        Secs2Date(wTime, &d);   // get day time they wanted
        hour = d.hour;
        minute = d.minute;
        Secs2Date(now, &d);     // get current date
        if (hour < d.hour)
            d.day++;            // next day
        if ((hour == d.hour) && (minute <= d.minute))
            d.day++;
        d.hour = hour;
        d.minute = minute;
        Date2Secs(&d, &wTime);
        err = SetWUTime((long) &wTime); // interfaces have a bug !
    }

    return(0L);
}
```

[Next](WakeINIT.c.md)[Previous](Wake100.md)

