---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/Source_BlendUtils_h.html
archived_at: '2026-07-18T03:01:56.926099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](Source-MainStuff.c.md)[Previous](Source-BlendUtils.c.md)

# Source/BlendUtils.h

```
/*--------------------------------------------------------------------------------------
//
//  File:       BlendProcs.h
//
//  Contents:   Header declarations procedures that generate blended fills.
//
//
//  By Georgiann ("George") Delaney
//  ©Ê1989 - 1990, Apple Computer, Inc.
//
//--------------------------------------------------------------------------------------*/



void  HLSRectBlend          (Rect *boundRect, short saturation);
void  HLSVLinearBlend       (Rect *boundRect, short saturation);
void  HLSHLinearBlend       (Rect *boundRect, short saturation);

void  GrayRectBlend         (Rect *boundRect);
void  GrayVLinearBlend      (Rect *boundRect);
void  GrayHLinearBlend      (Rect *boundRect);

void  GrayPatRectBlend      (Rect *boundRect);
void  GrayPatVLinearBlend   (Rect *boundRect);
void  GrayPatHLinearBlend   (Rect *boundRect);
```

[Next](Source-MainStuff.c.md)[Previous](Source-BlendUtils.c.md)

