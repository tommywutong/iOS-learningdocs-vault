---
title: vrcursors
apple_id: DTS10001021
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrcursors/Listings/TestFunctions_h.html
archived_at: '2026-07-26T19:52:56.584917Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrcursors](vrcursors.md)


[Next](Document%20Revision%20History.md)[Previous](TestFunctions.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# TestFunctions.h

```c
//////////
//
//  File:       TestFunctions.h
//
//  Contains:   Insert test functions prototypes and constants into this file.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1994-1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/27/96    rtm     first file
//
//////////

// header files
#include "QTUtilities.h"
#include "QTVRUtilities.h"
#include <QuickTimeVR.h>
#include <Resources.h>

// constants for "undefined" hot spots, ***both panoramas and objects***
// (these are listed in VRPWQTVR2.0, p. A-2)
#define kCursID_MouseOverMiscHS     -19690      // miscellaneous hot spots ('misc')
#define kCursID_MouseDownOnMiscHS   -19689
#define kCursID_MouseUpOnMiscHS     -19688
#define kCursID_MouseOverUndefHS    -19687      // undefined hot spots ('undf', other undefined, or missing type)
#define kCursID_MouseDownOnUndefHS  -19686
#define kCursID_MouseUpOnUndefHS    -19685

// function prototypes
PASCAL_RTN OSErr                    MyMouseOverHotSpotProc (QTVRInstance theInstance, UInt32 theHotSpotID, UInt32 theFlags, long theRefCon);
```

[Next](Document%20Revision%20History.md)[Previous](TestFunctions.c.md)

