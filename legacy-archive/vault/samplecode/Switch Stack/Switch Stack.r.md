---
title: Switch Stack
apple_id: DTS10000223
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Switch_Stack/Listings/Switch_Stack_r.html
archived_at: '2026-07-18T03:25:52.356257Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Switch Stack](Switch%20Stack.md)


[Next](Document%20Revision%20History.md)[Previous](Switch%20Stack.c.md)

# Switch Stack.r

```c
/*
**  File:       Switch Stack.r
**
**  Contains:   A simple 68K example of a VBL written in C that runs on a
**              private stack.
**
**  Written by: Jim Luther (Based on the VBL code from the Technical Note
**              "MultiFinder Miscellanea".) 
**
**  Copyright:  © 1993-1995 by Apple Computer, Inc., all rights reserved.
**
**  Change History (most recent first):
**
**       <5>     01/27/95   JML     Added .r file for resources
**       <4>     01/27/95   JML     Got rid of the THINK C-isms. Now builds with THINK C, MPW C, and Metrowerks C
**       <3>     11/02/93   JML     Added reentrancy comment to VBL
**       <2>     10/13/93   JML     Minor cleanup
**       <1>     10/08/93   JML     First pass
**
*/

#define SystemSevenOrLater 1

#include "Types.r"

resource 'DLOG' (140) {
    {40, 40, 115, 281},
    dBoxProc,
    visible,
    goAway,
    0x0,
    128,
    "",
    alertPositionMainScreen
};

resource 'DITL' (128) {
    {   /* array DITLarray: 3 elements */
        /* [1] */
        {40, 90, 55, 222},
        StaticText {
            disabled,
            "Static Text"
        },
        /* [2] */
        {40, 20, 56, 91},
        StaticText {
            disabled,
            "gCounter:"
        },
        /* [3] */
        {10, 20, 30, 213},
        StaticText {
            disabled,
            "Click mouse button to quitÉ"
        }
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](Switch%20Stack.c.md)

