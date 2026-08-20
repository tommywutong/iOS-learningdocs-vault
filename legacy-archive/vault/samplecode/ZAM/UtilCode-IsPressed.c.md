---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/UtilCode_IsPressed_c.html
archived_at: '2026-07-18T03:28:34.944953Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](UtilCode-WindowUtil.c.md)[Previous](UtilCode-GWorldUtils.h.md)

# UtilCode/IsPressed.c

```c

#include "IsPressed.proto.h"
Boolean IsPressed(unsigned short k, unsigned char km[16])
/*
    Checks if a given key is down by key Code
*/
{
    return ((km[k>>3] >> (k & 7)) & 1);
}
```

[Next](UtilCode-WindowUtil.c.md)[Previous](UtilCode-GWorldUtils.h.md)

