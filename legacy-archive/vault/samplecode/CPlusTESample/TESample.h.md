---
title: CPlusTESample
apple_id: DTS10000730
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CPlusTESample/Listings/TESample_h.html
archived_at: '2026-07-18T03:02:44.262352Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CPlusTESample](CPlusTESample.md)


[Next](TESample.r.md)[Previous](TESample.cp.md)

# TESample.h

```c
/*------------------------------------------------------------------------------------------

    Program:    CPlusTESample 2.0
    File:       TESample.h
    Uses:       Application.h
                TECommon.h

    by Andrew Shebanow
    of Apple Macintosh Developer Technical Support

    Copyright © 1989-1990 Apple Computer, Inc.
    All rights reserved.

------------------------------------------------------------------------------------------*/

#ifndef __TESAMPLE__
#define __TESAMPLE__

// we need resource definitions
#ifndef __TECOMMON__
#include "TECommon.h"
#endif

// Since we are based on the Application class, we need its class definitions
#ifndef __APPLICATION__
#include "Application.h"
#endif

// TESample is our application class. It is a subclass of TApplication,
// so it only needs to specify its behaviour in areas where it is different
// from the default.
class TESample : public TApplication {
public:
            TESample();             // Our constructor

private:
    // routines from TApplication we are overriding
    long    HeapNeeded();
    unsigned long SleepVal();
    void    DoIdle();
    void    AdjustCursor();
    void    AdjustMenus();
    void    DoMenuCommand(short menuID, short menuItem);
    void    OpenADoc(short vRefNum, long dirID, StringPtr fName, OSType fType);

    // routines for our own devious purposes
    void    DoNew();
    void    DoOpen();
};

#endif
```

[Next](TESample.r.md)[Previous](TESample.cp.md)

