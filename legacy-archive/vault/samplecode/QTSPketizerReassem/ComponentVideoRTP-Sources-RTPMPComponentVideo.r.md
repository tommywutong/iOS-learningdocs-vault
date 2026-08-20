---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/ComponentVideoRTP_Sources_RTPMPComponentVideo_r.html
archived_at: '2026-07-18T03:21:15.971745Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](ComponentVideoRTP-Sources-RTPRssmComponentVideo.c.md)[Previous](ComponentVideoRTP-Sources-RTPMPComponentVideo.c.md)

# ComponentVideoRTP/Sources/RTPMPComponentVideo.r

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
};
```

[Next](ComponentVideoRTP-Sources-RTPRssmComponentVideo.c.md)[Previous](ComponentVideoRTP-Sources-RTPMPComponentVideo.c.md)

