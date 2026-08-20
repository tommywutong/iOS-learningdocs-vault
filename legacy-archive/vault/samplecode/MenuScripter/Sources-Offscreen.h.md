---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_Offscreen_h.html
archived_at: '2026-07-18T03:14:43.820548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-PLStrs.c.md)[Previous](Sources-Offscreen.c.md)

# Sources/Offscreen.h

```c
// Offscreen.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#pragma once

#ifndef __QUICKDRAW__
    #include <Quickdraw.h>
#endif

#ifndef __QDOFFSCREEN__
    #include <QDOffscreen.h>
#endif


typedef struct WindowOffscreen
{
    CGrafPtr        windowPort;
    GDHandle        windowDevice;
    GWorldPtr       offscreenWorld;
} tWindowOffscreen;


tWindowOffscreen* DrawOffscreen ( WindowPtr theWindow );
tWindowOffscreen* DrawOnscreen ( tWindowOffscreen* theOffscreen );
tWindowOffscreen* DisposeOffscreen ( tWindowOffscreen* theOffscreen );
```

[Next](Sources-PLStrs.c.md)[Previous](Sources-Offscreen.c.md)

