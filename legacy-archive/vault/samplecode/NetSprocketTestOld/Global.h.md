---
title: NetSprocketTestOld
apple_id: DTS10000058
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/NetSprocketTestOld/Listings/Global_h.html
archived_at: '2026-07-18T03:16:54.243325Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NetSprocketTestOld](NetSprocketTestOld.md)


[Next](init.c.md)[Previous](events.c.md)

# Global.h

```c
/***********************************************************************
#
#       Global.h
#
#       This file contains the global definitions
#
#       Author: Michael Marinkovich
#               Apple Developer Technical Support
#
#
#       Modification History: 
#
#           6/4/95  MWM     Initial coding                   
#
#
#       Copyright © 1992-94 Apple Computer, Inc., All Rights Reserved
#
#
***********************************************************************/

#include <Drag.h>

Boolean         gHasDMTwo;                      // is DM 2.0 available?
Boolean         gInBackground = false;          // are we in the background?
Boolean         gDone = false;                  // app is done flag     
Boolean         gHasDrag;                       // we have Drag Manager?
Boolean         gHasAbout;                      // do we have an about box showing?
short           gWindCount;                     // window counter for new windows
```

[Next](init.c.md)[Previous](events.c.md)

