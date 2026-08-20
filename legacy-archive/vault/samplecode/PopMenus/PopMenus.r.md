---
title: PopMenus
apple_id: DTS10000195
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PopMenus/Listings/PopMenus_r.html
archived_at: '2026-07-18T03:19:21.663262Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PopMenus](PopMenus.md)


[Next](Document%20Revision%20History.md)[Previous](PopMenus.md)

# PopMenus.r

```c
/*------------------------------------------------------------------------------
#
#   Apple Macintosh Developer Technical Support
#
#   Pop-up Menu Example Application
#
#   PopMenus
#
#   PopMenus.r  -   ResEdit Source
#
#   Copyright © 1988 Apple Computer, Inc.
#   All rights reserved.
#
#   Versions:   1.0                 8/88
#
#   Components: PopMenus.p          August 1, 1988
#               PopMenus.r          August 1, 1988
#               PopMenus.make       August 1, 1988
#
#   This program is a simple example of how to use pop-up menus in your
#   application. It implements a pop-up as a userItem in a modal dialog
#   box (this is a helpful example in its own right!).
#
#   See Sample and TESample for the general structure and MultiFinder 
#   techniques that we recommend that you use when building a new application.
#
------------------------------------------------------------------------------*/
/*
 * Pop-up Menu Example - Resources
 * Bryan Stearns 07Apr87 
 */

#include "Types.r"

/* Our dialog record */
resource 'DLOG' (128) {
    {30, 30, 330, 490}, dBoxProc, invisible, noGoAway, 0, 128, "Pop-up Test"
};

/* Our dialogÕs item list */
resource 'DITL' (128) {
    {   
        /* the ÒOKÓ button */
        {110, 210, 130, 270}, Button { enabled, "OK" },

        /* our pop-upÕs userItem */
        {70, 106, 86, 210}, UserItem { enabled },

        /* the prompt for our userItem */
        /* (the initial space makes it look better hilighted) */
        {70, 20, 86, 105}, StaticText { disabled, " Pick a font:" },    

        /* our button's ÒdefaultÓ roundrect userItem (we move it to */
        /* around the OK button at runtime). It's important that it */
        /* be disabled, so that we can tell it from the pop-up! */
        {0, 0, 0, 0}, UserItem { disabled },

        /* The program name & date */
        {10, 10, 60, 280}, StaticText { disabled,
            "Pop-up Menu Example\nApple Developer Technical Support\n(BJS 07Apr87)" }
    }
};

/* The ÒI need System 4.1 etc.Ó alert */
resource 'ALRT' (129) {
    {50, 50, 180, 370}, 129, {
        OK, visible, sound1;
        OK, visible, sound1;
        OK, visible, sound1;
        OK, visible, sound1
    }
};

/* The item list for our ÒI need System 4.1 etc.Ó alert */
resource 'DITL' (129) {
    {   
        /* the ÒOKÓ button */
        {100, 220, 120, 300}, Button { enabled, "Finder" },

        /* The message */
        {10, 65, 90, 300}, StaticText { disabled,
            "The Pop-up Menu Example requires a Macintosh II, SE, Plus, or "
            "512Ke personal computer, with system software version 4.1 or newer."
        }
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](PopMenus.md)

