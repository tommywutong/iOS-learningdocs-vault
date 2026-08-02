---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_Offscreen_c.html
archived_at: '2026-07-18T03:14:43.765164Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-Offscreen.h.md)[Previous](Sources-MSWindow.h.md)

# Sources/Offscreen.c

```c
// Offscreen.c
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.


#include "Offscreen.h"


#ifndef __QUICKDRAW__
    #include <Quickdraw.h>
#endif

#ifndef __QDOFFSCREEN__
    #include <QDOffscreen.h>
#endif

#ifndef __MEMORY__
    #include <Memory.h>
#endif


tWindowOffscreen* DrawOffscreen ( WindowRef theWindow )
{
    tWindowOffscreen*   theOffscreen;
    GWorldPtr           theWorld;
    Rect                globalRect;


    theOffscreen = (tWindowOffscreen*) NewPtr ( sizeof ( tWindowOffscreen ) );
    if ( theOffscreen == 0L )
        return 0L;

    SetPort ( theWindow );
    GetGWorld ( &theOffscreen->windowPort, &theOffscreen->windowDevice );

    globalRect = theWindow->portRect;
    LocalToGlobal ( (Point*) &globalRect.top );
    LocalToGlobal ( (Point*) &globalRect.bottom );

    if ( NewGWorld ( &theWorld, 0, &globalRect, 0L, 0L, 0) == noErr )
    {
        SetGWorld ( theWorld, 0L );
        if ( !LockPixels ( theWorld->portPixMap ) )
        {
            DisposeOffscreen ( theOffscreen );
            return 0L;
        }

        CopyBits ( &theWindow->portBits, &((GrafPtr) theWorld)->portBits,
                    &theWindow->portRect, &theWorld->portRect, srcCopy, 0L );

        theOffscreen->offscreenWorld = theWorld;
        return theOffscreen;
    }

    DisposePtr ( (Ptr) theOffscreen );
    return 0L;
}



tWindowOffscreen* DrawOnscreen ( tWindowOffscreen* theOffscreen )
{
    if ( theOffscreen )
    {
        SetGWorld ( theOffscreen->windowPort, theOffscreen->windowDevice );
        CopyBits ( &((GrafPtr) theOffscreen->offscreenWorld)->portBits,
                        (BitMap*) &(theOffscreen->windowPort)->portPixMap,
                        &theOffscreen->offscreenWorld->portRect,
                        &theOffscreen->windowPort->portRect,
                        srcCopy, 0L );
        UnlockPixels ( theOffscreen->offscreenWorld->portPixMap );
        DisposeOffscreen ( theOffscreen );
    }

    return nil;
}



tWindowOffscreen* DisposeOffscreen ( tWindowOffscreen* theOffscreen )
{

    DisposeGWorld ( theOffscreen->offscreenWorld );
    DisposePtr ( (Ptr) theOffscreen );

    return nil;
}
```

[Next](Sources-Offscreen.h.md)[Previous](Sources-MSWindow.h.md)

