---
title: Show Movie
apple_id: DTS10000792
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Show_Movie/Listings/MovieStuff_h.html
archived_at: '2026-07-18T03:23:45.795395Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Show Movie](Show%20Movie.md)


[Next](Show%20Movie.c.md)[Previous](MovieStuff.c.md)

# MovieStuff.h

```c
/*
    File:       MovieStuff.h

    Contains:       Movie handling routine's headers.

    Written by: Jason Hodges-Harris & Don Swatman   

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/17/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#ifndef __MOVIESTUFF__
#define __MOVIESTUFF__

#include <Windows.h>
#include <Types.h>

//----------------------------------------------
// Prototypes
//----------------------------------------------

OSErr OpenMovieWindow ( WindowPtr pWindow,
                                                Boolean   doesAutoClose,
                                                Boolean   hasControler  );

OSErr CloseMovieWindow( WindowPtr pWindow,
                                                WindowPtr *pSlaveWindow  );

#define kStartFromBegining true
#define kStartAtCurrentPos false

OSErr StartMovieWindow( WindowPtr pWindow,
                                                Boolean   fromBegining  );

void UpdateMovieWindow (  WindowPtr pWindow   );

Boolean ServiceMovieTasks ( WindowPtr pWindow,
                                                        const EventRecord *theEvent );

#define kInSync 0
#define kOneThird -1

OSErr SetupSlaveMovie ( WindowPtr pMasterWindow,
                                                WindowPtr pSlaveWindow,
                                                short     slaveAheadBy,
                                                short     slaveDelayStart );

OSErr SetupMovieRate( WindowPtr pWindow,
                                            short delayBeforeChange  );

OSErr SetupLoop ( WindowPtr pWindow,
                                    short loopWhen,
                                    short loopTo  );

Boolean IsMoviePlaying (void);

void InitMovieGlobals(void);
void KillMovieGlobals(void);


#endif
```

[Next](Show%20Movie.c.md)[Previous](MovieStuff.c.md)

