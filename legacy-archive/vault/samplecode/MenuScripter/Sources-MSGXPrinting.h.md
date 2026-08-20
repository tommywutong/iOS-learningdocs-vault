---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSGXPrinting_h.html
archived_at: '2026-07-18T03:14:41.728541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSMain.c.md)[Previous](Sources-MSGXPrinting.c.md)

# Sources/MSGXPrinting.h

```c
// MSGXPrinting.c
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// GX printing by Don Swatman
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSGXPRINTING__
#define __MSGXPRINTING__

#include "MSGlobals.h"

// Start up and finish printing

void InitGXIfPresent(void);
void CleanUpGXIfPresent(void);

// Make any patches to the menu
short ConvertMenuActualToGXMenu ( short theItem );

// Get a QD rect for a print page
void GetRectOfPage( DPtr  theDoc,
                                        Rect  *pageRect );

// Put up the GX Page Setup dialog
Boolean DoGXPageSetup ( DPtr theDoc );

// Print a page
OSErr GXPrintDocument ( DPtr    theDoc,
                                                Boolean askUser );

void DuplicateStyleTERec( TEHandle  hSourceTE,
                                                    TEHandle *hDestTE,
                                                    Rect     *destRect,
                                                    GrafPtr   destPort );

void    AdjustMenusForGXPrintDialogs(Boolean dialogGoingUp);
void    SetupGXEditMenuRec(gxEditMenuRecord *editMenuRec);
OSErr PrintAShape(gxShape currentShape, long refCon);
OSErr GXPrintLoop(DPtr theDoc);

#endif
```

[Next](Sources-MSMain.c.md)[Previous](Sources-MSGXPrinting.c.md)

