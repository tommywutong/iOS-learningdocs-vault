---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSASSubroutines_h.html
archived_at: '2026-07-18T03:14:40.184352Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSDrag.c.md)[Previous](Sources-MSASSubroutines.c.md)

# Sources/MSASSubroutines.h

```c
// MSASSubroutines.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// Human Interface changes and GX Printing by Don Swatman
// ©Apple Computer Inc 1996, all rights reserved.

#pragma once

#ifndef __MSGLOBALS__
#include "MSGlobals.h"
#endif

#include <OSA.h>


OSErr   GetVolumeAndDirectory(void);
OSErr   FSSpecLaunchApplication(const FSSpec *fileSpec,ProcessSerialNumber *PSN);
void    SetUpScripts( void );

OSErr   LoadScriptFromResFile( FSSpec *theSpec, short theResID, OSAID *theScriptID );
OSErr   LoadScriptFromResFileRef( short theRefNum, short theResID, OSAID *theScriptID );
OSErr   StoreScriptToResFile( FSSpec *theFileRef, short theResID,
                                OSAID theScriptID, StringPtr theResName );
OSErr   StoreScriptToResFileRef( short theFileRef, short theResID,
                                OSAID theScriptID, StringPtr theResName );

OSErr   CleanUpAEScripts(void);
OSErr   ExecuteScript1(DPtr theDoc);
OSErr   ExecuteScript2(DPtr theDoc);
OSErr   ExecuteScript3(DPtr theDoc);
OSErr   ExecuteScript4(DPtr theDoc);

OSErr   GetTextDescFromReply(AEDesc *aReply, AEDesc *textDesc);
OSErr   GetSelection(AEDesc *textDesc);
OSErr   SetSelection(AEDesc *textDesc);

void    EnableAEScriptItems(Boolean fEnable);

pascal Boolean  IdleProc(EventRecord *myEvent, long *sleep, RgnHandle *mouseRgn);
```

[Next](Sources-MSDrag.c.md)[Previous](Sources-MSASSubroutines.c.md)

