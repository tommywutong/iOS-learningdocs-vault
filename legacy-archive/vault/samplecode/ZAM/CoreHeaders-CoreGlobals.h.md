---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreHeaders_CoreGlobals_h.html
archived_at: '2026-07-18T03:28:31.812673Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreHeaders-EventLoop.h.md)[Previous](ZAM.md)

# CoreHeaders/CoreGlobals.h

```c
/*
//  SlimGlobals.h
//
//  Global Variables Structures and Defines for the slim skeleton
*/


#pragma once




enum {
    kNumMoreMasters = 4,
    kLow16Bits = 16,
    kLow24Bits = 24
};









extern EventRecord  gEvent;                         // the most recent event
extern Boolean      gDone;                          // true when Quit is selected
extern Boolean      gBackgroundFlag;                // true if we are in the background
extern Boolean      gColorQD;                       // true if we can do color





/* MACROS */


#define RHEIGHT(r)  (r.bottom - r.top)
#define RWIDTH(r)   (r.right - r.left)


#include "WindowDispatch.h"
```

[Next](CoreHeaders-EventLoop.h.md)[Previous](ZAM.md)

