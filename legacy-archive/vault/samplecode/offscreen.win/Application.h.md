---
title: offscreen.win
apple_id: DTS10000772
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/offscreen.win/Listings/Application_h.html
archived_at: '2026-07-18T03:29:53.992276Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [offscreen.win](offscreen.win.md)


[Next](ApplicationPrivate.h.md)[Previous](Application.c.md)

# Application.h

```c
/*
    File:       Application.h

    Contains:   QuickTime 3.0 Offscreen sample application.

    Written by: Scott Kuechle
                based on MDIPlayer code by Brian S. Friedkin

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      4/24/98     srk     first file


 NOTES:


 TO DO:

*/

#pragma once

// Macintosh headers
#include "MacTypes.h"
#include "QTML.h"
#include "Movies.h"
#include "Scrap.h"
#include "FixMath.h"
#include "NumberFormatting.h"
#include "TextUtils.h"
#include "Resources.h"
#include "quickdraw.h"
#include "files.h"
#include "PictUtils.h"

#include <string.h>

// Windows headers
#define STRICT
#include <windows.h>
#include "resource.h"

// Program headers
#include "ApplicationPrivate.h"


#define RECT_WIDTH(r)   (r.right-r.left)
#define RECT_HEIGHT(r)  (r.bottom-r.top)

#define kWinSpacer  200

void        DrawBackgroundBitmap(HDC hDC, HWND hwnd, HANDLE hBitmap, RECT *updateRect);
void        DrawHelpMessage(HDC hDC, HWND hwnd);
WORD        GetDCBitDepth(HDC hDC);
HPALETTE    UseCustomPalette(HDC hDC, HPALETTE  newPalette);
void        DoDrawFrameInfo(HDC hMemDC, HWND hwnd, Rect *movieBounds, TimeValue theTime);
HBITMAP     DoCreateDIBSection(HDC dc, LPRGBQUAD srcRgbQuadArray,WORD depth,LONG width,LONG height);
HDC         DoCreateMemoryDC(HWND   hwnd);
void        CenterMovieRectInWindow(HWND hwnd, int movWidth, int movHeight, Rect *centeredRect);
```

[Next](ApplicationPrivate.h.md)[Previous](Application.c.md)

