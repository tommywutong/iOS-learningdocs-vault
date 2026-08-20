---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_AboutBox_c.html
archived_at: '2026-07-18T03:12:08.470083Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-AboutBox.h.md)[Previous](Resources-ISpSample.r.md)

# Source/AboutBox.c

```c
/*
    File:       AboutBox.c

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

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#include <Dialogs.h>
#include <TextUtils.h>

#include "AboutBox.h"
#include "AppShellResources.h"

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Functions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AboutBox

void
AboutBox(void)
{
Str255                  title, copyright;
SInt16                  itemHit;
AlertStdAlertParamRec   pb;

    GetIndString(title, kSTRn_AboutBoxStrings, 1);
    GetIndString(copyright, kSTRn_AboutBoxStrings, 2);

    pb.movable = false;
    pb.helpButton = false;
    pb.filterProc = nil;
    pb.defaultText = (StringPtr) kAlertDefaultOKText;
    pb.cancelText = nil;
    pb.otherText = nil;
    pb.defaultButton = kStdOkItemIndex;
    pb.cancelButton = kStdCancelItemIndex;
    pb.position = kWindowAlertPositionParentWindowScreen;

    StandardAlert(kAlertPlainAlert, title, copyright, &pb, &itemHit);
}
```

[Next](Source-AboutBox.h.md)[Previous](Resources-ISpSample.r.md)

