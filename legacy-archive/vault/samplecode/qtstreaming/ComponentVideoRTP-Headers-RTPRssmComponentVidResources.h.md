---
title: qtstreaming
apple_id: DTS10001051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming/Listings/ComponentVideoRTP_Headers_RTPRssmComponentVidResources_h.html
archived_at: '2026-07-26T19:53:05.831080Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming](qtstreaming.md)


[Next](ComponentVideoRTP-Sources-ComponentThing.r.md)[Previous](ComponentVideoRTP-Headers-RTPRssmComponentVideoDispatch.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# ComponentVideoRTP/Headers/RTPRssmComponentVidResources.h

```c
/*
    File:       RTPRssmComponentVidResources.h

    Contains:   Declarations for Component Video RTPReassembler resources

    Copyright:  © 1997-1999 by Apple Computer Inc. all rights reserved.

*/

#ifndef __RTPRSSMCOMPONENTVIDRESOURCES__
#define __RTPRSSMCOMPONENTVIDRESOURCES__

#include "ComponentVideoRTPResources.h"

/* ---------------------------------------------------------------------------
 *      M A C R O S
 * ---------------------------------------------------------------------------
 */

/*  change these for your component */
/*  type and ID have to match what's in the code warrior project! */

#define COMPONENT_NAME_STRING                   "Sample Component Video Reassembler"
#define COMPONENT_INFO_STRING                   "Sample Component Video Reassembler"

#define COMPONENT_ENTRY_POINT_STRING            "RTPRssmComponentVideo_ComponentDispatch"
#define COMPONENT_PPC_PEF_STRING                "RTPRssmComponentVideo.pef"
#define COMPONENT_68K_CODE_STRING               "RTPRssmComponentVideo.rsrc"

#define COMPONENT_VIDEO_CODEC_NAME_STRING       "Component Video"

/* ---------------------------------------------------------------------------
 *      C O N S T A N T S
 * ---------------------------------------------------------------------------
 */

enum
{
    kComponentType                  = kRTPReassemblerType,
    kComponentSubType               = kComponentVideoDataFormat
};

enum
{
    kComponentBaseID                = 256,
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
    kRTPRssmComponentVideoRegistrationResource  = kComponentBaseID,
    kRTPRssmComponentVideoStringListResource    = kComponentBaseID,
        kRTPRssmComponentVideoCodecNameString   = 1
};

#endif /* __RTPRSSMCOMPONENTVIDRESOURCES__ */
```

[Next](ComponentVideoRTP-Sources-ComponentThing.r.md)[Previous](ComponentVideoRTP-Headers-RTPRssmComponentVideoDispatch.h.md)

