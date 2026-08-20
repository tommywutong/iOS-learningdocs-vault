---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/IMAAudioRTP_Headers_RTPMPIMAAudio_h.html
archived_at: '2026-07-18T03:21:16.771426Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](IMAAudioRTP-Headers-RTPMPIMAAudioDispatch.h.md)[Previous](IMAAudioRTP-Headers-RTPDefines.h.md)

# IMAAudioRTP/Headers/RTPMPIMAAudio.h

```c
/*
    File:       RTPMPIMAAudio.h

    Contains:   Declarations for IMA Audio RTPMediaPacketizer

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __RTPMPCOMPONENTVIDEO__
#define __RTPMPCOMPONENTVIDEO__

#pragma once



/* ---------------------------------------------------------------------------
 *      H E A D E R S
 * ---------------------------------------------------------------------------
 */

#include <QTStreamingComponents.h>
#include "IMAAudioRTP.h"
#include "IMAAudioQueue.h"



/* ---------------------------------------------------------------------------
 *      D A T A T Y P E S
 * ---------------------------------------------------------------------------
 *
 *  An RTPMPIMAAudioInstanceData structure stores instance variables for
 *  an IMA Audio RTPMediaPacketizer instance.  The structure declares the
 *  following fields:
 *  
 *      itself                      the RTPMediaPacketizer instance that
 *                                  maintains this data structure
 *      
 *      itsBase                     the RTPMediaPacketizer to which the
 *                                  instance delegates calls
 *      
 *      itsFinalDerivation          the RTPMediaPacketizer instance to which
 *                                  the instance targets calls to itself
 *      
 *      itsInSystemHeap             true when this data structure resides in
 *                                  the system heap
 *      
 *      itsLockCount                count of execution contexts requiring that
 *                                  the instance data remain non-relocatable
 *      
 *      itsInitialized              true when the instance has initialized the
 *                                  remaining fields
 *      
 *      itsExpectedTimestamp        on entry to the RTPMPSetSamplData()
 *                                  implementation, this field should match
 *                                  the timeStamp field of the
 *                                  RTPMPSampleDataParams parameter
 *
 *      itsPayloadAttributesInitialized
 *                                  true when itsPayloadAttributes has been
 *                                  initialized from a sample description
 *
 *      itsPayloadAttributes        precomputed values for header the instance
 *                                  includes with each payload
 *
 *      itsSampleDescriptionSeed    the seed of the SampleDescription the
 *                                  instance is using for sample data
 *      
 *      itsAudioQueue               audio data awaiting packetization
 *
 *      itsPacketBuilder            the RTPMPPacketBuilder the instance uses
 *                                  to contruct network packets
 *      
 *      itsMediaTimeScale           the TimeScale of the source sample data
 *      
 *      itsMediaTimeBase            the TimeBase passed to RTPMPSetTimeBase()
 *      
 *      itsPayloadSizeLimit         the maximum allowable size, in octets, of
 *                                  payloads the instance may contruct
 *      
 *      itsPayloadDurationLimit     the maximum allowable duration of sample
 *                                  data the instance may encapsulate in a
 *                                  single payload
 *      
 *      itsInterleaveGroupFrameCount
 *                                  number of frames of sample data to
 *                                  encapsulate in a single interleave group
 *      
 */

typedef struct
{
    RTPMediaPacketizer  itself;
    RTPMediaPacketizer  itsBase;
    RTPMediaPacketizer  itsFinalDerivation;
    Boolean             itsInSystemHeap;
    UInt32              itsLockCount;
    Boolean             itsInitialized;
    UInt32              itsExpectedTimestamp;
    Boolean             itsPayloadAttributesInitialized;
    IMAAudioPayload     itsPayloadAttributes;
    UInt32              itsSampleDescriptionSeed;
    IMAAudioQueue       itsAudioQueue;
    RTPPacketBuilder    itsPacketBuilder;
    TimeScale           itsMediaTimeScale;
    TimeBase            itsMediaTimeBase;
    UInt32              itsPayloadSizeLimit;
    UInt32              itsPayloadDurationLimit;
    UInt32              itsInterleaveGroupFrameCount;
} RTPMPIMAAudioInstanceData;



#endif /* __RTPMPCOMPONENTVIDEO__ */
```

[Next](IMAAudioRTP-Headers-RTPMPIMAAudioDispatch.h.md)[Previous](IMAAudioRTP-Headers-RTPDefines.h.md)

