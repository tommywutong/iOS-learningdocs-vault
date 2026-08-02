---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSWindow_h.html
archived_at: '2026-07-18T03:14:43.656385Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-Offscreen.c.md)[Previous](Sources-MSWindow.c.md)

# Sources/MSWindow.h

```c
// MSWindow.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.


#ifndef __MSWINDOW__
#define __MSWINDOW__

#include <Memory.h>
#include <Types.h>
#include <Quickdraw.h>
#include <Fonts.h>
#include <ToolUtils.h>
#include <Traps.h>
#include "MSGlobals.h"
#include "MSUtils.h"
#include "MSAppleEvents.h"

DPtr        DPtrFromWindowPtr(WindowPtr theWindow);

void        MyGrowWindow( WindowPtr w, Point p );

void        GetPageEnds( short pageHeight, TEHandle theText,
                                PageEndsArray  pageBounds, short *nPages);

void        DoZoom( WindowPtr w, short c, Point p );

void        DoContent( WindowPtr theWindow, EventRecord theEvent );

OSErr       DoActivate(WindowPtr theWindow, Boolean activate);

void        DoUpdate( WindowPtr theWindow );

DPtr        NewDocument(Boolean isForOldDoc, WindowPtr behindWindow);

void        CloseMyWindow(WindowPtr aWindow);

void        ShowSelect( DPtr theDoc );

void        AdjustScrollbars( DPtr theDoc, Boolean needsResize );

void        GetWinContentRect( WindowPtr theWindow, Rect *r );

void        ResizeWindow( DPtr theDoc );

void        ResizePageSetupForDocument( DPtr theDoc );

void        InvalidateDocument( DPtr theDoc );

void        DrawPageExtras(DPtr theDoc);

void        PrintWindow( DPtr theDoc, Boolean askUser );

pascal void VActionProc(ControlHandle control, short part);

pascal void HActionProc(ControlHandle control, short part);

void        AdjustTE( DPtr theDoc );
void        AdjustHV( Boolean isVert, ControlHandle control, DPtr theDoc, Boolean canRedraw );
void        AdjustScrollValues( DPtr theDoc, Boolean canRedraw );
void        GetTERect( WindowPtr window, Rect *teRect );
void        AdjustScrollSizes( DPtr theDoc );
void        CommonAction( ControlHandle control, short *amount );
void        OffsetWindow(WindowPtr aWindow);
// void     GetLocalUpdateRgn( WindowPtr window, RgnHandle localRgn );
void        DoBackgroundContent ( WindowPtr theWindow, EventRecord theEvent);
void        DrawPageBreaks(DPtr theDoc);

void        ShowMSWindow( WindowPtr theWindow );
void        HideMSWindow( WindowPtr theWindow );

#endif
```

[Next](Sources-Offscreen.c.md)[Previous](Sources-MSWindow.c.md)

