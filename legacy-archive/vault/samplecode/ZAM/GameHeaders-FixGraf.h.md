---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_FixGraf_h.html
archived_at: '2026-07-18T03:28:32.461614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-GameAEvents.h.md)[Previous](GameHeaders-Document.h.md)

# GameHeaders/FixGraf.h

```
#pragma once
typedef struct {
    Fixed   h;
    Fixed   v;
} fixPt;

typedef struct {
    Fixed   top;
    Fixed   left;
    Fixed   bottom;
    Fixed   right;
} fixRect;


    // fixed point math stuff (thanks Myles & GX)
#define ff(x)   (((long)(x)<<16))
#define FixToInt(x) ((int)((x)>>16))
#define FixToDbl(x) ldexp((double)(x),-16)
#define DblToFix(x) ((long)ldexp((x),16))
#define RndFixToInt(x) ((int)((x)+FIX_HALF>>16))
#define FixRound(x) FixToi(x)
#define Frac2Fix(x) ((x)>>14)
#define Fix2Frac(x) ((x)<<14)
#define FracToDbl(x) ldexp((double)(x),-30)
#define DblToFrac(x) ((long)ldexp((x),30))
```

[Next](GameHeaders-GameAEvents.h.md)[Previous](GameHeaders-Document.h.md)

