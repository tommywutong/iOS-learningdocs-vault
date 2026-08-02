---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CUtils_h.html
archived_at: '2026-07-18T03:14:26.717373Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](QTVRPanoAuthoring.h.md)[Previous](CUtils.cp.md)

# CUtils.h

```c
/*
    Random and sundry error, file and path name utilities

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#pragma once

#include <ImageCompression.h>

#include <LWindow.h>

void GetFullPathName(
    const FSSpec *fileSpec,
    Str255 outPathName,
    short maxSize = 255);
OSErr FSpGetFullPath(
    const FSSpec *spec,
    short *fullPathLength,
    Handle *fullPath);
void ElipsedPathName(
    Str255 pathName,
    short maxWidth,
    Str255 elipsedName,
    char elipsis);
void ElipsedPathNameH(
    Handle pathNameH,
    short maxWidth,
    Str255 elipsedName,
    char elipsis);
void SetSizedDescriptor(
    LWindow *parent,
    PaneIDT inPaneID,
    StringPtr inDescStr);
void ReportError(
    ExceptionCode inErr,
    Int16 inStrIndex);
OSErr GetFileParent(
    FSSpec *fileSpec,
    FSSpec *parentSpec);
void ReadPictFrame(
    const FSSpec &inPictSpec,
    Rect &outPictRect);
void FixedToStr(
    Fixed inFixValue,
    Str255 outStr);
Fixed StrToFixed(
    StringPtr str);
Boolean FindCodecName(
    StringPtr outName,
    CodecType inCodec);
void SetCompressionText(
    LPane *inPane,
    CodecType inCodec,
    CodecQ inSpatialQuality);


enum
{
    err_Window = 1,
    err_OpenPicture = 2,
    err_CreateTileMovie = 3,
    err_CreatePanoMovie = 4,
    err_BadPictHeight = 5,
    err_ErrorSettingCompression = 6,
    STRx_Errors = 222
};

enum
{
    err_NotEnufMemory = 1,
    err_DiskError = 2,
    err_DiskFull = 3,
    err_NoDescription = 4,
    err_NoResource = 5,
    err_NotEnufPhysicalMemory = 6,
    STRx_ErrorDescs = 224
};

const ResIDT ALRT_Error = 129;
```

[Next](QTVRPanoAuthoring.h.md)[Previous](CUtils.cp.md)

