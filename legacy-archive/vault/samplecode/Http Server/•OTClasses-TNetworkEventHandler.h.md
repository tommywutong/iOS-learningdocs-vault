---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkEventHandler_h.html
archived_at: '2026-07-18T03:11:59.578295Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkException.h.md)[Previous](%E2%80%A2OTClasses-TNetworkEventHandler.cp.md)

# •OT_Classes/TNetworkEventHandler.h

```c
//  TNetworkEventHandler.h - Macintosh OpenTransport network class object
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

#ifndef _H_TNETWORKEVENTHANDLER
#define _H_TNETWORKEVENTHANDLER

#include <OpenTransport.h>
#include "TNetworkEvent.h"
#include "TNetworkException.h"

//
// TNetworkEventHandler  - OpenTransport Network Event Handler class 
//
class TNetworkEventHandler : private TLink
{

//  CONSTRUCTORS AND DESTRUCTORS
public:
            TNetworkEventHandler();
    virtual ~TNetworkEventHandler();

// HIGH LEVEL FUNCTIONS
public:
            void        ProcessEvents();
            TLifo*  GetEventQueue()  { return  &fEventQueue;  };

// ABSTRACT FUNCTIONS
    virtual void    HandleEvent(TNetworkEvent* ) = 0;

// CLASS FUNCTIONS
    static  void    ScanEventHandlerQueue();

// PROTECTED FIELDS
private:
    TLifo           fEventQueue;

// CLASS VARIABLES
private:
    static  TList   fgActiveList;

};

// USEFUL MACROS

#define QUEUE_NET_EVENT(_who_, _event_, _result_, _parm_) \
                _who_->GetEventQueue()->Enqueue( new  TNetworkEvent(_event_, _result_, _parm_))

#endif
```

[Next](%E2%80%A2OTClasses-TNetworkException.h.md)[Previous](%E2%80%A2OTClasses-TNetworkEventHandler.cp.md)

