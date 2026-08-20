---
title: InputSprocketPPTest
apple_id: DTS10000054
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/InputSprocketPPTest/Listings/ISpLQuitWindow_h.html
archived_at: '2026-07-18T03:12:56.888123Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [InputSprocketPPTest](InputSprocketPPTest.md)


[Next](ISpPPTest.r.md)[Previous](ISpLQuitWindow.cp.md)

# ISpLQuitWindow.h

```c
/*
    File:       ISpLQuitWindow.h

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

         <2>     7/17/98    BWS     add header and change creator for SDK
*/

/*************************************************************************************

File:      ISpLQuitWindow.h

Copyright © 1996, 1997, 1998 Apple Computer, Inc., All Rights Reserved


You may incorporate this sample code into your applications without
restriction, though the sample code has been provided "AS IS" and the
responsibility for its operation is 100% yours.  However, what you are
not permitted to do is to redistribute the source as "DSC Sample Code"
after having made changes. If you're going to re-distribute the source,
we require that you make it clear in the source that the code was
descended from Apple Sample Code, but that you've made changes.

*************************************************************************************/

#include <LWindow.h>

class LQuitWindow : public LWindow
{
public:
    enum {class_ID = 'ISqw'};

    LQuitWindow(LStream *inStream);

    static LQuitWindow *CreateLQuitWindowStream(LStream *inStream);

    void    ClickInGoAway(const EventRecord &inMacEvent);
};
```

[Next](ISpPPTest.r.md)[Previous](ISpLQuitWindow.cp.md)

