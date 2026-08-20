---
title: PCCardNetworkSample
apple_id: DTS10000258
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PCCardNetworkSample/Listings/MyPortCalls_h.html
archived_at: '2026-07-18T03:18:21.268945Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PCCardNetworkSample](PCCardNetworkSample.md)


[Next](MyPortModule.c.md)[Previous](MyPortCalls.c.md)

# MyPortCalls.h

```
/*
    File:       MyPortCalls.h

    Contains:   Generic calls for working with the MyPortScanner sample, to allow a PC Card Enabler
                to force an OT port deregistration

    Written by: Rich Kubota 

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/16/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#pragma once

#define kVersionMajor   1
#define kVersionMinor   0
#define kVersionStage   developStage
#define kVersionNonRel  0

extern OSStatus CreatePortProperties(const RegEntryID *cardRef);
extern OSStatus MyAddDeviceProperties(const RegEntryID *cardRef, UInt32 device);
extern void     CallPortScanner(void);
extern void     EnablerOfflinePort(const RegEntryID *cardRef);
static Boolean IsOpenTransportPresent(void);  

const unsigned char gDriverName[] = kDriverName;
```

[Next](MyPortModule.c.md)[Previous](MyPortCalls.c.md)

