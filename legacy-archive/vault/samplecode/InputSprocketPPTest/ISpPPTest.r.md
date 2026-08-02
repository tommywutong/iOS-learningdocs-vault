---
title: InputSprocketPPTest
apple_id: DTS10000054
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/InputSprocketPPTest/Listings/ISpPPTest_r.html
archived_at: '2026-07-18T03:12:57.049723Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [InputSprocketPPTest](InputSprocketPPTest.md)


[Next](ISpPPTestTools.cp.md)[Previous](ISpLQuitWindow.h.md)

# ISpPPTest.r

```c
/*
    File:       ISpPPTest.r

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

         <1>     7/17/98    BWS     first checked in
*/

/*************************************************************************************

File:      ISpPPTest.r

Copyright © 1996, 1997, 1998 Apple Computer, Inc., All Rights Reserved


You may incorporate this sample code into your applications without
restriction, though the sample code has been provided "AS IS" and the
responsibility for its operation is 100% yours.  However, what you are
not permitted to do is to redistribute the source as "DSC Sample Code"
after having made changes. If you're going to re-distribute the source,
we require that you make it clear in the source that the code was
descended from Apple Sample Code, but that you've made changes.

*************************************************************************************/

#include "InputSprocket.r"

/* the InputSprocket application resource tells utility programs how the */
/* application uses InputSprocket */

#define kResourceID_isap                        128
#define kResourceID_setl                        128

resource 'isap' (kResourceID_isap)
{
    callsISpInit,
    usesInputSprocket
};

/* the set list resource contains the list of all the saved sets for devices */
/* that are provided in the application's resource fork */

resource 'setl' (kResourceID_setl, "ISpTest (PowerPlant) sets")
{
    currentVersion,
    {
    };
};
```

[Next](ISpPPTestTools.cp.md)[Previous](ISpLQuitWindow.h.md)

