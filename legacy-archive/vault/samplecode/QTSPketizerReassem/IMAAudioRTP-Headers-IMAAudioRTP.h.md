---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/IMAAudioRTP_Headers_IMAAudioRTP_h.html
archived_at: '2026-07-18T03:21:16.575987Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](IMAAudioRTP-Headers-IMAAudioRTPResources.h.md)[Previous](IMAAudioRTP-Headers-IMAAudioQueue.h.md)

# IMAAudioRTP/Headers/IMAAudioRTP.h

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

[Next](IMAAudioRTP-Headers-IMAAudioRTPResources.h.md)[Previous](IMAAudioRTP-Headers-IMAAudioQueue.h.md)

