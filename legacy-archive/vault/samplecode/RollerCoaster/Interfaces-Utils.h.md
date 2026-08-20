---
title: RollerCoaster
apple_id: DTS10000881
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RollerCoaster/Listings/Interfaces_Utils_h.html
archived_at: '2026-07-18T03:22:14.775458Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RollerCoaster](RollerCoaster.md)


[Next](Interfaces-Win32Application.h.md)[Previous](Interfaces-Track.h.md)

# Interfaces/Utils.h

```c
/*
    File:       Utils.h

    Contains:   Interface file for Utils.c

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

#include <MacTypes.h>

#if TARGET_OS_WIN32
    #define STRICT
    #include <windows.h>
    #include <WINNT.h>

    #include "QTML.h"
    #include "Components.h"
    #include "ImageCompression.h"
#endif

#include <TextUtils.h>
#include <Dialogs.h>
#include <Math.h>

#include "QD3D.h"
#include "QD3DMath.h"

/************************************************************
*                                                           *
*    FUNCTION PROTOTYPES                                    *
*                                                           *
*************************************************************/

void Utils_RotatePoint(TQ3Point3D *point, float yangle);
unsigned long Utils_MyRandomLong(void);
float Utils_AngleBetweenVectors(TQ3Vector3D v1, TQ3Vector3D v2);
void Utils_DisplayErrorMsg(char *msg);
void Utils_DisplayFatalErrorMsg(char *msg);

void Utils_Mac_GetPictForTexture(short      resourceID,
                                PicHandle   *picH,
                                Rect        *picRect);

#if TARGET_OS_WIN32
    DWORD Utils_Win32_BuildCurDirPath(LPTSTR path, LPTSTR filename);
    ComponentResult Utils_Win32_GetPicFromFile(LPTSTR       filePath,
                                                PicHandle   *picH,
                                                Rect        *picRect);
    Boolean Utils_Win32_DoesFileExist(LPTSTR filePath);
#endif
```

[Next](Interfaces-Win32Application.h.md)[Previous](Interfaces-Track.h.md)

