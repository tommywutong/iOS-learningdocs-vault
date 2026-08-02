---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/MacShell_MacShell_r.html
archived_at: '2026-07-18T03:11:00.057442Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](MacShell-NavFile.c.md)[Previous](MacShell-MacShell.h.md)

# MacShell/MacShell.r

```c
#include "Types.r"

resource 'MENU' (128) {
    128,
    textMenuProc,
    0x7FFFFFFD,
    enabled,
    apple,
    {
        "About This DemoÉ", noIcon, noKey, noMark, plain,
        "-", noIcon, noKey, noMark, plain
    }
};

resource 'MENU' (129) {
    129,
    textMenuProc,
    allEnabled,
    enabled,
    "File",
    {
        "Quit", noIcon, "Q", noMark, plain
    }
};

resource 'MBAR' (128) {
    {
        128,
        129
    }
};

resource 'ALRT' (128) {
    {40, 40, 217, 322},
    128,
    {
        OK, visible, silent,
        OK, visible, silent,
        OK, visible, silent,
        OK, visible, silent
    },
    alertPositionMainScreen
};

resource 'DITL' (128) {
    {
        {145, 112, 165, 170},
        Button {
            enabled,
            "OK"
        },
        {9, 9, 133, 273},
        Picture {
            disabled,
            128
        }
    }
};

resource 'PICT' (128) {
    /* ... */
};
```

[Next](MacShell-NavFile.c.md)[Previous](MacShell-MacShell.h.md)

