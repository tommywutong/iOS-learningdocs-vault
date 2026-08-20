---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_RemoveServerKey_c.html
archived_at: '2026-07-18T03:18:33.124158Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TAboutBoxPane.cp.md)[Previous](sources-PPCGlue.c.md)

# sources/RemoveServerKey.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h> /* needed for offsetof */
#include <string.h>
#include <console.h>
#include <sioux.h>
#include <PLStringFuncs.h>

#include "AppleShareRegistry.h"
#include "AppleShareFileServerRegistry.h"



void BuildObjectSpecByShortID(OAMObjectSpec *obj, OAMShortObjectSpec id)
{
    memset(obj, 0, sizeof(OAMObjectSpec));
    obj->specType = kOAMObjectSpecByShortID;
    obj->u.shortID = id;
}

void BuildObjectSpecByNameType(OAMObjectSpec *obj, StringPtr name, OAMType type)
{
    short len = 0;

    memset(obj, 0, sizeof(OAMObjectSpec));
    obj->specType = kOAMObjectSpecByNameType;
    obj->objectType = type;
    len = *name + 1;
    memcpy(obj->u.name, name, len);
}


OAMStatus RemoveServerKey(OAMSessionID sessionId)
{

    OAMStatus               err = noErr;
    OAMObjectSpec           obj;    
    OAMAttributeDescriptor  attr[2] = {};

    unsigned char           key[4096];

    memset(&attr, 0, sizeof(attr));

    attr[0].attributeSignature          = kOAMMachine;
    attr[0].attributeType               = 'PGPs';
    attr[0].bufferDescriptor.buffer     =  key;
    attr[0].bufferDescriptor.bufferLen  =  sizeof(key);
    attr[1].attributeSignature = NULL;

    memset(&obj, 0, sizeof(OAMObjectSpec));

    obj.specType = kOAMObjectSpecByShortID;
    obj.u.shortID = kOAMMachineShortID;

    err = OAMDeleteAttribute(sessionId, &obj,  attr, NULL);
    return err;

}

int main ( void)
{
    OAMStatus       err = noErr;
    OAMSessionID    sessionID = 0;

    err = OAMInitialize(1, 0, NULL, NULL);

    err = OAMOpenSession(NULL, &sessionID, NULL);
    if (sessionID)
    {
        err = RemoveServerKey( sessionID);

        OAMCloseSession(sessionID, NULL);
    }
    err = OAMDeInitialize();

    return 0;
  }
```

[Next](sources-TAboutBoxPane.cp.md)[Previous](sources-PPCGlue.c.md)

