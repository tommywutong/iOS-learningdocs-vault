---
title: Scriptable Print SimpleText
apple_id: DTS10000305
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/Scriptable_Print_SimpleText/Listings/ThreeDMetafile_r.html
archived_at: '2026-07-18T03:23:33.122562Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Scriptable Print SimpleText](Scriptable%20Print%20SimpleText.md)


[Next](Document%20Revision%20History.md)[Previous](ThreeDMetafile.h.md)

# ThreeDMetafile.r

```c
/*
    File:       ThreeDMetafile.r

    Contains:   resources for 3d files

** Copyright 1995-1996 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DSC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.

*/

#include "Types.r"
#include "SysTypes.r"
#include "ThreeDMetafile.h"

resource 'WIND' (kThreeDWindowID) {
    {50, 50, 300, 400},
    noGrowDocProc,
    visible,
    goAway,
    0x0,
    "QuickDraw 3D",
    noAutoCenter
};
```

[Next](Document%20Revision%20History.md)[Previous](ThreeDMetafile.h.md)

