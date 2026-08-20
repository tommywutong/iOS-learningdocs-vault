---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/headers_PictRead_h.html
archived_at: '2026-07-18T03:18:58.510403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](PickOnePrefix.h.md)[Previous](headers-PickOnewindow.h.md)

# headers/PictRead.h

```c
#pragma once
/******************************************************************************
 **                                                                          **
 **     Module:     PictRead.h                                               **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Purpose:    protos for PICT to TEX routines                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1992-1995 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef PictRead_h
#define PictRead_h

#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */


PicHandle OpenPICTFile( 
    short   vRefNum, 
    Str255  fName);

PicHandle GetPICTFile( 
    void);

short LoadMapPICT(
    PicHandle           pict,
    unsigned long       mapId,
    unsigned long       mapSizeX, 
    unsigned long       mapSizeY, 
    TQ3StoragePixmap    *bMap);


#ifdef __cplusplus
}
#endif  /* __cplusplus */


#endif  /*  PictRead_h  */
```

[Next](PickOnePrefix.h.md)[Previous](headers-PickOnewindow.h.md)

