---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSMain_h.html
archived_at: '2026-07-18T03:14:42.179482Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSResultWind.c.md)[Previous](Sources-MSMain.c.md)

# Sources/MSMain.h

```c
// MSMain.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// Human Interface changes and GX Printing by Don Swatman
// ©Apple Computer Inc 1996, all rights reserved.

#pragma once

#include <Types.h>
#include <StandardFile.h>

void            MaintainMenus ( Boolean *pRedrawMenuBar );
void            MaintainEditItems ( TEHandle           theTE,     
                                    short              numTypes,
                                    ConstSFTypeListPtr typeList );
void            CheckMenus( void );
void            DoCommand( long mResult );
void            DoMenuItem( short theMenuID, short theItem );

OSErr           GXPrintingEventOverride( EventRecord *anEvent, Boolean filterEvent );
```

[Next](Sources-MSResultWind.c.md)[Previous](Sources-MSMain.c.md)

