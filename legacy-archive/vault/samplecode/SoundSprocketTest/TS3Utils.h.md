---
title: SoundSprocketTest
apple_id: DTS10000060
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundSprocketTest/Listings/TS3Utils_h.html
archived_at: '2026-07-18T03:25:11.265809Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundSprocketTest](SoundSprocketTest.md)


[Next](TS3Window.c.md)[Previous](TS3Utils.c.md)

# TS3Utils.h

```c
/*
 *  File:       TS3Utils.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __TS3Utils__
#define __TS3Utils__

#include <Dialogs.h>
#include <Types.h>

#include <QD3D.h>


void Utils_Init(
    void);

void Utils_Exit(
    void);

float Utils_Interval(
    const UnsignedWide* inPrevTime,
    const UnsignedWide* inCurrTime);

UserItemUPP Utils_GetOKUserItemProc(
    void);

void Utils_SetStr255Field(
    DialogPtr           inDialog,
    short               inItem,
    ConstStr255Param    inValue,
    Boolean             inHasValue);

Boolean Utils_GetStr255Field(
    DialogPtr           inDialog,
    short               inItem,
    Str255              outValue,
    Boolean*            outHasValue);

void Utils_SetUInt32Field(
    DialogPtr           inDialog,
    short               inItem,
    UInt32              inValue,
    Boolean             inHasValue);

Boolean Utils_GetUInt32Field(
    DialogPtr           inDialog,
    short               inItem,
    UInt32*             outValue,
    Boolean*            outHasValue,
    UInt32              inMin,
    UInt32              inMax);

void Utils_SetFloatField(
    DialogPtr           inDialog,
    short               inItem,
    float               inValue,
    Boolean             inHasValue);

Boolean Utils_GetFloatField(
    DialogPtr           inDialog,
    short               inItem,
    float*              outValue,
    Boolean*            outHasValue,
    float               inMin,
    float               inMax);

void Utils_SetVector3DField(
    DialogPtr           inDialog,
    short               inItem,
    const TQ3Vector3D*  inValue,
    Boolean             inHasValue);

Boolean Utils_GetVector3DField(
    DialogPtr           inDialog,
    short               inItem,
    TQ3Vector3D*        outValue,
    Boolean*            outHasValue);


#endif /* __TS3Utils__ */
```

[Next](TS3Window.c.md)[Previous](TS3Utils.c.md)

