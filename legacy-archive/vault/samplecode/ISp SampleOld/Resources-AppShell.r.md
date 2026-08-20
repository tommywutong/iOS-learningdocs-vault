---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Resources_AppShell_r.html
archived_at: '2026-07-18T03:12:08.270011Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Resources-ISpSample.r.md)[Previous](ISp%20SampleOld.md)

# Resources/AppShell.r

```c
/*
    File:       AppShell.r

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#Include "Controls.r"
#include "MacTypes.r"
#Include "Menus.r"

#Include "::Source:AppShellResources.h"
Include ":AppShell.rsrc";

resource 'MBAR' (kMBAR_Main)
{
    {
        kMENU_Apple,
        kMENU_File,
        kMENU_Edit
    }
};

resource 'MENU' (kMENU_Apple, "About Menu")
{
    kMENU_Apple,
    kMenuStdMenuProc,
    0xFFFFFFFD,
    enabled,
    apple,

    {
        "About ISp_SampleÉ",        noIcon,     noKey,      noMark,     plain;
        "-",                        noIcon,     noKey,      noMark,     plain;
    }
};

resource 'MENU' (kMENU_File, "File Menu")
{
    kMENU_File,
    kMenuStdMenuProc,
    0xFFFFFFFF,
    enabled,
    "File",

    {
        "Start Game",       noIcon,     "N",        noMark,     plain;
        "Configure Input",  noIcon,     "K",        noMark,     plain;
        "-",                noIcon,     noKey,      noMark,     plain;
        "Quit",             noIcon,     "Q",        noMark,     plain;
    }
};

resource 'MENU' (kMENU_Edit, "Edit Menu")
{
    kMENU_Edit,
    kMenuStdMenuProc,
    0xFFFFFFFD,
    enabled,
    "Edit",

    {
        "Undo",     noIcon,     "Z",        noMark,     plain;
        "-",        noIcon,     noKey,      noMark,     plain;
        "Cut",      noIcon,     "X",        noMark,     plain;
        "Copy",     noIcon,     "C",        noMark,     plain;
        "Paste",    noIcon,     "V",        noMark,     plain;
        "Clear",    noIcon,     noKey,      noMark,     plain;
    }
};

resource 'xmnu' (kMENU_Apple, "Apple Menu")
{
    versionZero
    {
        {
            dataItem {  kMenuCMD_AboutBox,  kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
        }
    }
};

resource 'xmnu' (kMENU_File, "File Menu")
{
    versionZero
    {
        {
            dataItem {  kMenuCMD_StartGame,         kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            dataItem {  kMenuCMD_ConfigureInput,    kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            skipItem {                                                                                                      },
            dataItem {  kMenuCMD_Quit,              kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    }
        }
    }
};

resource 'xmnu' (kMENU_Edit, "Edit Menu")
{
    versionZero
    {
        {
            dataItem {  kMenuCMD_Undo,      kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            skipItem {                                                                                                      },
            dataItem {  kMenuCMD_Cut,       kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            dataItem {  kMenuCMD_Copy,      kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            dataItem {  kMenuCMD_Paste,     kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    },
            dataItem {  kMenuCMD_Clear,     kMenuNoModifiers,   currScript, 0,  0,  noHierID,   sysFont,    naturalGlyph    }
        }
    }
};

resource 'STR#' (kSTRn_AboutBoxStrings, "About Box Strings")
{
    {
        "InputSprocket Sample Application";

        "by Brent Schorsch\n"
        "\n"
        "special thanks to Chris DeSalvo\n"
        "©1998"
    }
};
```

[Next](Resources-ISpSample.r.md)[Previous](ISp%20SampleOld.md)

