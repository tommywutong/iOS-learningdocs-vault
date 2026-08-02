---
title: jGNE Helper
apple_id: DTS10000188
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/jGNE_Helper/Listings/native_jGNE_native_jGNE_c.html
archived_at: '2026-07-18T03:29:47.783312Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [jGNE Helper](jGNE%20Helper.md)


[Next](Document%20Revision%20History.md)[Previous](jGNE%20Helper.c.md)

# native jGNE/native jGNE.c

```swift
#define OLDROUTINELOCATIONS     0
#define OLDROUTINENAMES         0
#define SystemSevenOrLater      1

#ifndef __FONTS__
#   include <Fonts.h>
#endif

#ifndef __DIALOGS__
#   include <Dialogs.h>
#endif

#ifndef __LOWMEM__
#   include <LowMem.h>
#endif

static pascal OSErr InitMac (void)
{
    MaxApplZone ( );
    InitGraf (&(qd.thePort));
    InitFonts ( );
    InitWindows ( );
    InitMenus ( );
    TEInit ( );
    InitDialogs (nil);

    return noErr;
}

static GetNextEventFilterUPP gGetNextEventFilterUPP;
static Boolean gFilterDone;

static void myGetNextEventFilter (EventRecord *event, Boolean *result)
{
    //
    //  IMPORTANT NOTE: It's not possible to declare a 68K jGNEFilter
    //  this way! Examine one of the jGNE Helper projects for an example
    //  of a 68K jGNEFilter. I hope to produce a "fat" filter some time
    //  in the near future.
    //

    if (gGetNextEventFilterUPP)
        CallGetNextEventFilterProc (gGetNextEventFilterUPP,event,result);

    if (*result && event->what == mouseDown)
    {
        event->what = nullEvent;
        *result = false;
        gFilterDone = true;
    }
}

void main (void)
{
    if (!InitMac ( ))
    {
        GetNextEventFilterUPP myFilterUPP = NewGetNextEventFilterProc (myGetNextEventFilter);

        if (myFilterUPP)
        {
            gGetNextEventFilterUPP = LMGetGNEFilter ( );
            LMSetGNEFilter (myFilterUPP);

            do
            {
                EventRecord event;
                WaitNextEvent (everyEvent,&event,1,nil);
            }
            while (!gFilterDone);

            if (LMGetGNEFilter ( ) != myFilterUPP)
                DebugStr ("\pSomeone else has gotten into the jGNE filter chain!");
            else
                LMSetGNEFilter (gGetNextEventFilterUPP);

            DisposeRoutineDescriptor (myFilterUPP);
        }
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](jGNE%20Helper.c.md)

