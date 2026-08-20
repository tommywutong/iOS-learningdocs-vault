---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_PresInfoWindow_h.html
archived_at: '2026-07-26T19:53:08.597570Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-PresinfoWindow.r.md)[Previous](sources-PresInfoWindow.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/PresInfoWindow.h

```
/*
    File:       PresInfoWindow.h

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __PRESINFOWINDOW__
#define __PRESINFOWINDOW__

#ifndef forRez

// ---------------------------------------------------------------------------
//      D E F I N I T I O N S
// ---------------------------------------------------------------------------

#define kSignature_PresInfoWind     FOUR_CHAR_CODE('pinf')

#define kCommand_GetPresInfo            3000

// ---------------------------------------------------------------------------
//      P R O T O T Y P E S
// ---------------------------------------------------------------------------

OSErr PresInfoWind_New(WindowPtr *outWindow);
void PresInfoWind_Close(WindowPtr inWindow);

void PresInfoWind_Idle(WindowPtr inWindow);

void PresInfoWind_GrowWindow(WindowPtr inWindow, EventRecord *inEvent);
void PresInfoWind_DoContentClick(WindowPtr inWindow, EventRecord *inEvent);
void PresInfoWind_ActivateWindow(WindowPtr inWindow, Boolean inBecomingActive);
void PresInfoWind_Draw(WindowPtr inWindow);

long PresInfoWind_GetMenuCommand(WindowPtr inWindow, long inMenuResult, void **outCommandParams);
OSErr PresInfoWind_DoCommand(WindowPtr inWindow, long inCommand, void *inCommandParams);

OSErr PresInfoWind_HandleMessage(WindowPtr inWindow, long inMessage, void *inMessageParams);

#endif  /* forRez */

// ---------------------------------------------------------------------------
//      R E Z  D E F I N I T I O N S        (also used by .r file)
// ---------------------------------------------------------------------------

#define kRezIDBase_PresInfoWindow       5100

#define rStringList_PresInfoWindow      kRezIDBase_PresInfoWindow
    #define rPresInfoWindString_TitleTemplate       1
    #define kPresInfoWindString_DefaultName         2

#define rDLOG_PresInfoWindow            kRezIDBase_PresInfoWindow
#define rDITL_PresInfoWindow            kRezIDBase_PresInfoWindow
    #define rPresInfoWindDITLItem_UpdateButton      1
    #define rPresInfoWindDITLItem_ShowAllCheckBox   2
    #define rPresInfoWindDITLItem_InfoArea          3

#endif /* __PRESINFOWINDOW__ */
```

[Next](sources-PresinfoWindow.r.md)[Previous](sources-PresInfoWindow.c.md)

