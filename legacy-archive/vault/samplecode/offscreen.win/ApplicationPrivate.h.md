---
title: offscreen.win
apple_id: DTS10000772
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/offscreen.win/Listings/ApplicationPrivate_h.html
archived_at: '2026-07-18T03:29:53.466153Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [offscreen.win](offscreen.win.md)


[Next](QTCode.c.md)[Previous](Application.h.md)

# ApplicationPrivate.h

```
/*
    File:       ApplicationPrivate.h

    Contains:   QuickTime 3.0 Offscreen sample application.

    Written by: Scott Kuechle

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      4/24/98     srk     first file


 NOTES:


 TO DO:

*/

    /* private data held in each child movie window */
typedef struct
{
    Movie           movie;              /* movie associated with the window */
    short           refNum;             /* movie reference number */
    TimeValue       currentTime;        /* current time value for movie display */
    LPRGBQUAD       srcRgbQuadArray;    /* rbg color values for our window background bitmap */
    HPALETTE        hBackgroundPalette; /* color palette for our window background */
    HBITMAP         hBitmap;            /* the DIB (from CreateDIBSection) for use with our memory device context */
    HANDLE          hBkgrndBitmap;      /* bitmap used to paint on the background of our windows */
    HANDLE          ghInst;
    HDC             hMemDC;             /* memory device context we use for drawing our bitmap/offscreen images */
    GWorldPtr       offscreenGWorld;    /* our Mac offscreen */
    LONG            maxWindowWidth;
    LONG            maxWindowHeight;
} ChildWindowRecord, *ChildWindowPtr;
```

[Next](QTCode.c.md)[Previous](Application.h.md)

