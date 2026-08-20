---
title: OTCodeResource
apple_id: DTS10000246
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OTCodeResource/Listings/ApplParamsHack_c.html
archived_at: '2026-07-18T03:17:11.307470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTCodeResource](OTCodeResource.md)


[Next](OTGetDefaultEthernetAddress.c.md)[Previous](OTCodeResource.md)

# ApplParamsHack.c

```c
/*
    File:       ApplParamsHack.c

    Contains:   Hack to allocate 32 bytes of application globals in a code resource.

    Written by: Quinn "The Eskimo!"

    Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

    You may incorporate this sample code into your applications without
    restriction, though the sample code has been provided "AS IS" and the
    responsibility for its operation is 100% yours.  However, what you are
    not permitted to do is to redistribute the source as "DSC Sample Code"
    after having made changes. If you're going to re-distribute the source,
    we require that you make it clear in the source that the code was
    descended from Apple Sample Code, but that you've made changes.
*/

#include <Types.h>

// To understand this, you really need to read the accompanying documentation.

extern long ZZZApplParamsHack[8] = {0, 1, 2, 3, 4, 5, 6, 7};
```

[Next](OTGetDefaultEthernetAddress.c.md)[Previous](OTCodeResource.md)

