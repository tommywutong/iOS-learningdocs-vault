---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/ComponentVideoRTP_RTPMPComponentVideo_Headers_ComponentVideoRTPResources_h.html
archived_at: '2026-07-18T03:21:10.386098Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](ComponentVideoRTP-RTPMPComponentVideo-Headers-RTPDefines.h.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Headers-ComponentVideoRTP.h.md)

# ComponentVideoRTP/RTPMPComponentVideo/Headers/ComponentVideoRTPResources.h

```c
/*
    File:       ComponentVideoRTPResources.h

    Contains:   Declarations for Component Video RTP component resources

    Copyright:  © 1997-1999 by Apple Computer Inc. all rights reserved.

*/



#ifndef __RTPRSSMCOMPONENTVIDEORESOURCES__
#define __RTPRSSMCOMPONENTVIDEORESOURCES__



/* ---------------------------------------------------------------------------
 *      H E A D E R S
 * ---------------------------------------------------------------------------
 */


#ifdef REZ
#   define thng_RezTemplateVersion  2   /* use extended 'thng' resource with resource map */
#   include "Components.r"
#   include "RTPDefines.h"
#else
#   include <Components.h>
#   include <QTStreamingComponents.h>
#endif /* REZ */



#include "ComponentVideoRTP.h"



/* ---------------------------------------------------------------------------
 *      M A C R O S
 * ---------------------------------------------------------------------------
 */


#define COMPONENT_VIDEO_PROTOCOL_ENCODING_STRING    "X-Sample-YUV-422-v0"
#define COMPONENT_VIDEO_HI_ENCODING_STRING          "Sample YUV 4:2:2"



#endif /* __RTPRSSMCOMPONENTVIDEORESOURCES__ */
```

[Next](ComponentVideoRTP-RTPMPComponentVideo-Headers-RTPDefines.h.md)[Previous](ComponentVideoRTP-RTPMPComponentVideo-Headers-ComponentVideoRTP.h.md)

