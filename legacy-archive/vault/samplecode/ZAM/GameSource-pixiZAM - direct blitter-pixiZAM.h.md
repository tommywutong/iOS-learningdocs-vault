---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_pixiZAM___direct_blitter_pixiZAM_h.html
archived_at: '2026-07-18T03:28:34.414472Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-SlamPixels.c.md)[Previous](GameSource-pixiZAM%20-%20direct%20blitter-pixiZAM.c.md)

# GameSource/pixiZAM - direct blitter/pixiZAM.h

```
typedef struct {
    Rect    bounds;
    short   height;
    short   rowLongs;
    long    *image;
    long    *mask;
} pixiZAM;

OSErr LoadPixiFromCIcon(pixiZAM *pz, short resID);
void PixelMover(pixiZAM *srcPixi, PixMapHandle destMap, Rect *destRect);
void MaskedPixelMover(pixiZAM *srcPixi, PixMapHandle destMap, Rect *destRect);
```

[Next](GameSource-SlamPixels.c.md)[Previous](GameSource-pixiZAM%20-%20direct%20blitter-pixiZAM.c.md)

