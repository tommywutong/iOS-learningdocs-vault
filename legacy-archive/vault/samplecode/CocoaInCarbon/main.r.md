---
title: CocoaInCarbon
apple_id: DTS10000385
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaInCarbon/Listings/main_r.html
archived_at: '2026-07-18T03:03:41.586048Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaInCarbon](CocoaInCarbon.md)


[Next](Document%20Revision%20History.md)[Previous](CocoaStuff-Controller.m.md)

# main.r

```c
/* main.r */

#include <Carbon/Carbon.r>
#include "main.h"

resource 'MBAR' (rMenuBar, preload) {
        {       /* array MenuArray: 3 elements */
                /* [1] */
                128,
                /* [2] */
                129,
                /* [3] */
                130
        }
};

resource 'MENU' (mApple, preload) {
        128,
        textMenuProc,
        0x7FFFFFFD,
        enabled,
        apple,
        {       /* array: 2 elements */
                /* [1] */
                "About HelloÉ", noIcon, noKey, noMark, plain,
                /* [2] */
                "-", noIcon, noKey, noMark, plain
        }
};

resource 'MENU' (mFile, preload) {
        129,
        textMenuProc,
        0x1400,
        enabled,
        "File",
        {       /* array: 11 elements */
                /* [1] */
                "New", noIcon, "N", noMark, plain,
                /* [2] */
                "Open", noIcon, "O", noMark, plain,
                /* [3] */
                "-", noIcon, noKey, noMark, plain,
                /* [4] */
                "Close", noIcon, "W", noMark, plain,
                /* [5] */
                "Save", noIcon, "S", noMark, plain,
                /* [6] */
                "Save AsÉ", noIcon, noKey, noMark, plain,
                /* [7] */
                "-", noIcon, noKey, noMark, plain,
                /* [8] */
                "Page SetupÉ", noIcon, noKey, noMark, plain,
                /* [9] */
                "PrintÉ", noIcon, noKey, noMark, plain,
                /* [10] */
                "-", noIcon, noKey, noMark, plain,
                /* [11] */
                "Quit", noIcon, "Q", noMark, plain
        }
};

resource 'MENU' (mEdit, preload) {
        130,
        textMenuProc,
        0x0,
        enabled,
        "Edit",
        {       /* array: 6 elements */
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

resource 'DITL' (kAboutBox) {
        {       /* array DITLarray: 3 elements */
                /* [1] */
                {16, 21, 38, 208},
                StaticText {
                        disabled,
                        "Hello hello hello..."
                },
                /* [2] */
                {116, 287, 136, 345},
                Button {
                        enabled,
                        "OK"
                },
                /* [3] */
                {54, 139, 74, 197},
                Button {
                        enabled,
                        "OK"
                }
        }
};

resource 'ALRT' (kAboutBox) {
        {40, 40, 139, 280},
        200,
        {       /* array: 4 elements */
                /* [1] */
                OK, visible, sound1,
                /* [2] */
                OK, visible, sound1,
                /* [3] */
                OK, visible, sound1,
                /* [4] */
                OK, visible, sound1
        },
    noAutoCenter
};
```

[Next](Document%20Revision%20History.md)[Previous](CocoaStuff-Controller.m.md)

