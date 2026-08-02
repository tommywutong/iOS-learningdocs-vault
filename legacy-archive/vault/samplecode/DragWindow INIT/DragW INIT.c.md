---
title: DragWindow INIT
apple_id: DTS10000185
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DragWindow_INIT/Listings/DragW_INIT_c.html
archived_at: '2026-07-18T03:07:11.635540Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DragWindow INIT](DragWindow%20INIT.md)


[Next](DragW.c.md)[Previous](DragWindow%20INIT.md)

# DragW INIT.c

```c
#include "Types.h"
#include "QuickDraw.h"
#include "Windows.h"
#include "Memory.h"
#include "Resources.h"
// NewDragWindow INIT, Copyright © 1990 Ricardo Batista
// This code gets executed during system startup, its the purpose is to
// load our DragWindow replacement routine so that a window is moved
// along with it's contents as supposed to moving around an outline only.
//
// This code is for MPW C 3.1, should be compiled into an INIT resource.
//
// After compiling copy this resource into a file that includes DragW 'DrgW'
//


#include "OSUtils.h"


void main(void)
{
    Handle H;

    H = GetResource('DrgW',-4033);                      // get our patch resource
    if (H) {
        LoadResource(H);                                // make sure is loaded
        DetachResource(H);                              // not a resource anymore
        HLock(H);                                       // make sure is locked
        HNoPurge(H);                                    // make sure is not purgeable
        NSetTrapAddress((long) *H, 0xA925, ToolTrap);   // replace old trap code
    }
}
```

[Next](DragW.c.md)[Previous](DragWindow%20INIT.md)

