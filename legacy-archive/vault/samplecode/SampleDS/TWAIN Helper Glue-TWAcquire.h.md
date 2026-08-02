---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWAcquire_h.html
archived_at: '2026-07-18T03:22:59.914564Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](TWAIN%20Helper%20Glue-TWDefs.h.md)[Previous](TWAIN%20Helper%20Glue-TWAcquire.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWAcquire.h

```c
// ===========================================================================
//  TWAcquire.c         TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//  Sample code for responding to the Acquire... menu item.
//

#ifndef _ACQUIREIMAGE_
#define _ACQUIREIMAGE_
#pragma once

#include "TWAIN.h"

extern TW_UINT16    ProcessTWMessage(TW_UINT16 TWMessage);

extern TW_UINT16    TWAcquire(PicHandle *pPictHandle);
extern TW_UINT16    TWTransferImage(PicHandle *pPictHandle);

extern TW_UINT16    TWAcquireFile ( FSSpecPtr specPtr, TW_UINT16 fileFormat );
extern TW_UINT16    TWTransferFile ( FSSpecPtr specPtr, TW_UINT16 fileFormat );

#endif
```

[Next](TWAIN%20Helper%20Glue-TWDefs.h.md)[Previous](TWAIN%20Helper%20Glue-TWAcquire.c.md)

