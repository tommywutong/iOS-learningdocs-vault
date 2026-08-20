---
title: rollercoasterold
apple_id: DTS10000135
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/rollercoasterold/Listings/Interfaces_TextureMap_h.html
archived_at: '2026-07-26T19:52:27.705188Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [rollercoasterold](rollercoasterold.md)


[Next](Interfaces-Track.h.md)[Previous](Interfaces-QD3DSupport.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Interfaces/TextureMap.h

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

#if defined(_MSC_VER)
#include "WinPrefix.h"
#else
#include <ConditionalMacros.h>
#endif

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

[Next](Interfaces-Track.h.md)[Previous](Interfaces-QD3DSupport.h.md)

