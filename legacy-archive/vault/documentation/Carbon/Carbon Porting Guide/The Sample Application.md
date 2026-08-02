---
title: Carbon Porting Guide
apple_id: TP30000991
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-12-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/carbon_porting_guide/cpg_apdx_sampleapp/cpg_apdx_sample_app.html
archived_at: '2026-07-15T05:24:53.431939Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Porting Guide](Introduction%20to%20Carbon%20Porting%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](New%20Carbon%20Functions.md)

# The Sample Application

The main code for Sample is included in `Sample.c` and `SampleInit.c` as shown in Listing B-1 and [Listing B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqg4wueqshijbuqskd). Sample also includes a definition file, `Sample.h`, and a compiled resource file, `TCSample.rsrc.`

The chapter [A Porting Example](A%20Porting%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgqwviucykjcummjqge) describes how to port the Sample application to Carbon. [An Example: Adding Carbon Events to Sample](New%20Carbon%20Technologies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqguwueqkcijdegq2j) describes how to add Carbon events to the Carbon version of Sample.

__Listing B-1__  Sample.c

```c

/*
    File:       Sample.c

    Contains:   Sample is an example application that demonstrates how to
                initialize the commonly used toolbox managers, operate
                successfully under MultiFinder, handle desk accessories,
                and create, grow, and zoom windows.

                It does not by any means demonstrate all the techniques
                you need for a large application. In particular, Sample
                does not cover exception handling, multiple windows/documents,
                sophisticated memory management, printing, or undo. All of
                these are vital parts of a normal full-sized application.

                This application is an example of the form of a Macintosh
                application; it is NOT a template. It is NOT intended to be
                used as a foundation for the next world-class, best-selling,
                600K application. A stick figure drawing of the human body may
                be a good example of the form for a painting, but that does not
                mean it should be used as the basis for the next Mona Lisa.

                We recommend that you review this program or TESample before
                beginning a new application.

    Written by:

    Copyright:  Copyright © 1988-1999 by Apple Computer, Inc., All Rights Reserved.

    You may incorporate this Apple sample source code into your program(s) without
    restriction. This Apple sample source code has been provided "AS IS" and the
    responsibility for its operation is yours. You are not permitted to redistribute
    this Apple sample source code as "Apple sample source code" after having made
    changes. If you're going to re-distribute the source, we require that you make
    it clear in the source that the code was descended from Apple sample source
    code, but that you've made changes.

    Change History (most recent first):
    8/13/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1
*/

/* Segmentation strategy:

   This program consists of three segments.
   1. "Main" contains most of the code, including the MPW libraries, and the
      main program.  This segment is in the file Sample.c
   2. "Initialize" contains code that is only used once, during startup, and
      can be unloaded after the program starts.  This segment is in the file
      SampleInit.c.
   3. "%A5Init" is automatically created by the Linker to initialize globals
      for the MPW libraries and is unloaded right away. */


/* SetPort strategy:

   Toolbox routines do not change the current port. In spite of this, in this
   program we use a strategy of calling SetPort whenever we want to draw or
   make calls which depend on the current port. This makes us less vulnerable
   to bugs in other software which might alter the current port (such as the
   bug (feature?) in many desk accessories which change the port on OpenDeskAcc).
   Hopefully, this also makes the routines from this program more self-contained,
   since they don't depend on the current port setting. */

#pragma segment Main

#include <Limits.h>
#include <Types.h>
#include <Resources.h>
#include <QuickDraw.h>
#include <Fonts.h>
#include <Events.h>
#include <Windows.h>
#include <Menus.h>
#include <TextEdit.h>
#include <Dialogs.h>
#include <Desk.h>
#include <ToolUtils.h>
#include <Memory.h>
#include <SegLoad.h>
#include <Files.h>
#include <OSUtils.h>
#include <DiskInit.h>
#include <Packages.h>
#include <Traps.h>
#include "Sample.h      "/* bring in all the #defines for Sample */

/* The "g" prefix is used to emphasize that a variable is global. */

/* GMac is used to hold the result of a SysEnvirons call. This makes
   it convenient for any routine to check the environment. */
SysEnvRec   gMac;               /* set up by Initialize */

/* GHasWaitNextEvent is set at startup, and tells whether the WaitNextEvent
   trap is available. If it is false, we know that we must call GetNextEvent. */
Boolean     gHasWaitNextEvent;  /* set up by Initialize */

/* GInBackground is maintained by our osEvent handling routines. Any part of
   the program can check it to find out if it is currently in the background. */
Boolean     gInBackground;      /* maintained by Initialize and DoEvent */


/* The following globals are the state of the window. If we supported more than
   one window, they would be attached to each document, rather than globals. */

/* GStopped tells whether the stop light is currently on stop or go. */
Boolean     gStopped;           /* maintained by Initialize and SetLight */

/* GStopRect and gGoRect are the rectangles of the two stop lights in the window. */
Rect        gStopRect;          /* set up by Initialize */
Rect        gGoRect;            /* set up by Initialize */


/* Define TopLeft and BotRight macros for convenience. Notice the implicit
   dependency on the ordering of fields within a Rect */
#define TopLeft(aRect)  (* (Point *) &(aRect).top)
#define BotRight(aRect) (* (Point *) &(aRect).bottom)


/* This routine is part of the MPW runtime library. This external
   reference to it is done so that we can unload its segment, %A5Init. */

#ifndef THINK_C
  extern void _DataInit();
#endif


void main()
{
#ifndef THINK_C
    UnloadSeg((Ptr) _DataInit);     /* note that _DataInit must not be in Main! */
#endif

    /* 1.01 - call to ForceEnvirons removed */

    /*  If you have stack requirements that differ from the default,
        then you could use SetApplLimit to increase StackSpace at
        this point, before calling MaxApplZone. */
    MaxApplZone();          /* expand the heap so code segments load at the top */

    Initialize();                   /* initialize the program */
    UnloadSeg((Ptr) Initialize);    /* note that Initialize must not be in Main! */

    EventLoop();                    /* call the main event loop */
} /*main*/


/*  Get events forever, and handle them by calling DoEvent.
    Get the events by calling WaitNextEvent, if it's available, otherwise
    by calling GetNextEvent. Also call AdjustCursor each time through the loop. */

void EventLoop()
{
    RgnHandle   cursorRgn;
    Boolean     gotEvent;
    EventRecord event;
    Point       mouse;

    cursorRgn = NewRgn();   /* we’ll pass WNE an empty region the 1st time thru */
    do {
        /* use WNE if it is available */
        if ( gHasWaitNextEvent ) {
            GetGlobalMouse(&mouse);
            AdjustCursor(mouse, cursorRgn);
            gotEvent = WaitNextEvent(everyEvent, &event, LONG_MAX, cursorRgn);
        }
        else {
            SystemTask();
            gotEvent = GetNextEvent(everyEvent, &event);
        }
        if ( gotEvent ) {
            /* make sure we have the right cursor before handling the event */
            AdjustCursor(event.where, cursorRgn);
            DoEvent(&event);
        }
        /*  If you are using modeless dialogs that have editText items,
            you will want to call IsDialogEvent to give the caret a chance
            to blink, even if WNE/GNE returned FALSE. However, check FrontWindow
            for a non-NIL value before calling IsDialogEvent. */
    } while ( true );   /* loop forever; we quit via ExitToShell */
} /*EventLoop*/

/* Do the right thing for an event. Determine what kind of event it is, and call
 the appropriate routines. */

void DoEvent(EventRecord *event)
{
    short       part, err;
    WindowPtr   window;
    Boolean     hit;
    char        key;
    Point       aPoint;

    switch ( event->what ) {
        case mouseDown:
            part = FindWindow(event->where, &window);
            switch ( part ) {
                case inMenuBar:         /* process a mouse menu command (if any) */
                    AdjustMenus();
                    DoMenuCommand(MenuSelect(event->where));
                    break;
                case inSysWindow:       /* let the system handle the mouseDown */
                    SystemClick(event, window);
                    break;
                case inContent:
                    if ( window != FrontWindow() ) {
                        SelectWindow(window);
                        /*DoEvent(event);*//* use this line for "do first click" */
                    } else
                        DoContentClick(window);
                    break;
                case inDrag:    /* pass screenBits.bounds to get all gDevices */
                    DragWindow(window, event->where, &qd.screenBits.bounds);
                    break;
                case inGrow:
                    break;
                case inZoomIn:
                case inZoomOut:
                    hit = TrackBox(window, event->where, part);
                    if ( hit ) {
                        SetPort(window); /* the window must be the current port... */
                        EraseRect(&window->portRect);   /* because of a bug in */
                                                        /* ZoomWindow */
                        ZoomWindow(window, part, true); /* note that we invalidate */
                                                        /* and erase... */
                        InvalRect(&window->portRect);   /* to make things look */
                                                        /* better on-screen */
                    }
                    break;
            }
            break;
        case keyDown:
        case autoKey:                       /* check for menukey equivalents */
            key = event->message & charCodeMask;
            if ( event->modifiers & cmdKey )            /* Command key down */
                if ( event->what == keyDown ) {
                    AdjustMenus();      /* enable/disable/check menu items properly */
                    DoMenuCommand(MenuKey(key));
                }
            break;
        case activateEvt:
            DoActivate((WindowPtr) event->message,
                        (event->modifiers & activeFlag) != 0);
            break;
        case updateEvt:
            DoUpdate((WindowPtr) event->message);
            break;
        /*  1.01 - It is not a bad idea to at least call DIBadMount in response
            to a diskEvt, so that the user can format a floppy. */
        case diskEvt:
            if ( HiWord(event->message) != noErr ) {
                SetPt(&aPoint, kDILeft, kDITop);
                err = DIBadMount(aPoint, event->message);
            }
            break;
        case kOSEvent:
        /*  1.02 - must BitAND with 0x0FF to get only low byte */
            switch ((event->message >> 24) & 0x0FF) {       /* high byte of message */
                case kSuspendResumeMessage: /* suspend/resume is also an */
                                            /* activate/deactivate */
                    gInBackground = (event->message & kResumeMask) == 0;
                    DoActivate(FrontWindow(), !gInBackground);
                    break;
            }
            break;
    }
} /*DoEvent*/


/*  Change the cursor's shape, depending on its position. This also calculates the region
    where the current cursor resides (for WaitNextEvent). If the mouse is ever outside of
    that region, an event would be generated, causing this routine to be called,
    allowing us to change the region to the region the mouse is currently in. If
    there is more to the event than just “the mouse moved”, we get called before the
    event is processed to make sure the cursor is the right one. In any (ahem) event,
    this is called again before we fall back into WNE. */

void AdjustCursor(Point mouse, RgnHandle region)
{
    WindowPtr   window;
    RgnHandle   arrowRgn;
    RgnHandle   plusRgn;
    Rect        globalPortRect;

    window = FrontWindow(); /* we only adjust the cursor when we are in front */
    if ( (! gInBackground) && (! IsDAWindow(window)) ) {
        /* calculate regions for different cursor shapes */
        arrowRgn = NewRgn();
        plusRgn = NewRgn();

        /* start with a big, big rectangular region */
        SetRectRgn(arrowRgn, kExtremeNeg, kExtremeNeg, kExtremePos, kExtremePos);

        /* calculate plusRgn */
        if ( IsAppWindow(window) ) {
            SetPort(window);    /* make a global version of the viewRect */
            SetOrigin(-window->portBits.bounds.left, -window->portBits.bounds.top);
            globalPortRect = window->portRect;
            RectRgn(plusRgn, &globalPortRect);
            SectRgn(plusRgn, window->visRgn, plusRgn);
            SetOrigin(0, 0);
        }

        /* subtract other regions from arrowRgn */
        DiffRgn(arrowRgn, plusRgn, arrowRgn);

        /* change the cursor and the region parameter */
        if ( PtInRgn(mouse, plusRgn) ) {
            SetCursor(*GetCursor(plusCursor));
            CopyRgn(plusRgn, region);
        } else {
            SetCursor(&qd.arrow);
            CopyRgn(arrowRgn, region);
        }

        /* get rid of our local regions */
        DisposeRgn(arrowRgn);
        DisposeRgn(plusRgn);
    }
} /*AdjustCursor*/


/*  Get the global coordinates of the mouse. When you call OSEventAvail
    it will return either a pending event or a null event. In either case,
    the where field of the event record will contain the current position
    of the mouse in global coordinates and the modifiers field will reflect
    the current state of the modifiers. Another way to get the global
    coordinates is to call GetMouse and LocalToGlobal, but that requires
    being sure that thePort is set to a valid port. */

void GetGlobalMouse(Point *mouse)
{
    EventRecord event;

    OSEventAvail(kNoEvents, &event);    /* we aren't interested in any events */
    *mouse = event.where;               /* just the mouse position */
} /*GetGlobalMouse*/


/*  This is called when an update event is received for a window.
    It calls DrawWindow to draw the contents of an application window.
    As an efficiency measure that does not have to be followed, it
    calls the drawing routine only if the visRgn is non-empty. This
    will handle situations where calculations for drawing or drawing
    itself is very time-consuming. */

void DoUpdate(WindowPtr window)
{
    if ( IsAppWindow(window) ) {
        BeginUpdate(window);                /* this sets up the visRgn */
        if ( ! EmptyRgn(window->visRgn) )   /* draw if updating needs to be done */
            DrawWindow(window);
        EndUpdate(window);
    }
} /*DoUpdate*/


/*  This is called when a window is activated or deactivated.
    In Sample, the Window Manager's handling of activate and
    deactivate events is sufficient. Other applications may have
    TextEdit records, controls, lists, etc., to activate/deactivate. */

void DoActivate(WindowPtr window, Boolean becomingActive)
{
    if ( IsAppWindow(window) ) {
        if ( becomingActive )
            /* do whatever you need to at activation */ ;
        else
            /* do whatever you need to at deactivation */ ;
    }
} /*DoActivate*/


/*  This is called when a mouse-down event occurs in the content of a window.
    Other applications might want to call FindControl, TEClick, etc., to
    further process the click. */

void DoContentClick(WindowPtr window)
{
    SetLight(window, ! gStopped);
} /*DoContentClick*/


/* Draw the contents of the application window. We do some drawing in color, using
   Classic QuickDraw's color capabilities. This will be black and white on old
   machines, but color on color machines. At this point, the window’s visRgn
   is set to allow drawing only where it needs to be done. */

void DrawWindow(WindowPtr window)
{
    SetPort(window);

    EraseRect(&window->portRect);   /* clear out any garbage that may linger */
    if ( gStopped )                 /* draw a red (or white) stop light */
        ForeColor(redColor);
    else
        ForeColor(whiteColor);

    PaintOval(&gStopRect);
    ForeColor(blackColor);
    FrameOval(&gStopRect);

    if ( ! gStopped )               /* draw a green (or white) go light */
        ForeColor(greenColor);
    else
        ForeColor(whiteColor);

    PaintOval(&gGoRect);
    ForeColor(blackColor);
    FrameOval(&gGoRect);
} /*DrawWindow*/


/*  Enable and disable menus based on the current state.
    The user can only select enabled menu items. We set up all the menu items
    before calling MenuSelect or MenuKey, since these are the only times that
    a menu item can be selected. Note that MenuSelect is also the only time
    the user will see menu items. This approach to deciding what enable/
    disable state a menu item has the advantage of concentrating all
    the decision-making in one routine, as opposed to being spread throughout
    the application. Other application designs may take a different approach
    that is just as valid. */

void AdjustMenus()
{
    WindowPtr   window;
    MenuHandle  menu;

    window = FrontWindow();

    menu = GetMenuHandle(mFile);
    if ( IsDAWindow(window) )       /* we can allow desk accessories to be */
                                    /* closed from the menu */
        EnableItem(menu, iClose);
    else
        DisableItem(menu, iClose);  /* but not our traffic light window */

    menu = GetMenuHandle(mEdit);
    if ( IsDAWindow(window) ) {     /* a desk accessory might need the edit menu… */
        EnableItem(menu, iUndo);
        EnableItem(menu, iCut);
        EnableItem(menu, iCopy);
        EnableItem(menu, iClear);
        EnableItem(menu, iPaste);
    } else {                        /* …but we don’t use it */
        DisableItem(menu, iUndo);
        DisableItem(menu, iCut);
        DisableItem(menu, iCopy);
        DisableItem(menu, iClear);
        DisableItem(menu, iPaste);
    }

    menu = GetMenuHandle(mLight);
    if ( IsAppWindow(window) ) {    /* we know that it must be the traffic light */
        EnableItem(menu, iStop);
        EnableItem(menu, iGo);
    } else {
        DisableItem(menu, iStop);
        DisableItem(menu, iGo);
    }
    CheckItem(menu, iStop, gStopped); /* we can also determine the check/uncheck */
                                     /* state,too */
    CheckItem(menu, iGo, ! gStopped);
} /*AdjustMenus*/


/*  This is called when an item is chosen from the menu bar (after calling
    MenuSelect or MenuKey). It performs the right operation for each command.
    It is good to have both the result of MenuSelect and MenuKey go to
    one routine like this to keep everything organized. */

void DoMenuCommand(long menuResult)
{
    short       menuID;             /* the resource ID of the selected menu */
    short       menuItem;           /* the item number of the selected menu */
    short       itemHit;
    Str255      daName;
    short       daRefNum;
    Boolean     handledByDA;

    menuID = HiWord(menuResult);    /* use macros for efficiency to... */
    menuItem = LoWord(menuResult);  /* get menu item number and menu number */
    switch ( menuID ) {
        case mApple:
            switch ( menuItem ) {
                case iAbout:        /* bring up alert for About */
                    itemHit = Alert(rAboutAlert, nil);
                    break;
                default:            /* all non-About items in this menu are DAs */
                    /* type Str255 is an array in MPW 3 */
                    GetMenuItemText(GetMenuHandle(mApple), menuItem, daName);
                    daRefNum = OpenDeskAcc(daName);
                    break;
            }
            break;
        case mFile:
            switch ( menuItem ) {
                case iClose:
                    DoCloseWindow(FrontWindow());
                    break;
                case iQuit:
                    Terminate();
                    break;
            }
            break;
        case mEdit:                 /* call SystemEdit for DA editing & MultiFinder */
            handledByDA = SystemEdit(menuItem-1);/* since we don’t do any Editing */
            break;
        case mLight:
            switch ( menuItem ) {
                case iStop:
                    SetLight(FrontWindow(), true);
                    break;
                case iGo:
                    SetLight(FrontWindow(), false);
                    break;
            }
            break;
    }
    HiliteMenu(0);              /* unhighlight what MenuSelect (or MenuKey) hilited */
} /*DoMenuCommand*/


/* Change the setting of the light. */

void SetLight(WindowPtr window, Boolean newStopped)
{
    if ( newStopped != gStopped ) {
        gStopped = newStopped;
        SetPort(window);
        InvalRect(&window->portRect);
    }
} /*SetLight*/


/* Close a window. This handles desk accessory and application windows. */

/*  1.01 - At this point, if there was a document associated with a
    window, you could do any document saving processing if it is 'dirty'.
    DoCloseWindow would return true if the window actually closed, i.e.,
    the user didn’t cancel from a save dialog. This result is handy when
    the user quits an application, but then cancels the save of a document
    associated with a window. */

Boolean DoCloseWindow(WindowPtr window)
{
    if ( IsDAWindow(window) )
        CloseDeskAcc(((WindowPeek) window)->windowKind);
    else if ( IsAppWindow(window) )
        CloseWindow(window);
    return true;
} /*DoCloseWindow*/


/**************************************************************************************
*** 1.01 DoCloseBehind(window) was removed ***

    1.01 - DoCloseBehind was a good idea for closing windows when quitting
    and not having to worry about updating the windows, but it suffered
    from a fatal flaw. If a desk accessory owned two windows, it would
    close both those windows when CloseDeskAcc was called. When DoCloseBehind
    got around to calling DoCloseWindow for that other window that was already
    closed, things would go very poorly. Another option would be to have a
    procedure, GetRearWindow, that would go through the window list and return
    the last window. Instead, we decided to present the standard approach
    of getting and closing FrontWindow until FrontWindow returns NIL. This
    has a potential benefit in that the window whose document needs to be saved
    may be visible since it is the front window, therefore decreasing the
    chance of user confusion. For aesthetic reasons, the windows in the
    application should be checked for updates periodically and have the
    updates serviced.
**************************************************************************************/


/* Clean up the application and exit. We close all of the windows so that
 they can update their documents, if any. */

/*  1.01 - If we find out that a cancel has occurred, we won't exit to the */
/*          shell, but will return instead. */

void Terminate()
{
    WindowPtr   aWindow;
    Boolean     closed;

    closed = true;
    do {
        aWindow = FrontWindow();                /* get the current front window */
        if (aWindow != nil)
            closed = DoCloseWindow(aWindow);    /* close this window */
    }
    while (closed && (aWindow != nil));
    if (closed)
        ExitToShell();                          /* exit if no cancellation */
} /*Terminate*/


/*  Check to see if a window belongs to the application. If the window pointer
    passed was NIL, then it could not be an application window. WindowKinds
    that are negative belong to the system and windowKinds less than userKind
    are reserved by Apple except for windowKinds equal to dialogKind, which
    mean it is a dialog.
    1.02 - In order to reduce the chance of accidentally treating some window
    as an AppWindow that shouldn't be, we'll only return true if the windowkind
    is userKind. If you add different kinds of windows to Sample you'll need
    to change how this all works. */

Boolean IsAppWindow(WindowPtr window)
{
    short       windowKind;

    if ( window == nil )
        return false;
    else {  /* application windows have windowKinds = userKind (8) */
        windowKind = ((WindowPeek) window)->windowKind;
        return ( windowKind == userKind );
    }
} /*IsAppWindow*/


/* Check to see if a window belongs to a desk accessory. */

Boolean IsDAWindow(WindowPtr window)
{
    if ( window == nil )
        return false;
    else    /* DA windows have negative windowKinds */
        return ( ((WindowPeek) window)->windowKind < 0 );
} /*IsDAWindow*/


/*  Display an alert that tells the user an error occurred, then exit the program.
    This routine is used as an ultimate bail-out for serious errors that prohibit
    the continuation of the application. Errors that do not require the termination
    of the application should be handled in a different manner. Error checking and
    reporting has a place even in the simplest application. The error number is used
    to index an 'STR#' resource so that a relevant message can be displayed. */

void AlertUser()
{
    short       itemHit;

    SetCursor(&qd.arrow);
    itemHit = Alert(rUserAlert, nil);
    ExitToShell();
} /* AlertUser */
```


__Listing B-2__  SampleInit.c

```c

/* File:            SampleInit.c */

/* Repeated comments from Sample.c removed */

#pragma segment Initialize

#include <Limits.h>
#include <Types.h>
#include <Resources.h>
#include <QuickDraw.h>
#include <Fonts.h>
#include <Events.h>
#include <Windows.h>
#include <Menus.h>
#include <TextEdit.h>
#include <Dialogs.h>
#include <Desk.h>
#include <ToolUtils.h>
#include <Memory.h>
#include <SegLoad.h>
#include <Files.h>
#include <OSUtils.h>
#include <DiskInit.h>
#include <Packages.h>
#include <Traps.h>
#include <OSUtils.h>
#include "Sample.h      "/* bring in all the #defines for Sample */


/* The "g" prefix is used to emphasize that a variable is global. */
/* All are extern since the variables are declared in the main segment. */

/* GMac is used to hold the result of a SysEnvirons call. This makes
   it convenient for any routine to check the environment. */
extern SysEnvRec    gMac;               /* set up by Initialize */

/* GHasWaitNextEvent is set at startup, and tells whether the WaitNextEvent
   trap is available. If it is false, we know that we must call GetNextEvent. */
extern Boolean      gHasWaitNextEvent;  /* set up by Initialize */

/* GInBackground is maintained by our osEvent handling routines. Any part of
   the program can check it to find out if it is currently in the background. */
extern Boolean      gInBackground;      /* maintained by Initialize and DoEvent */


/* The following globals are the state of the window. If we supported more than
   one window, they would be attached to each document, rather than globals. */

/* GStopped tells whether the stop light is currently on stop or go. */
extern Boolean      gStopped;           /* maintained by Initialize and SetLight */

/* GStopRect and gGoRect are the rectangles of the two stop lights in the window. */
extern Rect     gStopRect;          /* set up by Initialize */
extern Rect     gGoRect;            /* set up by Initialize */


/*  Set up the whole world, including global variables, Toolbox managers,
    and menus. We also create our one application window at this time.
    Since window storage is non-relocateable, how and when to allocate space
    for windows is very important so that heap fragmentation does not occur.
    Because Sample has only one window and it is only disposed when the application
    quits, we will allocate its space here, before anything that might be a locked
    relocatable object gets into the heap. This way, we can force the storage to be
    in the lowest memory available in the heap. Window storage can differ widely
    amongst applications depending on how many windows are created and disposed. */

/*  1.01 - The code that used to be part of ForceEnvirons has been moved into
    this module. If an error is detected, instead of merely doing an ExitToShell,
    which leaves the user without much to go on, we call AlertUser, which puts
    up a simple alert that just says an error occurred and then calls ExitToShell.
    Since there is no other cleanup needed at this point if an error is detected,
    this form of error- handling is acceptable. If more sophisticated error recovery
    is needed, an exception mechanism, such as is provided by Signals, can be used. */

void Initialize()
{
    Handle      menuBar;
    WindowPtr   window;
    long        total, contig;
    EventRecord event;
    short       count;

    gInBackground = false;

    InitGraf((Ptr) &qd.thePort);
    InitFonts();
    InitWindows();
    InitMenus();
    TEInit();
    InitDialogs(nil);
    InitCursor();

    /*  Call MPPOpen and ATPLoad at this point to initialize AppleTalk,
        if you are using it. */
    /*  NOTE -- It is no longer necessary, and actually unhealthy, to check
        PortBUse and SPConfig before opening AppleTalk. The drivers are capable
        of checking for port availability themselves. */

    /*  This next bit of code is necessary to allow the default button of our
        alert be outlined.
        1.02 - Changed to call EventAvail so that we don't lose some important
        events. */

    for (count = 1; count <= 3; count++)
        EventAvail(everyEvent, &event);

    /*  Ignore the error returned from SysEnvirons; even if an error occurred,
        the SysEnvirons glue will fill in the SysEnvRec. You can save a redundant
        call to SysEnvirons by calling it after initializing AppleTalk. */

    SysEnvirons(kSysEnvironsVersion, &gMac);

    /* Make sure that the machine has at least 128K ROMs. If it doesn't, exit. */

    if (gMac.machineType < 0) AlertUser();

    /*  1.02 - Move TrapAvailable call to after SysEnvirons so that we can tell
        in TrapAvailable if a tool trap value is out of range. */

    gHasWaitNextEvent = TrapAvailable(_WaitNextEvent, ToolTrap);

    /*  1.01 - We used to make a check for memory at this point by examining ApplLimit,
        ApplicationZone, and StackSpace and comparing that to the minimum size we told
        MultiFinder we needed. This did not work well because it assumed too much about
        the relationship between what we asked MultiFinder for and what we would actually
        get back, as well as how to measure it. Instead, we will use an alternate
        method comprised of two steps. */

    /*  It is better to first check the size of the application heap against a value
        that you have determined is the smallest heap the application can reasonably
        work in. This number should be derived by examining the size of the heap that
        is actually provided by MultiFinder when the minimum size requested is used.
        The derivation of the minimum size requested from MultiFinder is described
        in Sample.h. The check should be made because the preferred size can end up
        being set smaller than the minimum size by the user. This extra check acts to
        insure that your application is starting from a solid memory foundation. */

    if ((long) GetApplLimit() - (long) ApplicationZone() < kMinHeap) AlertUser();

    /*  Next, make sure that enough memory is free for your application to run. It
        is possible for a situation to arise where the heap may have been of required
        size, but a large scrap was loaded which left too little memory. To check for
        this, call PurgeSpace and compare the result with a value that you have
        determined is the minimum amount of free memory your application needs at
        initialization. This number can be derived several different ways. One way that
        is fairly straightforward is to run the application in the minimum size
        configuration as described previously. Call PurgeSpace at initialization and
        examine the value returned. However, you should make sure that this result is not
        being modified by the scrap's presence. You can do that by calling ZeroScrap
        before calling PurgeSpace. Remove this call before shipping, though. */

    /* ZeroScrap(); */

    PurgeSpace(&total, &contig);
    if (total < kMinSpace) AlertUser();

    /*  The extra benefit to waiting until after the Toolbox Managers have been
        initialized to check memory is that we can now give the user an alert to tell
        him/her what happened. Although it is possible that the memory situation could
        be worsened by displaying an alert, MultiFinder would gracefully exit the
        application with an informative alert if memory became critical. Here we are
        acting more in a preventative manner to avoid future disaster from low-memory
        problems. */

    /*  We will allocate our own window storage instead of letting the Window
        Manager do it because GetNewWindow may load in temp. resources before
        making the NewPtr call, and this can lead to heap fragmentation. */

    window = (WindowPtr) NewPtr(sizeof(WindowRecord));
    if ( window == nil ) AlertUser();
    window = GetNewWindow(rWindow, (Ptr) window, (WindowPtr) -1);

    menuBar = GetNewMBar(rMenuBar);         /* read menus into menu bar */
    if ( menuBar == nil ) AlertUser();
    SetMenuBar(menuBar);                    /* install menus */
    DisposeHandle(menuBar);
    AppendResMenu(GetMenuHandle(mApple), 'DRVR');   /* add DA names to Apple menu */
    DrawMenuBar();

    gStopped = true;
    if ( !GoGetRect(rStopRect, &gStopRect) )
        AlertUser();                        /* the stop light rectangle */
    if ( !GoGetRect(rGoRect, &gGoRect) )
        AlertUser();                        /* the go light rectangle */
} /*Initialize*/


/*  This utility loads the global rectangles that are used by the window
    drawing routines. It shows how the resource manager can be used to hold
    values in a convenient manner. These values are then easily altered without
    having to re-compile the source code. In this particular case, we know
    that this routine is being called at initialization time. Therefore,
    if a failure occurs here, we will assume that the application is in such
    bad shape that we should just exit. Your error handling may differ, but
    the check should still be made. */

Boolean GoGetRect(short rectID, Rect *theRect)
{
    Handle      resource;

    resource = GetResource('RECT', rectID);
    if ( resource != nil ) {
        *theRect = **((Rect**) resource);
        return true;
    }
    else
        return false;
} /* GoGetRect */


/*  Check to see if a given trap is implemented. This is only used by the
    Initialize routine in this program, so we put it in the Initialize segment.
    The recommended approach to see if a trap is implemented is to see if
    the address of the trap routine is the same as the address of the
    Unimplemented trap. */
/*  1.02 - Needs to be called after call to SysEnvirons so that it can check
    if a ToolTrap is out of range of a pre-MacII ROM. */

Boolean TrapAvailable(short tNumber, TrapType tType)
{
    if ( ( tType == ToolTrap ) &&
        ( gMac.machineType > envMachUnknown ) &&
        ( gMac.machineType < envMacII ) ) {     /* it's a 512KE, Plus, or SE */
        tNumber = tNumber & 0x03FF;
        if ( tNumber > 0x01FF )                 /* which means the tool traps */
            tNumber = _Unimplemented;           /* only go to 0x01FF */
    }
    return NGetTrapAddress(tNumber, tType) !=
                                        NGetTrapAddress(_Unimplemented, ToolTrap);
} /*TrapAvailable*/
```

[Next](Document%20Revision%20History.md)[Previous](New%20Carbon%20Functions.md)

