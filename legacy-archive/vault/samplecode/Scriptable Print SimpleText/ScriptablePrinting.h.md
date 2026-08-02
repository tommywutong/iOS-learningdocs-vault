---
title: Scriptable Print SimpleText
apple_id: DTS10000305
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/Scriptable_Print_SimpleText/Listings/ScriptablePrinting_h.html
archived_at: '2026-07-18T03:23:29.649941Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scriptable Print SimpleText](Scriptable%20Print%20SimpleText.md)


[Next](SimpleText.c.md)[Previous](ScriptablePrinting.c.md)

# ScriptablePrinting.h

```c
/*
**  File:       ScriptablePrinting.h
**
**  Functions defined in Technote 11xx
**
** Copyright 1999 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
*/

#ifndef __SCRIPTABLEPRINTING__
#define __SCRIPTABLEPRINTING__

#ifndef __PRINTING__
#include <Printing.h>
#endif

#ifndef __PRINTING__
#include <Printing.h>
#endif

#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif

#include "PrintAETypes.h"

#if PRAGMA_ONCE
#pragma once
#endif

#ifdef __cplusplus
extern "C" {
#endif

#if PRAGMA_STRUCT_ALIGN
    #pragma options align=mac68k
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(push, 2)
#elif PRAGMA_STRUCT_PACK
    #pragma pack(2)
#endif

OSStatus getPrintRecordFromEvent(const AppleEvent *inAppleEvent,
                                THPrint     *hPrintP);

OSStatus getPrintJobPrintRec(THPrint docPrintRec,
                            THPrint settingsPrintRec,
                            THPrint *jobPrintRecP);

OSStatus getPrintJobShowDialog(const AppleEvent *inAppleEvent,
                                Boolean *showDialog);

#if PRAGMA_STRUCT_ALIGN
    #pragma options align=reset
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(pop)
#elif PRAGMA_STRUCT_PACK
    #pragma pack()
#endif

#ifdef __cplusplus
}
#endif

#endif /* __SCRIPTABLEPRINTING__ */
```

[Next](SimpleText.c.md)[Previous](ScriptablePrinting.c.md)

