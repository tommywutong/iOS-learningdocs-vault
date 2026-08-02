---
title: AEObject-Edition Sample
apple_id: DTS10000204
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEObject-Edition_Sample/Listings/Sampdefines_h.html
archived_at: '2026-07-18T02:59:30.851142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEObject-Edition Sample](AEObject-Edition%20Sample.md)


[Next](Structs.h.md)[Previous](SampConstants.h.md)

# Sampdefines.h

```c
/*------------------------------------------------------------------------------
 *
 *  Apple Developer Technical Support
 *
 *  Edition publishing routines
 *
 *  Program:    AEObject-Edition Sample
 *  File:       SampDefines.h - C Source
 *
 *  by:         C.K. Haun <TR>
 *
 *  Copyright © 1990-1992 Apple Computer, Inc.
 *  All rights reserved.
 *
 *------------------------------------------------------------------------------
 * This file loads the defines, macros, and prototypes I use in this sample
 *----------------------------------------------------------------------------*/

#ifndef __DEFINES__
#define __DEFINES__

#ifdef __REDUMP__
#include "SampConstants.h"
#include "Structs.h"
#include "prototypes.h"
#include "Macros.h"

#else
#pragma load "Sampheaders"      /* see the Buildheaders.c file */
#endif 

#endif
```

[Next](Structs.h.md)[Previous](SampConstants.h.md)

