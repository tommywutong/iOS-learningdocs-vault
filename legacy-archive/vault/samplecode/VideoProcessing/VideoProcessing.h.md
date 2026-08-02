---
title: VideoProcessing
apple_id: DTS10000883
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-06'
source_url: https://developer.apple.com/library/archive/samplecode/VideoProcessing/Listings/VideoProcessing_h.html
archived_at: '2026-07-18T03:27:53.034075Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoProcessing](VideoProcessing.md)


[Next](VideoProcessingPrefix.h.md)[Previous](Utilities.h.md)

# VideoProcessing.h

```c
/*
 *  VideoProcessing.h
 *  VideoProcessing
 *
 *  Created by Scott Kuechle on Wed May 14 2003.
 *  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
 *
 */

#if __MACH__
    #include <QuickTime/QuickTime.h>
#else

#endif

typedef struct
    {
    // input: supplied by client
    Ptr     baseAddr;       // base address of start of this layer
    Rect    layerBounds;    // bounds of the layer (ie, where to draw)
    long    rowBytes;       // rowBytes, stripped of high bits
    } LayerRecord, *LayerPtr;

#define kNumPixelFormatsSupported   0x20

typedef struct {
    long        width;
    long        height;
    Rect        dstRect;
    OSType      pixelFormat;
    Ptr         baseAddr;
    long        rowBytes;

    LayerRecord source, overlay, dest;
    UInt32      *redCount, *greenCount, *blueCount;
    UInt32      redMin, redMax;
    UInt32      greenMin, greenMax;
    UInt32      blueMin, blueMax;
} AppBlitDecompressRecord;

typedef struct
    {
    ComponentInstance           self;
    ComponentInstance           delegateComponent;
    ComponentInstance           target;

    OSType                      **wantedDestinationPixelTypeH;
    } AppBlitGlobalsRecord, *AppBlitGlobalsPtr;
```

[Next](VideoProcessingPrefix.h.md)[Previous](Utilities.h.md)

