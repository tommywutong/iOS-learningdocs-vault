---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWSystem_h.html
archived_at: '2026-07-18T03:23:00.366822Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](TWAIN%20Helper%20Glue-TWUtilities.c.md)[Previous](TWAIN%20Helper%20Glue-TWSystem.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWSystem.h

```c
// ===========================================================================
//  TWSystem.h          TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//
//  

#ifndef __TWSystem__
#define __TWSystem__
#pragma once

#include <TWAIN/TWAIN.h>

extern TW_INT16     pstrcopy(pTW_UINT8 destin,pTW_UINT8 source);
extern TW_INT16     pstrcmp(pTW_UINT8 string1,pTW_UINT8 string2);
extern TW_INT16     pstrcat(pTW_UINT8 destin, pTW_UINT8 source);
extern TW_INT16     HasColorQuickDraw();

extern SInt16       StandardCautionAlert ( ConstStringPtr error, ConstStringPtr explanation );


#endif
```

[Next](TWAIN%20Helper%20Glue-TWUtilities.c.md)[Previous](TWAIN%20Helper%20Glue-TWSystem.c.md)

