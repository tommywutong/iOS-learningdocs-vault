---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/MacShell_ImagesFromURL_r.html
archived_at: '2026-07-18T03:10:59.864152Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](MacShell-MacShell.c.md)[Previous](MacShell-all.h.md)

# MacShell/ImagesFromURL.r

```c
#include "Types.r"

resource 'DLOG' (1006) {
    {40, 40, 140, 589},
    dBoxProc,
    visible,
    noGoAway,
    0x0,
    1006,
    "",
    alertPositionMainScreen
};

resource 'DITL' (1006) {
    {   /* array DITLarray: 4 elements */
        /* [1] */
        {60, 470, 80, 528},
        Button {
            enabled,
            "OK"
        },
        /* [2] */
        {60, 390, 80, 448},
        Button {
            enabled,
            "Cancel"
        },
        /* [3] */
        {20, 110, 36, 525},
        EditText {
            disabled,
            "http://www.apple.com/quicktime/developers/icefloe/images/writinguin.gif"
        },
        /* [4] */
        {20, 20, 36, 101},
        StaticText {
            disabled,
            "Enter a URL:"
        }
    }
};
```

[Next](MacShell-MacShell.c.md)[Previous](MacShell-all.h.md)

