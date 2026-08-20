---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/ComponentVideoRTP_Headers_ComponentVideoRTPResources_h.html
archived_at: '2026-07-18T03:21:15.081757Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](ComponentVideoRTP-Headers-RTPDefines.h.md)[Previous](ComponentVideoRTP-Headers-ComponentVideoRTP.h.md)

# ComponentVideoRTP/Headers/ComponentVideoRTPResources.h

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

[Next](ComponentVideoRTP-Headers-RTPDefines.h.md)[Previous](ComponentVideoRTP-Headers-ComponentVideoRTP.h.md)

