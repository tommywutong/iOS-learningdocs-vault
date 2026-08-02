---
title: OTPAPSampleServer
apple_id: DTS10000252
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OTPAPSampleServer/Listings/ATalkSampleUtils_h.html
archived_at: '2026-07-18T03:17:17.076247Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTPAPSampleServer](OTPAPSampleServer.md)


[Next](EnableEOMSample.c.md)[Previous](ATalkSampleUtils.c.md)

# ATalkSampleUtils.h

```c
/*
    File:       ATalkSample.h

    Contains:   Some utility routines used by the Sample programs

    Copyright:  © 1993-1995 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __ATALKSAMPLEUTILS__
#define __ATALKSAMPLEUTILS__

#include "OpenTransport.h"
#include "OpenTptAppleTalk.h"


void Idle(void);
void ShowEndpointInfo(EndpointRef ep);
void ShowEndpointState(EndpointRef ep, char* prefixString);
void ShowFullEndpointData(EndpointRef ep);
void ShowDDPAddress(DDPAddress* addr);

#endif
```

[Next](EnableEOMSample.c.md)[Previous](ATalkSampleUtils.c.md)

