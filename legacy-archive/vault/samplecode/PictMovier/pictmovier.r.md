---
title: PictMovier
apple_id: DTS10000332
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PictMovier/Listings/pictmovier_r.html
archived_at: '2026-07-18T03:19:00.826323Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PictMovier](PictMovier.md)


[Next](Document%20Revision%20History.md)[Previous](pictmovier.c.md)

# pictmovier.r

```c
#include    "Types.r"

include "StdCompression.rsrc";


resource 'MENU' (128) {
    128,
    textMenuProc,
    0x7FFFFFFD,
    enabled,
    apple,
    {   /* array: 2 elements */
        /* [1] */
        "About PictMovierÉ", noIcon, noKey, noMark, plain,
        /* [2] */
        "-", noIcon, noKey, noMark, plain
    }
};

resource 'MENU' (130) {
    130,
    textMenuProc,
    0x7FFFFFBD,
    enabled,
    "Edit",
    {   /* array: 6 elements */
        /* [1] */
        "Undo", noIcon, "Z", noMark, plain,
        /* [2] */
        "-", noIcon, noKey, noMark, plain,
        /* [3] */
        "Cut", noIcon, "X", noMark, plain,
        /* [4] */
        "Copy", noIcon, "C", noMark, plain,
        /* [5] */
        "Paste", noIcon, "V", noMark, plain,
        /* [6] */
        "Clear", noIcon, noKey, noMark, plain
    }
};

resource 'MENU' (129) {
    129,
    textMenuProc,
    0x7FFFFFF7,
    enabled,
    "File",
    {   /* array: 5 elements */
        /* [1] */
        "OpenÉ", noIcon, "O", noMark, plain,
        /* [2] */
        "Close", noIcon, "W", noMark, plain,
        /* [3] */
        "SaveÉ", noIcon, "S", noMark, plain,
        /* [4] */
        "-", noIcon, noKey, noMark, plain,
        /* [5] */
        "Quit", noIcon, "Q", noMark, plain
    }
};

resource 'MENU' (131) {
    131,
    textMenuProc,
    0x7FFFFFAF,
    enabled,
    "PictMovier",
    {   /* array: 8 elements */
        /* [1] */
        "CompressionÉ", noIcon, "K", noMark, plain,
        /* [2] */
        "Number of StagesÉ", noIcon, noKey, noMark, plain,
        /* [3] */
        "Oversample 2X", noIcon, "2", check, plain,
        /* [4] */
        "Backwards", noIcon, "B", noMark, plain,
        /* [5] */
        "-", noIcon, noKey, noMark, plain,
        /* [6] */
        "Preview StageÉ", noIcon, noKey, noMark, plain,
        /* [7] */
        "-", noIcon, noKey, noMark, plain,
        /* [8] */
        "Do TransformÉ", noIcon, "M", noMark, plain
    }
};

resource 'DLOG' (128) {
    {40, 40, 186, 326},
    dBoxProc,
    visible,
    goAway,
    0x0,
    128,
    ""
};

resource 'DLOG' (129) {
    {40, 40, 186, 326},
    dBoxProc,
    visible,
    goAway,
    0x0,
    129,
    ""
};

resource 'DITL' (128) {
    {   /* array DITLarray: 5 elements */
        /* [1] */
        {116, 210, 136, 268},
        Button {
            enabled,
            "OK"
        },
        /* [2] */
        {85, 210, 105, 268},
        Button {
            enabled,
            "Cancel"
        },
        /* [3] */
        {29, 194, 45, 269},
        EditText {
            enabled,
            ""
        },
        /* [4] */
        {68, 23, 86, 94},
        CheckBox {
            enabled,
            "Linear"
        },
        /* [5] */
        {16, 21, 56, 171},
        StaticText {
            disabled,
            "Number of Stages of Metamorphis :"
        }
    }
};

resource 'DITL' (129) {
    {   /* array DITLarray: 4 elements */
        /* [1] */
        {114, 210, 134, 268},
        Button {
            enabled,
            "OK"
        },
        /* [2] */
        {84, 210, 104, 268},
        Button {
            enabled,
            "Cancel"
        },
        /* [3] */
        {8, 9, 45, 167},
        StaticText {
            disabled,
            "Choose Metamorphis stage to preview :"
        },
        /* [4] */
        {27, 191, 43, 266},
        EditText {
            enabled,
            ""
        }
    }
};

resource 'DITL' (140) {
    {   /* array DITLarray: 2 elements */
        /* [1] */
        {222, 276, 242, 334},
        Button {
            enabled,
            "Oh"
        },
        /* [2] */
        {7, 63, 213, 357},
        StaticText {
            disabled,
            "^0^1^2^3"
        }
    }
};

resource 'SIZE' (0) {
    reserved,
    ignoreSuspendResumeEvents,
    reserved,
    cannotBackground,
    notMultiFinderAware,
    backgroundAndForeground,
    dontGetFrontClicks,
    ignoreChildDiedEvents,
    is32BitCompatible,
    notHighLevelEventAware,
    onlyLocalHLEvents,
    notStationeryAware,
    dontUseTextEditServices,
    reserved,
    reserved,
    reserved,
    2000000,
    500000
};

resource 'ALRT' (140) {
    {39, 41, 294, 409},
    140,
    {   /* array: 4 elements */
        /* [1] */
        OK, visible, sound1,
        /* [2] */
        OK, visible, sound1,
        /* [3] */
        OK, visible, sound1,
        /* [4] */
        OK, visible, sound1
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](pictmovier.c.md)

