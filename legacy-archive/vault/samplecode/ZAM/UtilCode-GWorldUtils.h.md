---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/UtilCode_GWorldUtils_h.html
archived_at: '2026-07-18T03:28:34.824872Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](UtilCode-IsPressed.c.md)[Previous](UtilCode-GWorldUtils.c.md)

# UtilCode/GWorldUtils.h

```c
/*
//  GWorldUtils.h
//
//  Created:    8/12/91 at 8:01:49 PM
//  By:     Tony Myles
//
//  Copyright: © 1991-93 Tony Myles, All rights reserved worldwide
//
//  Description:    some utility routines to help create graphics worlds
*/


#ifndef __GWORLDUTILS__
#define __GWORLDUTILS__

#ifndef __QDOFFSCREEN__
#include <QDOffscreen.h>
#endif

// QuickDraw.h
OSErr CreateOptimumGWorld(GWorldPtr *optGWorld, Rect *devRect);
OSErr CreateGWorldFromPictResource(GWorldPtr *pictGWorldP, short pictResID);
OSErr CreateGWorldFromPict(GWorldPtr *pictGWorld, PicHandle pictH);
OSErr CreateGWorldFromCIconResource(GWorldPtr *iconGWorldP, short iconResID);
OSErr CreateGWorldFromCIcon(GWorldPtr *iconGWorldP, CIconHandle cIconH);
OSErr CreateGWorldFromCIconMask(GWorldPtr *maskGWorldP, CIconHandle cIconH);
OSErr CreateRegionFromCIconMask(RgnHandle *maskRgn, CIconHandle cIconH);


#endif
```

[Next](UtilCode-IsPressed.c.md)[Previous](UtilCode-GWorldUtils.c.md)

