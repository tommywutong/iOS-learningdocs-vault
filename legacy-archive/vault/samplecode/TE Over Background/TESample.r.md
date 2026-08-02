---
title: TE Over Background
apple_id: DTS10000172
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/TE_Over_Background/Listings/TESample_r.html
archived_at: '2026-07-18T03:26:05.012927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TE Over Background](TE%20Over%20Background.md)


[Next](TESampleGlue.a.md)[Previous](TESample.h.md)

# TESample.r

```c
/*------------------------------------------------------------------------------
#
#   Apple Macintosh Developer Technical Support
#
#   MultiFinder-Aware TextEdit Sample Application
#
#   TESample
#
#   TESample.r  -   Rez Source
#
#   Copyright © 1989 Apple Computer, Inc.
#   All rights reserved.
#
#   Versions:   
#               1.00                08/88
#               1.01                11/88
#               1.02                04/89
#               1.03                06/89
#
#   Components:
#               TESample.p          June 1, 1989
#               TESample.c          June 1, 1989
#               TESampleGlue.a      June 1, 1989    -MPW only-
#               TESample.r          June 1, 1989
#               TESample.h          June 1, 1989
#               PTESample.make      June 1, 1989    -MPW only-
#               CTESample.make      June 1, 1989    -MPW only-
#               TESampleGlue.s      June 1, 1989    -A/UX only-
#               TESampleAUX.r       June 1, 1989    -A/UX only-
#               Makefile            June 1, 1989    -A/UX only-
#
#   TESample is an example application that demonstrates how 
#   to initialize the commonly used toolbox managers, operate 
#   successfully under MultiFinder, handle desk accessories and 
#   create, grow, and zoom windows. The fundamental TextEdit 
#   toolbox calls and TextEdit autoscroll are demonstrated. It 
#   also shows how to create and maintain scrollbar controls.
#
#   It does not by any means demonstrate all the techniques you 
#   need for a large application. In particular, Sample does not 
#   cover exception handling, multiple windows/documents, 
#   sophisticated memory management, printing, or undo. All of 
#   these are vital parts of a normal full-sized application.
#
#   This application is an example of the form of a Macintosh 
#   application; it is NOT a template. It is NOT intended to be 
#   used as a foundation for the next world-class, best-selling, 
#   600K application. A stick figure drawing of the human body may 
#   be a good example of the form for a painting, but that does not 
#   mean it should be used as the basis for the next Mona Lisa.
#
#   We recommend that you review this program or Sample before 
#   beginning a new application. Sample is a simple app. which doesnÕt 
#   use TextEdit or the Control Manager.
#
------------------------------------------------------------------------------*/

include "TESample.¹.rsrc";

#include "types.r"


/* here is the quintessential MultiFinder friendliness device, the SIZE resource */

resource 'SIZE' (-1) {
    dontSaveScreen,
    acceptSuspendResumeEvents,
    enableOptionSwitch,
    canBackground,              /* we can background; we don't currently, but our sleep value */
                                /* guarantees we don't hog the Mac while we are in the background */
    multiFinderAware,           /* this says we do our own activate/deactivate; don't fake us out */
    backgroundAndForeground,    /* this is definitely not a background-only application! */
    dontGetFrontClicks,         /* change this is if you want "do first click" behavior like the Finder */
    ignoreChildDiedEvents,      /* essentially, I'm not a debugger (sub-launching) */
    not32BitCompatible,         /* this app should not be run in 32-bit address space */
    reserved,
    reserved,
    reserved,
    reserved,
    reserved,
    reserved,
    reserved,
    384 * 1024,
    384 * 1024  
};
```

[Next](TESampleGlue.a.md)[Previous](TESample.h.md)

