---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPRssmIMAAudio_Headers_IMAAudioRTP_h.html
archived_at: '2026-07-18T03:21:14.207359Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioRTPResources.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioPayload.h.md)

# IMAAudioRTP/RTPRssmIMAAudio/Headers/IMAAudioRTP.h

```
/*
    File:       IMAAudioRTP.h

    Contains:   Declarations for IMA Audio RTP components

    Copyright:  © 1997-1999 by Apple Computer Inc. all rights reserved.

*/



#ifndef __COMPONENTVIDEORTP__
#define __COMPONENTVIDEORTP__



/* ---------------------------------------------------------------------------
 *      H E A D E R S
 * ---------------------------------------------------------------------------
 */

#ifdef REZ
#   include "ConditionalMacros.r"
#else
#   include <ConditionalMacros.h>
#   include "IMAAudioPayload.h"
#endif /* REZ */



/* ---------------------------------------------------------------------------
 *      C O N S T A N T S
 * ---------------------------------------------------------------------------
 */

#ifdef REZ
enum
{
    kIMAAudioDataFormat         = 'ima4',   /* kIMACompression */
    kComponentManufactureType   = 'SMPL'
};
#else
enum
{
    kIMAAudioDataFormat         = FOUR_CHAR_CODE( 'ima4' ), /* kIMACompression */
    kComponentManufactureType   = FOUR_CHAR_CODE( 'SMPL' )
};
#endif /* REZ */



#endif /* __COMPONENTVIDEORTP__ */
```

[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioRTPResources.h.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioPayload.h.md)

