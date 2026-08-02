---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Source_WRay_Error_c.html
archived_at: '2026-07-18T03:28:25.851160Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Source-WRayEvents.c.md)[Previous](Source-WRayDocument.c.md)

# Source/WRay_Error.c

```c
/* 
 *  WRay_Error.c
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

/*------------------*/
/*  Include Files   */
/*------------------*/
#include "QD3D.h"

#if defined(OS_MACINTOSH) && OS_MACINTOSH
#include <Dialogs.h>
#include <Strings.h>
#include <TextUtils.h>
#endif

#include "WRay_Main.h"  /* kStringRsrcID */
#include "WRay_Error.h"


/*------------------*/
/*    Constants     */
/*------------------*/
#define kErrorAlertRsrcID   129


/*----------------------*/
/*  Local Prototypes    */
/*----------------------*/


/*
 *  QuickDraw3D_Exit
 *
 *  Displays C string in an alert box.
 */
void Error_Alert(
    short       iconType,
    char        *pMessage)
{
    GrafPtr     oldPort;
    short       itemHit;

    if (pMessage == NULL)
        return;

    /* Convert C string to Pascal */
    c2pstr (pMessage);
    ParamText ((ConstStr255Param) pMessage, NULL, NULL, NULL);

    GetPort (&oldPort);

    if (iconType == kStopIcon)
        itemHit = StopAlert (kErrorAlertRsrcID, NULL);
    else
        itemHit = NoteAlert (kErrorAlertRsrcID, NULL);

    SetPort (oldPort);

    /* Restore C string */
    p2cstr ((StringPtr) pMessage);
}


/*
 *  QuickDraw3D_Exit
 */
Boolean Error_ShowMessage(
    short       resStringIndex)
{
    Str255  notice;

    GetIndString (notice, kStringRsrcID, resStringIndex);
    if (notice[0] > 0)
    {
        p2cstr (notice);
        Error_Alert(kNoteIcon, (char *) notice);
        return true;
    }

    return false;
}
```

[Next](Source-WRayEvents.c.md)[Previous](Source-WRayDocument.c.md)

