---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_AppleEventHandler_c.html
archived_at: '2026-07-18T03:12:08.620139Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-AppleEventHandler.h.md)[Previous](Source-AboutBox.h.md)

# Source/AppleEventHandler.c

```c
/*
    File:       AppleEventHandler.c

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#include <Errors.h>

#include "AppleEventHandler.h"

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Variables

static AEEventHandlerUPP    gAppleEventHandler;

static Boolean  *gQuitFlag;

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Functions

static OSErr AppleEventHandler(const AppleEvent *inEvent, AppleEvent *outReply, UInt32 inRefCon);

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AppleEventsInit

void
AppleEventsInit(void)
{
    //¥ Install our AppleEvent dispatch routine
    gAppleEventHandler = NewAEEventHandlerProc(AppleEventHandler);
    AEInstallEventHandler(typeWildCard, typeWildCard, gAppleEventHandler, 0L, false);
}

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AppleEventsShutDown

void
AppleEventsShutDown(void)
{
    AERemoveEventHandler(typeWildCard, typeWildCard, gAppleEventHandler, false);
    DisposeRoutineDescriptor(gAppleEventHandler);
}

#pragma mark -

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AppleEventsGotRequiredParams

Boolean
AppleEventsGotRequiredParams(const AppleEvent *inEvent)
{
DescType    returnedType;
Size        actualSize;
OSErr       theErr;

    theErr = AEGetAttributePtr(inEvent, keyMissedKeywordAttr, typeWildCard, &returnedType, nil, 0,  &actualSize);

    return (errAEDescNotFound == theErr);

}


//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AppleEventsRegisterQuitFlag

void
AppleEventsRegisterQuitFlag(Boolean *inFlag)
{
    if (nil != inFlag)
        gQuitFlag = inFlag;
}

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    AppleEventHandler

static OSErr
AppleEventHandler(const AppleEvent *inEvent, AppleEvent *outReply, UInt32 inRefCon)
{
#pragma unused (outReply, inRefCon)

OSErr       theErr;
DescType    actualType;
Size        actualSize;
DescType    eventClass, eventID;

    theErr = AEGetAttributePtr(inEvent, keyEventClassAttr, typeType, &actualType, &eventClass, sizeof (eventClass), &actualSize);
    if (noErr != theErr)
        return (theErr);

    theErr = AEGetAttributePtr(inEvent, keyEventIDAttr, typeType, &actualType, &eventID, sizeof (eventID), &actualSize);
    if (noErr != theErr)
        return (theErr);

    if (eventClass == kCoreEventClass)
    {
        switch (eventID)
        {
            case kAEOpenApplication:
                return (errAEEventNotHandled);
                break;

            case kAEOpenDocuments:
                return (errAEEventNotHandled);
                break;

            case kAEPrintDocuments:
                return (errAEEventNotHandled);
                break;

            case kAEQuitApplication:
                if (AppleEventsGotRequiredParams(inEvent))
                {
                    if (nil != gQuitFlag)
                        *gQuitFlag ^= 1;

                    return (noErr);
                }
                else
                {
                    return (errAEParamMissed);
                }
                break;

            default:
                return (errAEHandlerNotFound);
        }       
    }

    return (noErr);
}
```

[Next](Source-AppleEventHandler.h.md)[Previous](Source-AboutBox.h.md)

