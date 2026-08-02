---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkEventHandler_cp.html
archived_at: '2026-07-18T03:11:59.512924Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkEventHandler.h.md)[Previous](%E2%80%A2OTClasses-TNetworkEvent.h.md)

# •OT_Classes/TNetworkEventHandler.cp

```c
//  TNetworkEventHandler.cp - Macintosh OpenTransport network class object
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinne Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
// 

#include "TNetworkEventHandler.h"


// ---------------------------------------------------------------------------
//   TNetworkEventHandler::fgActiveList
// ---------------------------------------------------------------------------
//  List of active TNetworkEventHandler objects
//
TList   TNetworkEventHandler::fgActiveList; 


// ---------------------------------------------------------------------------
//   TNetworkEventHandler
// ---------------------------------------------------------------------------
//  Default Constructor

TNetworkEventHandler::TNetworkEventHandler()
{

// add this to the end list of network event handlers   
    fgActiveList.Append(this);
}

// ---------------------------------------------------------------------------
//   ~TNetworkEventHandler
// ---------------------------------------------------------------------------
//  Destructor

TNetworkEventHandler::~TNetworkEventHandler()
{
    TNetworkEvent*  aEvent;

// dispose of any outstanding events..
    while( aEvent = (TNetworkEvent*) fEventQueue.Dequeue() ) 
            delete aEvent;

// remove this from list of network event handlers  
    fgActiveList.Remove(this);

};


// ---------------------------------------------------------------------------
//   TNetworkEventHandler::ProcessAnEvent
// ---------------------------------------------------------------------------
//  Process Network Event for this handler

void TNetworkEventHandler::ProcessEvents()
{
    TNetworkEvent*  aEvent;
    TLifo       eventList;

    if(! fEventQueue.IsEmpty()){

// get head of event list
        eventList.fHead = fEventQueue.StealList();
        eventList.Reverse();

// Process each event on list   
        while( aEvent = (TNetworkEvent*) eventList.Dequeue() )
            {
                    HandleEvent(aEvent);
                    delete aEvent;
                }       
        }
}


// ---------------------------------------------------------------------------
//   TNetworkEventHandler::ScanEventHandlerQueue
// ---------------------------------------------------------------------------
//  Scan Network Event list looking for things to do

void TNetworkEventHandler::ScanEventHandlerQueue()
{
    TNetworkEventHandler *aTask;

    for (aTask =  (TNetworkEventHandler*) fgActiveList.GetFirst(); 
          aTask ;
          aTask = (TNetworkEventHandler*) aTask->Next())
        {
            aTask->ProcessEvents();
        }           

}
```

[Next](%E2%80%A2OTClasses-TNetworkEventHandler.h.md)[Previous](%E2%80%A2OTClasses-TNetworkEvent.h.md)

