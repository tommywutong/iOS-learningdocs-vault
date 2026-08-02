---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAppleEvents_h.html
archived_at: '2026-07-18T03:14:40.834241Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSASSubroutines.c.md)[Previous](Sources-MSAppleEvents.c.md)

# Sources/MSAppleEvents.h

```c
// MSAppleEvents.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAPPLEEVENTS__
#define __MSAPPLEEVENTS__

#include <Types.h>
#include <Quickdraw.h>
#include <Packages.h>
#include <GestaltEqu.h>
#include <Editions.h>

#include "MSToken.h"

#define     noRefCon    -1

void            InitAppleEvents(void);
void            DoAppleEvent(EventRecord theEvent);

pascal OSErr DoOpenApp(const AppleEvent *message,const AppleEvent *reply,long refcon);
pascal OSErr DoOpenDocument( const AppleEvent *theEvent, const AppleEvent *theReply, long refcon );
pascal OSErr MyQuit(const AppleEvent *message,const AppleEvent *reply,long refcon); 
pascal OSErr DoPrintDocuments(const AppleEvent *message, AppleEvent *reply, long refcon);


#endif
```

[Next](Sources-MSASSubroutines.c.md)[Previous](Sources-MSAppleEvents.c.md)

