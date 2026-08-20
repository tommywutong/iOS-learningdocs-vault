---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWUtilities_h.html
archived_at: '2026-07-18T03:23:00.520600Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](Document%20Revision%20History.md)[Previous](TWAIN%20Helper%20Glue-TWUtilities.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWUtilities.h

```c
// ===========================================================================
//  TWUtilities.c       TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//
//  Glue-code utilities.

#ifndef _TWUTILITIES_
#define _TWUTILITIES_
#pragma once

#include <TWAIN/TWAIN.h>

extern TW_INT16     SetupOneValue(pTW_CAPABILITY pCapability,
                        TW_INT16 ItemType,TW_INT32 Item);

extern TW_INT16     SetupRange(pTW_CAPABILITY pCapability,TW_INT16 ItemType,
                        TW_INT32 MinValue,TW_INT32 MaxValue,TW_INT32 StepSize,
                        TW_INT32 DefaultValue,TW_INT32 CurrentValue);

extern TW_INT16     SetupEnumeration(pTW_CAPABILITY pCapability,
                        TW_INT16 ItemType,TW_INT16 NumItems,
                        TW_INT16 CurrentIndex,TW_INT16 DefaultIndex,
                        pTW_UINT8 ItemList);

extern TW_INT16     SetupArray(pTW_CAPABILITY   pCapability,
                        TW_INT16        ItemType,
                        TW_INT16        NumItems,
                        pTW_UINT8       ItemList);

extern TW_INT16     GetOneValue(pTW_CAPABILITY pCapability,
                        pTW_INT16 pItemType,pTW_INT32 pItem);

extern TW_INT16     GetRange(pTW_CAPABILITY pCapability,pTW_INT16 pItemType,
                        pTW_INT32 pMinValue,pTW_INT32 pMaxValue,pTW_INT32 pStepSize,
                        pTW_INT32 pDefaultValue,pTW_INT32 pCurrentValue);

extern TW_INT16     GetEnumeration(pTW_CAPABILITY pCapability,
                        pTW_INT16 pItemType,pTW_INT16 pNumItems,
                        pTW_INT16 pCurrentIndex,pTW_INT16 pDefaultIndex,
                        pTW_UINT8 pItemList,TW_INT16 MaxBytes);

extern TW_INT16     GetArray(   pTW_CAPABILITY  pCapability,
                        pTW_INT16       pItemType,
                        pTW_INT16       pNumItems,
                        pTW_UINT8       pItemList,
                        TW_INT16        MaxBytes);

extern TW_INT16     DumpOneValue(pTW_CAPABILITY pCapability,
                        pTW_INT16 pItemType,pTW_INT32 pItem);

extern TW_INT16     DumpRange(pTW_CAPABILITY pCapability,pTW_INT16 pItemType,
                        pTW_INT32 pMinValue,pTW_INT32 pMaxValue,pTW_INT32 pStepSize,
                        pTW_INT32 pDefaultValue,pTW_INT32 pCurrentValue);

extern TW_INT16     DumpEnumeration(pTW_CAPABILITY pCapability,
                        pTW_INT16 pItemType,pTW_INT16 pNumItems,
                        pTW_INT16 pCurrentIndex,pTW_INT16 pDefaultIndex,
                        pTW_UINT8 pItemList,TW_INT16 MaxBytes);

extern TW_INT16     DumpArray(  pTW_CAPABILITY  pCapability,
                        pTW_INT16       pItemType,
                        pTW_INT16       pNumItems,
                        pTW_UINT8       pItemList,
                        TW_INT16        MaxBytes);

extern TW_INT16     GetItemSize(TW_INT16 ItemType);

#endif
```

[Next](Document%20Revision%20History.md)[Previous](TWAIN%20Helper%20Glue-TWUtilities.c.md)

