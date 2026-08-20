---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_Offscreen_h.html
archived_at: '2026-07-18T02:59:14.750105Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-Sample.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-Offscreen.c.md)

# Virtual Sphere Sample Code 1.1/Offscreen.h

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* Offscreen.h
/*
/* Yet another offscreen drawing module that uses GWorld to eliminate drawing flicker.
/*
/* Basic calling sequence is the following:
/*      InitOffscreen (...);
/*      window = GetNewWindow (...);
/*      CheckOffscreenForWindow (&gWorld, window, ...);
/*      while (1) {
/*          CheckOffscreenForWindow (&gWorld, window, ...);
/*          BeginDrawingOffscreen (&gWorld, window);
/*          ... Draw Something ...
/*          EndDrawingOffscreen (&gWorld, window);
/*      }
/*      FreeOffscreen (&gWorld);
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __OFFSCREEN__
#define __OFFSCREEN__

#ifndef __GLOBALS__
#include "Globals.h"
#endif

#ifndef __QDOFFSCREEN__
#include <QDOffscreen.h>
#endif

/* Must be called before any other routines in this module.  The other
 * routines should not be called if GWorld is not available */
pascal OSErr    InitializeOffscreen (Boolean *gWorldAvailable);

pascal void     FreeOffscreen (GWorldPtr offscreenGWorld);

pascal QDErr    CheckOffscreenForWindow (GWorldPtr *offscreenGWorld,
                                         short     pixelDepth,
                                         WindowPtr window);

pascal void     BeginDrawingOffscreen (GWorldPtr offscreenGWorld, WindowPtr window);
pascal void     EndDrawingOffscreen   (GWorldPtr offscreenGWorld, WindowPtr window);



#endif __OFFSCREEN__
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-Sample.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-Offscreen.c.md)

