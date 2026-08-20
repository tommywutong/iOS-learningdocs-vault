---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_PresinfoWindow_r.html
archived_at: '2026-07-26T19:53:08.603415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-QTSSampleCodeUtils.c.md)[Previous](sources-PresInfoWindow.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/PresinfoWindow.r

```c
/*
    File:       PresinfoWindow.r

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#define forRez          1

#include "ConditionalMacros.r"
#include "Dialogs.r"
#include "Types.r"

#include "PresInfoWindow.h"

/* =====================   Usher Info Window   ========================================== */

resource 'STR#' (rStringList_PresInfoWindow, purgeable) {
    {
        " Info",
        "Info",
    }
};

resource 'DLOG' (rDLOG_PresInfoWindow, purgeable) {
    {50, 50, 350, 350},
    zoomDocProc,
    invisible,
    noGoAway,
    0x0,
    rDITL_PresInfoWindow,
    "",
    centerMainScreen
};

resource 'DITL' (rDITL_PresInfoWindow, purgeable) {
    {   /* array DITLarray: 3 elements */
        /* [1] */
        {8, 8, 30, 102},
        UserItem {
            enabled
        },
        /* [2] */
        {10, 119, 30, 242},
        UserItem {
            enabled
        },
        /* [3] */
        {40, 0, 286, 286},
        UserItem {
            enabled
        }
    }
};
```

[Next](sources-QTSSampleCodeUtils.c.md)[Previous](sources-PresInfoWindow.h.md)

