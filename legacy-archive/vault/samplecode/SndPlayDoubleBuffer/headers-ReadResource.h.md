---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_ReadResource_h.html
archived_at: '2026-07-18T03:24:54.937495Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-SetupDBHeader.h.md)[Previous](headers-PrivateDBFFFunctions.h.md)

# _headers/ReadResource.h

```c
/*
    File:       ReadResource.h

    Contains:   Header for routines demonstrating how to read resource files without
                using the Resource Manager.

    Written by:  Mark Cookson

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/31/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef __READRESOURCE__
#define __READRESOURCE__

#include <Errors.h>
#include <Resources.h>

#ifndef __DEFINES__
#include "Defines.h"
#endif

struct ResourceHeader {
    long            resDataOffset;
    long            resMapOffset;
    long            resDataLength;
    long            resMapLength;
};
typedef struct ResourceHeader ResourceHeader;

struct ResourceMap {
    unsigned char   reserved1[16];//for copy of resource header
    long            reserved2;//for handle to next resource map
    short           reserved3;//for file reference number
    short           resFileAttrs;
    unsigned short  typesListOffset;
    unsigned short  namesListOffset;
    unsigned short  numTypesInMap;
};
typedef struct ResourceMap ResourceMap;

struct ResourceTypeListEntry {
    OSType          resType;
    unsigned short  numEntries;
    unsigned short  referenceOffset;
};
typedef struct ResourceTypeListEntry ResourceTypeListEntry;

struct ResReference {
    short           ID;
    unsigned short  nameOffset;
    long            dataOffset;//high byte is actually resource attributes, low three bytes are offset to beginning of data
    long            reserved;//for handle to resource
};
typedef struct ResReference ResReference;

        OSErr   MyGetFirstResource      (short refNum,
                                        OSType targetType,
                                        short *targetID);

        OSErr   MyGetResourcePosition   (short refNum,
                                        OSType targetType,
                                        short targetID,
                                        long *firstByte);

        OSErr   MyGetTypesPosition      (short refNum,
                                        OSType theType,
                                        short *numResources,
                                        long *dataOffset,
                                        long *firstByteOfTypeList);

#endif
```

[Next](headers-SetupDBHeader.h.md)[Previous](headers-PrivateDBFFFunctions.h.md)

