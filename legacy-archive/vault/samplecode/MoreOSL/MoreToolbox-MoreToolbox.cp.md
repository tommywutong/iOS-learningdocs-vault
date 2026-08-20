---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreToolbox_MoreToolbox_cp.html
archived_at: '2026-07-18T03:15:55.599662Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreToolbox-MoreToolbox.h.md)[Previous](MoreTextUtils-MoreTextUtils.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreToolbox/MoreToolbox.cp

```c
/*
    File:       MoreToolbox.cp

    Contains:   

    Written by: Pete Gontier

    Copyright:  Copyright (c) 1998 Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <5>      2/9/99    PCG     lose QDGlobals and ShowWatchCursor
         <4>     1/29/99    PCG     new Carbon
         <3>     1/22/99    PCG     TARGET_CARBON
         <2>    11/11/98    PCG     fix header
         <1>    11/10/98    PCG     first big re-org at behest of Quinn

    Old Change History (most recent first):

         <3>    10/23/98    PCG     add HavePowerManager
         <2>     7/24/98    PCG     eliminate dependency on 'qd'
         <1>     6/16/98    PCG     initial checkin
*/

#include "MoreToolbox.h"
#include "MoreQuickDraw.h"
#include "MoreAppearance.h"

#include <MacMemory.h>
#include <Fonts.h>
#include <Dialogs.h>
#include <Sound.h>
#include <Gestalt.h>
#include <Power.h>

static long     gSystemVersion;
static Boolean  gHavePowerManager;

pascal long GetSystemVersion (void)
{
    //
    //  Simply returns our cached variable. See InitMac
    //  for how this variable is initialized.
    //

    return gSystemVersion;
}

pascal Boolean HaveAppleEvents (void)
{
    return 0x0700 <= GetSystemVersion ( ); // cheating
}

pascal OSStatus InitMac (void)
{
    OSStatus err = noErr;

    if (!(err = Gestalt (gestaltSystemVersion, &gSystemVersion)))
    {
        long powerMgrResponse;
        err = Gestalt (gestaltPowerMgrAttr,&powerMgrResponse);

        if (err == gestaltUndefSelectorErr)
            err = noErr;
        else if (!err)
        {
            gHavePowerManager = (powerMgrResponse & (1L << gestaltPMgrExists)) ? true : false;

#if !TARGET_CARBON

            MaxApplZone ( );
            (void) MoreAssert (MemError ( ) == noErr);

            InitGraf (&(qd.thePort));
            InitFonts ( );
            InitWindows ( );
            InitMenus ( );
            TEInit ( );
            InitDialogs (nil);

#endif

            if (!(err = InitMoreQuickDraw ( )))
            {
                if (!(err = InitMoreAppearance ( )))
                {
                    err = ShowWatchCursor ( );
                }
            }
        }
    }

    return err;
}

pascal void Beep (void)
{
    SysBeep (10);
}

pascal Boolean HavePowerManager (void)
{
    return gHavePowerManager;
}
```

[Next](MoreToolbox-MoreToolbox.h.md)[Previous](MoreTextUtils-MoreTextUtils.h.md)

