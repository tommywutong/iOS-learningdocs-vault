---
title: MakeIcon
apple_id: DTS10000089
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeIcon/Listings/IconUtil_h.html
archived_at: '2026-07-18T03:14:21.301027Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeIcon](MakeIcon.md)


[Next](InitMac.c.md)[Previous](IconUtil.c.md)

# IconUtil.h

```
/*
    File:       IconUtil.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

GWorldPtr CreateOffScreen (WindowPtr basePort, short depth, Boolean UseTempMem);
GWorldPtr LoadPictToGWorld(int resID, WindowPtr wp, int numEntries,
                        int pdepth, int gdepth, Boolean linkCtabToPal);
OSErr SetUpPixMap(
    short        depth,       /* Desired number of bits/pixel in off-screen */
    Rect         *bounds,     /* Bounding rectangle of off-screen */
    CTabHandle   colors,      /* Color table to assign to off-screen */
    PixMapHandle aPixMap      /* Handle to the PixMap being initialized */
    );

Handle MakeICN_pound(GWorldPtr  gwp, Rect *srcRect, short iconSize);

Handle MakeIconMask(GWorldPtr srcGWorld, Rect *srcRect, short iconSize);

Handle MakeIcon(GWorldPtr srcGWorld, Rect *srcRect, short dstDepth, short iconSize);

void TearDownPixMap(PixMapHandle pix);
PicHandle PIXtoPICT(CGrafPtr wp);
```

[Next](InitMac.c.md)[Previous](IconUtil.c.md)

