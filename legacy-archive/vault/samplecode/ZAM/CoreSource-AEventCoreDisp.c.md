---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_AEventCoreDisp_c.html
archived_at: '2026-07-18T03:28:31.939561Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-Document.c.md)[Previous](CoreSource-AdjustMenus.c.md)

# CoreSource/AEventCoreDisp.c

```c

#include "CoreGlobals.h"


pascal OSErr AEOpenApp( AppleEvent *theAE, AppleEvent *reply, long rfCon)
{
    return noErr;
}

pascal OSErr AEOpenDoc( AppleEvent  *theAE, AppleEvent  *reply, long  rfCon)
{
    return errAEEventNotHandled;
}


pascal OSErr AEPrintDoc( AppleEvent  *theAE, AppleEvent  *reply, long  rfCon)
{
    return errAEEventNotHandled;
}


pascal OSErr AEQuitApp( AppleEvent  *theAE, AppleEvent  *reply, long  rfCon)
{
    gDone = true;       /* set flag to indicate that program should quit */ 
    return noErr;
}

void DoHighLevelEvent(EventRecord *evt)
{
    short   err;

    err = AEProcessAppleEvent(evt);
    if(err)
    {
        ErrMsgCode("\pError processing Apple Event in DoHighLevelEvent",err);
    }
}

void InstallAppleEvents(void)
{
    short   err;

    err = AEInstallEventHandler (kCoreEventClass, kAEOpenApplication, AEOpenApp,0,FALSE);
    if(err)
    {
        ErrMsgCode("\pCould not install AE handler.",err);
        ExitToShell();
    }

    err = AEInstallEventHandler (kCoreEventClass, kAEOpenDocuments, AEOpenDoc,0,FALSE);
    if(err)
    {
        ErrMsgCode("\pCould not install AE handler.",err);
        ExitToShell();
    }

    err = AEInstallEventHandler (kCoreEventClass, kAEPrintDocuments, AEPrintDoc,0,FALSE);
    if(err)
    {
        ErrMsgCode("\pCould not install AE handler.",err);
        ExitToShell();
    }
    err = AEInstallEventHandler (kCoreEventClass, kAEQuitApplication, AEQuitApp,0,FALSE);
    if(err)
    {
        ErrMsgCode("\pCould not install AE handler.",err);
        ExitToShell();
    }

}
```

[Next](CoreSource-Document.c.md)[Previous](CoreSource-AdjustMenus.c.md)

