---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/ComponentVideoRTP_RTPMPComponentVideo_Sources_RTPMPComponentVideo_r.html
archived_at: '2026-07-26T19:53:06.617638Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](ComponentVideoRTP-RTPRssmComponentVideo-Headers-ComponentVideoPayload.h.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Sources-RTPMPComponentVideo.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# ComponentVideoRTP/RTPMPComponentVideo/Sources/RTPMPComponentVideo.r

```c
/*
    File:       RTPMPComponentVideo.r

    Contains:   Resources for Component Video RTPMediaPacketizer

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    An RTPMediaPaketizer must define at least one packetizer info resource ('pcki')
    and a public component resource map ('thnr') that points to the packetizer info
    resources.

    QuickTime Streaming uses a packetizer info resource to determine what media data
    format a packetizer encodes, and to compare packetizers that encode the same
    type of data.
*/

#undef DLOG_RezTemplateVersion
#define DLOG_RezTemplateVersion 1

#include "RTPMPComponentVideoResources.h"
#include "ComponentThing.r"
#include "Controls.r"
#include "ControlDefinitions.r"
#include "Dialogs.r"
#include "MacTypes.r"
#include "Menus.r"
#include "QTStreamingComponents.r"

resource 'STR#' ( kRTPMPComponentVideoStringListResource )
{
    {
        COMPONENT_VIDEO_PROTOCOL_ENCODING_STRING,   // kRTPMPComponentVideoProtocolEncodingString
        COMPONENT_VIDEO_HI_ENCODING_STRING          // kRTPMPComponentVideoHIEncodingString
    }
};

resource 'thnr' ( kComponentBaseID )
{
    {
        'pcki', 1, 0,
        'pcki', kComponentBaseID, cmpResourceNoFlags,
    }
};

resource 'pcki' ( kComponentBaseID )
{
    {
        'vide',                             // media type
        kComponentVideoDataFormat,          // data format type
        kComponentManufactureType,
        kMediaPacketizerCanPackEditRate | kMediaPacketizerCanPackEmptyEdit,
        canPackIdentityMatrixType,
        {
            kRTPPayloadSpeedTag, 128,
            kRTPPayloadLossRecoveryTag, 128
        },
        kRTPPayloadTypeDynamicFlag,
        0,
        COMPONENT_VIDEO_PROTOCOL_ENCODING_STRING
    }
};
```

[Next](ComponentVideoRTP-RTPRssmComponentVideo-Headers-ComponentVideoPayload.h.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Sources-RTPMPComponentVideo.c.md)

