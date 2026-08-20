---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWGlue_h.html
archived_at: '2026-07-18T03:23:00.252121Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](TWAIN%20Helper%20Glue-TWSystem.c.md)[Previous](TWAIN%20Helper%20Glue-TWGlue.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWGlue.h

```c
// ===========================================================================
//  TWGlue.h            TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//  
//

#ifndef __GLUECODE__
#define __GLUECODE__
#pragma once

#include    "TWAIN.h"

/* primary glue code calls */
extern pTW_IDENTITY TWGetDSIdentity(void);
extern pTW_IDENTITY TWGetAppIdentity(void);
extern TW_INT16 TWInitialize(pTW_IDENTITY pIdentity);
extern TW_INT16 TWTerminate(void);

extern TW_INT16 TWSelectDS(void);
extern TW_INT16 TWEventDS(EventRecord *pEvent,pTW_INT16 pMessage);

extern TW_INT16 TWRegisterCallback(DSMENTRYPROC ptr);

extern TW_INT16 TWOpenDSM(void);
extern TW_INT16 TWCloseDSM(void);

extern TW_INT16 TWOpenDSIdentity(pTW_IDENTITY pDSIdentity);
extern TW_INT16 TWOpenDS(void);
extern TW_INT16 TWCloseDS(void);

extern TW_INT16 TWEnableDS(pTW_USERINTERFACE pUserInterface);
extern TW_INT16 TWDisableDS(pTW_USERINTERFACE pUserInterface);

extern TW_INT16 TWMessageDS(TW_UINT32 DG,TW_UINT16 Dat,TW_UINT16 Msg,
                    TW_MEMREF pData);
extern TW_INT16 TWMessageDSM(TW_UINT32 DG,TW_UINT16 Dat,TW_UINT16 Msg,
                    TW_MEMREF pData);

/* capabilities calls */

extern TW_INT16 TWGetPixelTypes(pTW_INT16 pDoesBW,pTW_INT16 pDoesGray,
                    pTW_INT16 pDoesRGB, pTW_INT16 pDoesPalette);

extern TW_INT16 TWSetPixelType(TW_INT16 PixelType);

extern TW_INT16 TWGetDSCapability ( TW_UINT16 capabilityID, TW_INT16 value, pTW_INT16 isCapable );
extern TW_INT16 TWSetDSCapability ( TW_UINT16 capabilityID, TW_INT16 value );

/* miscellaneous calls */

extern TW_INT16 TWIsDSEnabled(void);

extern TW_INT16 TWDSMVersion(pTW_INT16 pMajor,pTW_INT16 pMinor);


#endif
```

[Next](TWAIN%20Helper%20Glue-TWSystem.c.md)[Previous](TWAIN%20Helper%20Glue-TWGlue.c.md)

