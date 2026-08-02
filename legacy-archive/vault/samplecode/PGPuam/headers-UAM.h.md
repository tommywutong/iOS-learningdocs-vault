---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/headers_UAM_h.html
archived_at: '2026-07-18T03:18:29.683251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](In%20process-dumpuserInfo.c.md)[Previous](headers-RegisterFileLibs.h.md)

# headers/UAM.h

```c
/*
    File:       UAM.h

    Contains:   xxx put contents here xxx

    Version:    AppleShare IP

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         AppleShare IP

    Writers:

        (EAS)   Erik Sea
        (AKN)   Akira Nonaka

    Change History (most recent first):

       <AS7>     8/29/98    EAS     Take out a duplicate structure from OAMTypes.h
       <AS6>     8/17/98    AKN     added UAMChangeUID()
       <AS5>     8/13/98    AKN     First checked in.
*/

// UAM.h

#pragma once

/*  vin... 
#include "OAMTypes.h"
*/

enum { kUAMAuthLogin, kUAMAuthLoginContinue, kUAMAuthChangeKey, kUAMAuthChangeKeyContinue };
enum { kUAMAuthObject = 0, kUAMAuthStream = 1 };


#ifdef __cplusplus
extern "C" {
#endif

#ifdef AGENT
typedef OSStatus    OAMStatus;
typedef OSType      OAMType;
typedef OSType      OAMObjectType;
typedef struct OAMObjectSpec OAMObjectSpec;
typedef UInt32      OAMShortObjectSpec, *OAMShortObjectSpecPtr;
#endif
extern OAMStatus UAMGetAttributeID(UInt32 id, OSType creator, OSType type, void *buffer, UInt32 *size);
extern OAMStatus UAMSetAttributeID(UInt32 id, OSType creator, OSType type, void *buffer, UInt32 *size);

extern OAMStatus UAMGetAttribute(OAMObjectSpec* obj, OSType creator, OSType type, void *buffer, UInt32 *size);
extern OAMStatus UAMSetAttribute(OAMObjectSpec* obj, OSType creator, OSType type, void *buffer, UInt32 *size);
extern OAMStatus UAMCreateObject(OAMObjectSpec* obj);
extern UInt32 UAMGetThreadID();
extern UInt32 UAMSleep(UInt32 msec);
extern void UAMWakeup(UInt32 id,UInt32 refCon);
extern OAMStatus UAMChangeUID(UInt32 newID);
#ifdef __cplusplus
}
#endif
```

[Next](In%20process-dumpuserInfo.c.md)[Previous](headers-RegisterFileLibs.h.md)

