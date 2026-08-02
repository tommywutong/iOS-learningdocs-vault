---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkServerApp_cp.html
archived_at: '2026-07-18T03:11:59.778583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkServerApp.h.md)[Previous](%E2%80%A2OTClasses-TNetworkException.h.md)

# •OT_Classes/TNetworkServerApp.cp

```c
//  TNetworkServerApp.cp - Macintosh OpenTransport Network Server Application class object
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

#include "TNetworkServerApp.h"
#include "TNetworkEventHandler.h"
#include "TThread.h"

// ---------------------------------------------------------------------------
//   TNetworkServerApp
// ---------------------------------------------------------------------------
//  Default Constructor

TNetworkServerApp::TNetworkServerApp()
{
    ThrowIfOTErr( ::InitOpenTransport());
    fSleepTime =    kNoSleep;       // network task doesnt sleep
}

// ---------------------------------------------------------------------------
//   ~TNetworkServerApp
// ---------------------------------------------------------------------------
//  Destructor

TNetworkServerApp::~TNetworkServerApp()
{
};


// ---------------------------------------------------------------------------
//   TNetworkServerApp::Start()
// ---------------------------------------------------------------------------
//  

void TNetworkServerApp::Start()
{
// handle any specific startup issues.      

    TBackGroundApp::Start();        // call the inherited Start
}


// ---------------------------------------------------------------------------
//   TNetworkServerApp::DoIdle()
// ---------------------------------------------------------------------------
// process any network events   durring idle time   

void TNetworkServerApp::DoIdle()
{
    TNetworkEventHandler::ScanEventHandlerQueue();
    TThread::Yield();
}
```

[Next](%E2%80%A2OTClasses-TNetworkServerApp.h.md)[Previous](%E2%80%A2OTClasses-TNetworkException.h.md)

