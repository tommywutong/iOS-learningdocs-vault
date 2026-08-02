---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/ComponentVideoRTP_RTPRssmComponentVideo_Headers_RTPRssmComponentVideo_h.html
archived_at: '2026-07-18T03:21:11.722448Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](ComponentVideoRTP-RTPRssmComponentVideo-Headers-RTPRssmComponentVideoDispatch.h.md)[Previous](ComponentVideoRTP-RTPRssmComponentVideo-Headers-RTPDefines.h.md)

# ComponentVideoRTP/RTPRssmComponentVideo/Headers/RTPRssmComponentVideo.h

```c
/*
    File:       RTPRssmComponentVideo.h

    Contains:   Declarations for Component Video RTPReassembler

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
#include "ComponentVideoRTP.h"



/* ---------------------------------------------------------------------------
 *      D A T A T Y P E S
 * ---------------------------------------------------------------------------
 *
 *  An RTPRssmComponentVideoInstanceData structure stores instance variables
 *  for a Component Video RTPReassembler instance.  The structure declares the
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
 *      itsSavedChunk               the most recent frame of reassembled
 *                                  sample data
 *
 */

typedef struct
{
    RTPReassembler          itself;
    RTPReassembler          itsBase;
    RTPReassembler          itsFinalDerivation;
    ComponentVideoPayload   itsPayloadAttributes;
    SHChunkRecord *         itsSavedChunk;
} RTPRssmComponentVideoInstanceData;



#endif /* __RTPRSSMCOMPONENTVIDEO__ */
```

[Next](ComponentVideoRTP-RTPRssmComponentVideo-Headers-RTPRssmComponentVideoDispatch.h.md)[Previous](ComponentVideoRTP-RTPRssmComponentVideo-Headers-RTPDefines.h.md)

