---
title: RAMDisk
apple_id: DTS10000430
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RAMDisk/Listings/ShowInitIcon_ShowInitIcon_h.html
archived_at: '2026-07-18T03:21:47.506232Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RAMDisk](RAMDisk.md)


[Next](TradDriverLoaderLib-TradDriverLoaderLib.c.md)[Previous](ShowInitIcon-ShowInitIcon.c.md)

# ShowInitIcon/ShowInitIcon.h

```c
#ifndef __ShowInitIcon__
#define __ShowInitIcon__

#include <Types.h>

// Usage: pass the ID of your icon family (ICN#/icl4/icl8) to have it drawn in the right spot.
// If 'advance' is true, the next INIT icon will be drawn to the right of your icon. If it is false, the next INIT icon will overwrite
// yours. You can use it to create animation effects by calling ShowInitIcon several times with 'advance' set to false.

#ifdef __cplusplus
extern "C" {
#endif

pascal void ShowInitIcon (short iconFamilyID, Boolean advance);

#ifdef __cplusplus
}
#endif

#endif /* __ShowInitIcon__ */
```

[Next](TradDriverLoaderLib-TradDriverLoaderLib.c.md)[Previous](ShowInitIcon-ShowInitIcon.c.md)

