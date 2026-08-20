---
title: Easy Video Grabber
apple_id: DTS10000320
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Easy_Video_Grabber/Listings/EasyGrabberTest_c.html
archived_at: '2026-07-18T03:07:32.631439Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Easy Video Grabber](Easy%20Video%20Grabber.md)


[Next](Document%20Revision%20History.md)[Previous](BigEasyVideoGrabber.h.md)

# EasyGrabberTest.c

```c
/*
  File:         EasyGrabberTest.c
  Contains:     Test Application for the Video Grabber Functions.
  Written by:   David Van Brink / QT Engineering
  Copyright:    © 1991-1994 by Apple Computer, Inc., all rights reserved.
  Change History (most recent first):
  <2>       12/4/94     khs     changed the format of the file to the new look and feel
  <1>       12/18/91    dvb     1.0 Started
  To Do:
*/


// INCLUDES
#include <QuickDraw.h>
#include <Events.h>
#include <Menus.h>
#include <ToolUtils.h>
#include <Menus.h>
#include <Windows.h>
#include <Memory.h>
#include <Fonts.h>
#include <OSEvents.h>

#include <Movies.h>

#include "BigEasyVideoGrabber.h"

// FUNCTION PROTOTYPES
static void InitToolbox(void);
static void DigitizeInAWindow(void);


// FUNCTIONS
void InitToolbox(void)
{
    InitGraf(&qd.thePort);
    InitFonts();
    FlushEvents(0xffff, 0);
    InitWindows();
    InitMenus();
    InitCursor();

    EnterMovies();
}


void DigitizeInAWindow(void)
{
    WindowPtr w;
    Rect r;
    short i;
    Boolean gotAFrame;

    SetRect(&r, 100, 100, 260, 220);            /* 160 x 120 window */

    w = NewCWindow(0, &r, "\pFive Clicks", true, noGrowDocProc, (WindowPtr) - 1, 0, 0);

    SetPort(w);

    /*
     * Set the rectangle we'll be drawing into.
     */
    SetRect(&r, 0, 0, 160, 120);

    /*
     * Let the user click five times
     * and grab a frame each time.
     *
     * This is a substandard user interface,
     * I am sure you will agree.
     */
    for (i = 0; i < 5; i++)
    {
        /*
         * Wait For A MouseClick
         */
        while (!Button())
            ;
        while (Button())
            ;

        /*
         * Grab a frame, allocate and deallocate on the fly.
         */
        gotAFrame = GrabEasyVideoGrabber(nil, &r);

        /*
         * If we didn't get a frame, just quit and go home.
         */
        if (!gotAFrame)
            return;
    }
}


// MAIN
void main(void)
{
    InitToolbox();
    DigitizeInAWindow();
    FlushEvents(0xffff, 0);
}
```

[Next](Document%20Revision%20History.md)[Previous](BigEasyVideoGrabber.h.md)

