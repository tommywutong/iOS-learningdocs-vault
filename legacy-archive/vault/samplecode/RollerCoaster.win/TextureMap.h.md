---
title: RollerCoaster.win
apple_id: DTS10000882
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RollerCoaster.win/Listings/TextureMap_h.html
archived_at: '2026-07-18T03:22:13.573646Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RollerCoaster.win](RollerCoaster.win.md)


[Next](Track.c.md)[Previous](TextureMap.c.md)

# TextureMap.h

```c
/*
    File:       TextureMap.h

    Contains:   Interface file for TextureMap.c

    Written by: Scott Kuechle, based on original Gerbils code by Brian Greenstone

    Copyright:  © 1998 by Apple Computer, Inc. All rights reserved

    Change History (most recent first)

        <1>     9/1/98      srk     first file


*/

#pragma once

/************************************************************
*                                                           *
*    INCLUDE FILES                                          *
*                                                           *
*************************************************************/

#include <Resources.h>

#include "QD3DShader.h"
#include "QD3DStorage.h"
#include "QD3DMath.h"
#include "QDOffscreen.h"
#include "ImageCompression.h"

#if TARGET_OS_WIN32
    #include "QTML.h"
#endif

#include "Utils.h"

/************************************************************
*                                                           *
*    FUNCTION PROTOTYPES                                    *
*                                                           *
*************************************************************/

TQ3ShaderObject TextureMap_Get(PicHandle picH, Rect *picRect);
```

[Next](Track.c.md)[Previous](TextureMap.c.md)

