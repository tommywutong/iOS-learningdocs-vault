---
title: BusErrorTest
apple_id: DTS10000008
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BusErrorTest/Listings/BusErrTest4Init_c.html
archived_at: '2026-07-18T03:02:20.557257Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BusErrorTest](BusErrorTest.md)


[Next](BusErrTestInit.a.md)[Previous](BusErrTest.c.md)

# BusErrTest4Init.c

```c
/*******************************************************************************

    BusErrTest by Cameron

*******************************************************************************/

#include <String.h>

/* Type 1 includes */
#include <Types.h>
#include <QuickDraw.h>

/* Type 2 includes */
#include <Controls.h>
#include <Events.h>
#include <Fonts.h>
#include <Memory.h>
#include <Menus.h>
#include <OSUtils.h>
#include <Resources.h>
#include <SegLoad.h>
#include <TextEdit.h>
#include <ToolUtils.h>
#include <Traps.h>

/* Type 3 includes */
#include <Desk.h>
#include <Files.h>
#include <OSEvents.h>
#include <Windows.h>

/* Type 4 includes */
#include <Dialogs.h>

/*  Global Variables  */

Str255          WindTitle;
WindowPtr       MyWindow,aWindPtr;
short           err,itemHit;
EventRecord     MyEvent;
Boolean         quit,DrawOn,IsBtn;
Rect            WindRect,Rect1,Rect2;
Point           aPoint;
CursHandle      myCrsr;

/*************************************************************************************/
extern void INSTALLVECTOR();
extern void CAUSEBUSERR();
extern void REPLACEVECTOR();

/*************************************************************************************/
void    InitMac()
{
    InitGraf(&qd.thePort);
    InitFonts();
    FlushEvents(everyEvent,0);
    InitWindows();
    InitCursor();
    quit = false;
    DrawOn = false;
    IsBtn = false;
}
/*************************************************************************************/
void    DoDraw()
{
    DrawOn = true;
    GlobalToLocal(&MyEvent.where);
    MoveTo(MyEvent.where.h,MyEvent.where.v);
    EraseRect(&WindRect);
}
/*************************************************************************************/
main()
{
    InitMac();
    MyWindow = GetNewWindow(2009,nil,(WindowPtr)-1);

    if (MyWindow)
    {
        SetPort(MyWindow);
        while (quit != true)
        {
            if (DrawOn)
            {
                if (StillDown())
                {
                    GetMouse (&aPoint);
                    StdLine (aPoint);
                }
                else { DrawOn = false; }
            }
            else
            {
                if (WaitNextEvent(everyEvent,&MyEvent,0,nil))
                {
                    switch (MyEvent.what)
                    {
                        case mouseDown:
                        {
                            if ((FindWindow (MyEvent.where,&aWindPtr) == inContent) /* make sure the mouseDown is */
                            && (aWindPtr == MyWindow))                              /* where we want it */
                                { CAUSEBUSERR(); }
                            else if (FindWindow (MyEvent.where,&aWindPtr) == inGoAway)
                                { quit = true; }
                            break;
                        }
                        case keyDown:
                        {
                            if ((char)(BitAnd (MyEvent.message,charCodeMask)) == 'q')
                                { quit = true; }
                            break;
                        }
                    }
                }
            }
        }
        /* REPLACEVECTOR(); */
    }
}
```

[Next](BusErrTestInit.a.md)[Previous](BusErrTest.c.md)

