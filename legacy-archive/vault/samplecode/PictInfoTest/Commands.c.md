---
title: PictInfoTest
apple_id: DTS10000146
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PictInfoTest/Listings/Commands_c.html
archived_at: '2026-07-18T03:18:59.976020Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PictInfoTest](PictInfoTest.md)


[Next](PictInfoTest.c.md)[Previous](main.c.md)

# Commands.c

```c
// Simple framework for Macintosh sample code
//
// Nick Thompson, DEVSUPPORT
//
// Application handlers, called by the AE stuff.  
// 
// 9/16/94  nick    first cut
//
//  Copyright:  © 1989-94 by Apple Computer, Inc., all rights reserved.

#include "AppGlobals.h"
#include "ErrorHandling.h"
#include "ShellCommands.h"

//----------------------------------------------------------------------------------//
//  Send a Quit Application Apple Event to myself to terminate this app.        

void SendQuitApp( void )
{
    AppleEvent  myAppleEvent, reply;

    //  Create the Apple Event.
    FailIfErr(AECreateAppleEvent( kCoreEventClass, 
                                  kAEQuitApplication, 
                                  &gSelfAddress,
                                  kAutoGenerateReturnID, 
                                  kAnyTransactionID, 
                                  &myAppleEvent));

    //  Send the Apple Event.
    FailIfErr(AESend( &myAppleEvent, 
                      &reply, 
                      kAENoReply+kAENeverInteract, 
                      kAENormalPriority,
                      kAEDefaultTimeout, 
                      nil, 
                      nil));

    AEDisposeDesc(&myAppleEvent);               // Dispose of the Apple Event.
} // SendQuitApp

//----------------------------------------------------------------------------------//
//  Send a Open Document Application Apple Event to myself to open a document.      

void SendOpenDoc(FSSpec *myFSSpec)
{
    AppleEvent    myAppleEvent;
    AppleEvent    defReply;
    AEDescList    docList;
    OSErr         myErr;
    OSErr         ignoreErr;

    myAppleEvent.dataHandle = nil;
    docList.dataHandle  = nil;
    defReply.dataHandle = nil;

    // Create empty list and add one file spec
    FailIfErr(AECreateList(nil,0,false, &docList));

    FailIfErr(AEPutPtr(&docList,1,typeFSS,(Ptr)myFSSpec,sizeof(FSSpec)));

    FailIfErr(AECreateAppleEvent(   kCoreEventClass,
                                    kAEOpenDocuments,
                                    &gSelfAddress,
                                    kAutoGenerateReturnID,
                                    kAnyTransactionID,
                                    &myAppleEvent));

    // Put Params into our event and send it

    FailIfErr(AEPutParamDesc( &myAppleEvent,
                              keyDirectObject,
                              &docList));

    FailIfErr(AESend( &myAppleEvent,
                      &defReply,
                      kAENoReply+kAENeverInteract,
                      kAENormalPriority,
                      kAEDefaultTimeout,
                      nil,
                      nil));


    if (myAppleEvent.dataHandle) 
        ignoreErr = AEDisposeDesc(&myAppleEvent);

    if (docList.dataHandle) 
        ignoreErr = AEDisposeDesc(&docList);

}   // SendOpenDoc 
```

[Next](PictInfoTest.c.md)[Previous](main.c.md)

