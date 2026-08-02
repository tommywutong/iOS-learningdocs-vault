---
title: RollerCoaster
apple_id: DTS10000881
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RollerCoaster/Listings/Interfaces_Win32Application_h.html
archived_at: '2026-07-18T03:22:14.817617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RollerCoaster](RollerCoaster.md)


[Next](Interfaces-WinPrefix.h.md)[Previous](Interfaces-Utils.h.md)

# Interfaces/Win32Application.h

```c
/*
    File:       Win32Application.h

    Contains:   Interface file for Win32Application.c

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

/* Windows headers */
#define STRICT
#include <windows.h>        // required for all Windows applications
#include "resource.h"       // Windows resource IDs

#include <stdio.h>

#include "Document.h"
#include "QD3DSupport.h"

#include "QD3DIO.h"
#include "QD3DErrors.h"
#include "QD3DStorage.h"
```

[Next](Interfaces-WinPrefix.h.md)[Previous](Interfaces-Utils.h.md)

