---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_Blitter_h.html
archived_at: '2026-07-18T03:25:25.193262Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-CDUtils.c.md)[Previous](Source-Blitter.c.md)

# Source/Blitter.h

```c
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

#ifndef __BLITTER__
#define __BLITTER__

//¥ ------------------------------  Includes

#include <QuickDraw.h>

//¥ ------------------------------  Public Definitions
//¥ ------------------------------  Public Types
//¥ ------------------------------  Public Variables
//¥ ------------------------------  Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern void TransBitBlit(UInt8 *image, CGrafPtr dest, UInt32 width, UInt32 height, UInt32 fullWidth, SInt32 x, SInt32 y);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-CDUtils.c.md)[Previous](Source-Blitter.c.md)

