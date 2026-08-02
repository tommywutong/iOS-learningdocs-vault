---
title: FreqForEverChange
apple_id: DTS10000347
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/FreqForEverChange/Listings/FreqForEverChange_r.html
archived_at: '2026-07-18T03:08:58.346668Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FreqForEverChange](FreqForEverChange.md)


[Next](FreqForEverChangePPC.r.md)[Previous](FreqForEverChange.c.md)

# FreqForEverChange.r

```c
#include "Types.r"
include "Sounds.rsrc";

#define AllItems    0b1111111111111111111111111111111   /* 31 flags */
#define MenuItem2   0b00010

resource 'DLOG' (128, "AboutÉ") {
    {66, 102, 224, 400},
    dBoxProc, visible, noGoAway, 0x0, 128, ""
};

resource 'DITL' (128) {
     {
/* 1 */ {130, 205, 150, 284},
        button {
            enabled,
            "Continue"
        };
/* 2 */ {104, 144, 120, 296},               /* SourceLanguage Item */
        staticText {
            disabled,
            ""
        };
/* 3 */ {88, 144, 105, 218},                /* Author Item */
        staticText {
            disabled,
            ""
        };
/* 4 */ {8, 32, 26, 273},
        staticText {
            disabled,
            "Macintosh Programmer's Workshop"
        };
/* 5 */ {32, 103, 50, 202},
        staticText {
            disabled,
            ""
        };
/* 6 */ {88, 16, 104, 144},
        staticText {
            enabled, "Source Language:"
        };
/* 7 */ {104, 16, 120, 144},
        staticText {
            enabled, "Brought to you by:"
        }
    }
};

resource 'MENU' (128, "Apple", preload) {
    128, textMenuProc,
    AllItems & ~MenuItem2,  /* Disable item #2 */
    enabled, apple,
    {
        "AboutÉ",
            noicon, nokey, nomark, plain;
        "-",
            noicon, nokey, nomark, plain
    }
};
```

[Next](FreqForEverChangePPC.r.md)[Previous](FreqForEverChange.c.md)

