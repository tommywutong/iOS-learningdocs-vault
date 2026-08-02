---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/IMAAudioRTP_RTPRssmIMAAudio_Headers_IMAAudioRTPResources_h.html
archived_at: '2026-07-26T19:53:07.126345Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPDefines.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioRTP.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# IMAAudioRTP/RTPRssmIMAAudio/Headers/IMAAudioRTPResources.h

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

[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPDefines.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioRTP.h.md)

