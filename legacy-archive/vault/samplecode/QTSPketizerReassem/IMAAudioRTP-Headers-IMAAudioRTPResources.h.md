---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/IMAAudioRTP_Headers_IMAAudioRTPResources_h.html
archived_at: '2026-07-18T03:21:16.545744Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](IMAAudioRTP-Headers-RTPDefines.h.md)[Previous](IMAAudioRTP-Headers-IMAAudioRTP.h.md)

# IMAAudioRTP/Headers/IMAAudioRTPResources.h

```c
/*
    File:       IMAAudioRTPResources.h

    Contains:   Declarations for IMA Audio RTP component resources

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



#include "IMAAudioRTP.h"



/* ---------------------------------------------------------------------------
 *      M A C R O S
 * ---------------------------------------------------------------------------
 */

#define IMA_AUDIO_PROTOCOL_ENCODING_STRING  "X-Sample-IMA-ADPCM-4-1-v0"
#define IMA_AUDIO_HI_ENCODING_STRING        "Sample IMA 4:1 Audio"



#endif /* __RTPRSSMCOMPONENTVIDEORESOURCES__ */
```

[Next](IMAAudioRTP-Headers-RTPDefines.h.md)[Previous](IMAAudioRTP-Headers-IMAAudioRTP.h.md)

