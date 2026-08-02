---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CMovieMaker_h.html
archived_at: '2026-07-18T03:14:25.278053Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CPict2VRWindow.cp.md)[Previous](CMovieMaker.cp.md)

# CMovieMaker.h

```c
/*
    A set of static functions that know how to create QTVR movies from a source PICT file.

    Created 29 January 1996 by Edward Harp. Based on code by Pete Falco and msnm.

    Copyright © 1996, Apple Computer, Inc.
*/

#ifndef _CMovieMaker_
#define _CMovieMaker_

#ifndef __MOVIES__
#include <Movies.h>
#endif

#include "CApp.h"

class CMovieMaker
{
public:

    static Boolean MakeAMovie(
        Boolean inReplaceFiles,
        const FSSpec &inSrcSpec,
        const FSSpec &inTileSpec,
        const FSSpec &inDestSpec,
        Int16 inWidth,
        Int16 inHeight,
        Fixed inPan,
        Fixed inTilt,
        Fixed inZoom,
        CodecType inCodec,
        CodecQ inSpatialQuality,
        Int16 inDepth,
        ProgressProc inProgressProc);

    static void CreateTileMovie(
        PicHandle inPicH,
        const FSSpec &inTileSpec,
        CodecType inCodec,
        CodecQ inSpatialQuality,
        Int16 inDepth,
        ProgressProc inProgressProc);

    static void CreateSingleNodeMovie(
        const FSSpec &inTileSpec,
        const FSSpec &inMovieSpec,
        Int16 inWidth,
        Int16 inHeight,
        Fixed inPan,
        Fixed inTilt,
        Fixed inZoom);

    static pascal OSErr QTProgress(
        short inMessage,
        Fixed inCompleteness,
        long inRefcon);
};

#endif
```

[Next](CPict2VRWindow.cp.md)[Previous](CMovieMaker.cp.md)

