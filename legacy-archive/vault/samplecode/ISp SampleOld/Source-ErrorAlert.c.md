---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_ErrorAlert_c.html
archived_at: '2026-07-18T03:12:08.901924Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-ErrorAlert.h.md)[Previous](Source-CModalDialog.h.md)

# Source/ErrorAlert.c

```c
/*
    File:       ErrorAlert.c

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
#include <Processes.h>
#include <NumberFormatting.h>
#include <TextUtils.h>

#include "ErrorAlert.h"
#include "AppShellResources.h"


//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Variables

unsigned char gFatalErrOccuredStr[] = "\pA fatal error has occured (";
unsigned char gErrOccuredStr[] = "\pAn error has occured (";
unsigned char gEndParenStr[] = "\p)";

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Functions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AboutBox

void
ErrorAlert(StringPtr errorStr, OSStatus errNum, Boolean shouldQuit)
{
Str255                  titleStr;
Str31                   errorNumAsStr;
SInt32                  length = 0;
SInt16                  itemHit;
AlertStdAlertParamRec   pb;

    //¥Êset up the error string with the error number
    NumToString (errNum, errorNumAsStr);

    if (shouldQuit)
    {
        BlockMoveData (&gFatalErrOccuredStr[1], &titleStr[1], gFatalErrOccuredStr[0]);
        length = gFatalErrOccuredStr[0];
    }
    else
    {
        BlockMoveData (&gErrOccuredStr[1], &titleStr[1], gErrOccuredStr[0]);
        length = gErrOccuredStr[0];
    }

    BlockMoveData (&errorNumAsStr[1], &titleStr[1+length], errorNumAsStr[0]);
    length += errorNumAsStr[0];

    BlockMoveData (&gEndParenStr[1], &titleStr[1+length], gEndParenStr[0]);
    length += gEndParenStr[0];

    titleStr[0] = length;

    //¥Êset up the pb for StandardAlert
    pb.movable = false;
    pb.helpButton = false;
    pb.filterProc = nil;
    pb.defaultText = (StringPtr) kAlertDefaultOKText;
    pb.cancelText = nil;
    pb.otherText = nil;
    pb.defaultButton = kStdOkItemIndex;
    pb.cancelButton = kStdCancelItemIndex;
    pb.position = kWindowAlertPositionParentWindowScreen;

    StandardAlert(kAlertStopAlert, titleStr, errorStr, &pb, &itemHit);

    if (shouldQuit)
        ExitToShell();
}
```

[Next](Source-ErrorAlert.h.md)[Previous](Source-CModalDialog.h.md)

