---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSResultWind_h.html
archived_at: '2026-07-18T03:14:42.364981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSScript.c.md)[Previous](Sources-MSResultWind.c.md)

# Sources/MSResultWind.h

```c
// MSResultWind.h
//
// Written by Don Swatman and Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.


#ifndef __MSRESULTWIND__
#define __MSRESULTWIND__

#include "MSGlobals.h"

OSErr       OpenResultWind( void );
void        CloseResultWind( WindowPtr theWind );
WindowPtr   GetResultsWindPtr( void );
DPtr        GetResultsDoc( void );
Boolean     IsThereAResultWind( void );
Boolean     IsThisResultWind( WindowPtr theWind );

OSErr       DisplayDescResult( WindowPtr theWindow,
                                AEDesc* theTextDesc, DPtr theDoc, OSErr theErr );
OSErr       DisplayOSAIDResult( WindowPtr theWindow,
                                OSAID theOSAID, DPtr theDoc, OSErr theErr );
OSAError    DisplayOSAScriptError( DPtr theDoc );

#endif
```

[Next](Sources-MSScript.c.md)[Previous](Sources-MSResultWind.c.md)

