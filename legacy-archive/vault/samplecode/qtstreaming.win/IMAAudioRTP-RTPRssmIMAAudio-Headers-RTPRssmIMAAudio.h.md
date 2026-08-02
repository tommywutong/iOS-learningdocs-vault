---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/IMAAudioRTP_RTPRssmIMAAudio_Headers_RTPRssmIMAAudio_h.html
archived_at: '2026-07-26T19:53:07.147834Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPRssmIMAAudioDispatch.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPDefines.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# IMAAudioRTP/RTPRssmIMAAudio/Headers/RTPRssmIMAAudio.h

```c
/*
    File:       RTPRssmIMAAudio.h

    Contains:   Declarations for IMA Audio RTPReassembler

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __RTPRSSMCOMPONENTVIDEO__
#define __RTPRSSMCOMPONENTVIDEO__

#pragma once

/* ---------------------------------------------------------------------------
 *      H E A D E R S
 * ---------------------------------------------------------------------------
 */

#include <QTStreamingComponents.h>
#include "IMAAudioRTP.h"

/* ---------------------------------------------------------------------------
 *      D A T A T Y P E S
 * ---------------------------------------------------------------------------
 *
 *  An RTPRssmIMAAudioInstanceData structure stores instance variables
 *  for an IMA Audio RTPReassembler instance.  The structure declares the
 *  following fields:
 *
 *      itself                      the RTPReassembler instance that maintains
 *                                  this data structure
 *
 *      itsBase                     the RTPReassembler to which the instance
 *                                  delegates calls
 *
 *      itsFinalDerivation          the RTPReassembler instance to which the
 *                                  instance targets calls to itself
 *
 *      itsPayloadAttributes        cached attributes of incoming payloads
 *
 */

typedef struct
{
    RTPReassembler      itself;
    RTPReassembler      itsBase;
    RTPReassembler      itsFinalDerivation;
    IMAAudioPayload     itsPayloadAttributes;
} RTPRssmIMAAudioInstanceData;

#endif /* __RTPRSSMCOMPONENTVIDEO__ */
```

[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPRssmIMAAudioDispatch.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPDefines.h.md)

