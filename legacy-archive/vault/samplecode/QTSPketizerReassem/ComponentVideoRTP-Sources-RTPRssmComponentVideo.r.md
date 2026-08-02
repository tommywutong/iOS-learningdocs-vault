---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/ComponentVideoRTP_Sources_RTPRssmComponentVideo_r.html
archived_at: '2026-07-18T03:21:16.366565Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](IMAAudioRTP-Headers-IMAAudioPayload.h.md)[Previous](ComponentVideoRTP-Sources-RTPRssmComponentVideo.c.md)

# ComponentVideoRTP/Sources/RTPRssmComponentVideo.r

```c
/*
    File:       RTPRssmComponentVideo.r

    Contains:   Resources for Component Video RTPReassembler

    Copyright:  © 1997-1998 by Apple Computer, Inc., all rights reserved.



    An RTPReassembler must define at least one reassembler info resource
    (kRTPReassemblerInfoResType) and a public component resource map ('thnr') that
    points to the reassembler info resources.

    QuickTime Streaming uses a reassembler info resource to determine what RTP
    payload type a reassembler handles, and to compare reassemblers that handle the
    same payload type.
*/

#define SystemSevenOrLater 1
#define SystemSevenOrBetter 1


#include "RTPRssmComponentVidResources.h"
#include "QTStreamingComponents.r"
#include "ComponentThing.r"



resource 'STR#' ( kRTPRssmComponentVideoStringListResource )
{
    {
        COMPONENT_VIDEO_CODEC_NAME_STRING
    }
};



resource 'thnr' ( kComponentBaseID )
{
    {
        kRTPReassemblerInfoResType, 1, 0,
        kRTPReassemblerInfoResType, kComponentBaseID, cmpResourceNoFlags,
    }
};



resource kRTPReassemblerInfoResType ( kComponentBaseID )
{
    {
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

[Next](IMAAudioRTP-Headers-IMAAudioPayload.h.md)[Previous](ComponentVideoRTP-Sources-RTPRssmComponentVideo.c.md)

