---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPRssmIMAAudio_Headers_RTPRssmIMAAudioResources_h.html
archived_at: '2026-07-18T03:21:14.380239Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPRssmIMAAudio-Sources-ComponentThing.r.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPRssmIMAAudioDispatch.h.md)

# IMAAudioRTP/RTPRssmIMAAudio/Headers/RTPRssmIMAAudioResources.h

```c
/*
    File:       RTPRssmIMAAudioResources.h

    Contains:   Declarations for IMA Audio RTPReassembler resources

    Copyright:  © 1997-1999 by Apple Computer Inc. all rights reserved.

*/



#ifndef __RTPRSSMCOMPONENTVIDRESOURCES__
#define __RTPRSSMCOMPONENTVIDRESOURCES__



#include "IMAAudioRTPResources.h"



/* ---------------------------------------------------------------------------
 *      M A C R O S
 * ---------------------------------------------------------------------------
 */


/*  change these for your component */
/*  type and ID have to match what's in the code warrior project! */

#define COMPONENT_NAME_STRING                   "Sample IMA Audio Reassembler"
#define COMPONENT_INFO_STRING                   "Sample IMA Audio Reassembler"

#define COMPONENT_ENTRY_POINT_STRING            "RTPRssmIMAAudio_ComponentDispatch"
#define COMPONENT_PPC_PEF_STRING                "RTPRssmIMAAudio.pef"
#define COMPONENT_68K_CODE_STRING               "RTPRssmIMAAudio.rsrc"



/* ---------------------------------------------------------------------------
 *      C O N S T A N T S
 * ---------------------------------------------------------------------------
 */


enum
{
    kComponentType                  = kRTPReassemblerType,
    kComponentSubType               = kIMAAudioDataFormat
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



#endif /* __RTPRSSMCOMPONENTVIDRESOURCES__ */
```

[Next](IMAAudioRTP-RTPRssmIMAAudio-Sources-ComponentThing.r.md)[Previous](IMAAudioRTP-RTPRssmIMAAudio-Headers-RTPRssmIMAAudioDispatch.h.md)

