---
title: PCCardNetworkSample
apple_id: DTS10000258
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PCCardNetworkSample/Listings/EnablerSample_h.html
archived_at: '2026-07-18T03:18:20.662426Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PCCardNetworkSample](PCCardNetworkSample.md)


[Next](EnablerSmpl.c.md)[Previous](dlpiuser.h.md)

# EnablerSample.h

```c
/*
    File:       EnablerSample.h

    Contains:   

    Written by: Rich Kubota 

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

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
#include "ProjectDefines.h"
#include <NameRegistry.h>

#ifdef __cplusplus
extern "C" {
#endif

    typedef void (*PortOfflineProcPtr)(const RegEntryID *cardRef);

#ifdef __cplusplus
}
#endif
```

[Next](EnablerSmpl.c.md)[Previous](dlpiuser.h.md)

