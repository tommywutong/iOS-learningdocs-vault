---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/ComponentVideoRTP_RTPMPComponentVideo_Headers_RTPMPComponentVideoResources_h.html
archived_at: '2026-07-18T03:21:10.718490Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](ComponentVideoRTP-RTPMPComponentVideo-Sources-ComponentThing.r.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Headers-RTPMPComponentVideoDispatch.h.md)

# ComponentVideoRTP/RTPMPComponentVideo/Headers/RTPMPComponentVideoResources.h

```c
/*
    File:       RTPMPComponentVideoResources.h

    Contains:   Declarations for Component Video RTPMediaPacketizer resources

    Copyright:  © 1997-1999 by Apple Computer Inc. all rights reserved.

*/



#ifndef __RTPMPCOMPONENTVIDEORESOURCES__
#define __RTPMPCOMPONENTVIDEORESOURCES__



#include "ComponentVideoRTPResources.h"



/* ---------------------------------------------------------------------------
 *      M A C R O S
 * ---------------------------------------------------------------------------
 */

/*  change these for your component */
/*  type and ID have to match what's in the code warrior project! */

#define COMPONENT_NAME_STRING                   "Sample Component Video Media Packetizer"
#define COMPONENT_INFO_STRING                   "Sample Component Video Media Packetizer"

#define COMPONENT_ENTRY_POINT_STRING            "RTPMPComponentVideo_ComponentDispatch"
#define COMPONENT_PPC_PEF_STRING                "RTPMPComponentVideo.pef"
#define COMPONENT_68K_CODE_STRING               "RTPMPComponentVideo.rsrc"



enum
{
    kComponentType                  = kRTPMediaPacketizerType,
    kComponentSubType               = kComponentVideoDataFormat
};

enum
{
    kComponentBaseID                = 128,
    kComponentBaseIDPPC             = kComponentBaseID
};

#define kComponentBaseID68K         ( kComponentBaseID + 1 )

enum
{
    kComponentVersion               = 0x00010001,
    kComponentFlags                 = 0
};

#define kComponentRegFlags          ( componentDoAutoVersion | componentHasMultiplePlatforms )

enum
{
    kRTPMPComponentVideoStringListResource          = kComponentBaseID,
        kRTPMPComponentVideoProtocolEncodingString  = 1,
        kRTPMPComponentVideoHIEncodingString        = 2
};



#endif /* __RTPMPCOMPONENTVIDEORESOURCES__ */
```

[Next](ComponentVideoRTP-RTPMPComponentVideo-Sources-ComponentThing.r.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Headers-RTPMPComponentVideoDispatch.h.md)

