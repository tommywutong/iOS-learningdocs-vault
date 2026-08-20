---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkSession_h.html
archived_at: '2026-07-18T03:12:00.052807Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkStream.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkSession.cp.md)

# •OT_Classes/TNetworkSession.h

```c
//  TNetworkSession.h - Macintosh OpenTransport Network Session class object
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

#ifndef _H_TNetworkSession
#define _H_TNetworkSession

#include "TNetworkEventHandler.h"
#include "TNetworkStream.h"
#include "TThread.h"        

class  TNetworkAcceptor;

// Local Prototypes

//
// TNetworkSession  - OpenTransport Network Session class 
//
class TNetworkSession : public TLink, TNetworkEventHandler, public TThread 
{
//  CONSTRUCTORS AND DESTRUCTORS
public:
                     TNetworkSession(TNetworkAcceptor*);
    virtual ~TNetworkSession();

// CALLBACKS        
protected:
//      virtual void*   Run();

// ACCESSORS
public:
        EndpointRef     GetEndpoint()        { return fEndPoint; };
        TCall*              GetCallInfo()        { return &fCallInfo; };
        TDiscon*            GetDisconInfo()  { return &fDisconInfo; };
TNetworkIOStream&   GetStreamRef()   { return fioStream; };

// FUNCTIONS FROM TThread
private:
    void Done();

// FUNCTIONS FROM TNetworkEventHandler
private:
    void    HandleEvent(TNetworkEvent* );

// EVENT MANGEMENT FUNCTIONS
private:
    void EventOpenComplete          (TNetworkEvent* );
    void EventPassCon                   (TNetworkEvent* );
    void EventDisconnect                (TNetworkEvent* );
    void EventOrdRelease            (TNetworkEvent* );
    void EventDisconnectComplete(TNetworkEvent* );
    void EventUnbindComplete    (TNetworkEvent* );
    void EventExDataAvail               (TNetworkEvent* );
    void EventMemoryReleased        (TNetworkEvent* );
    void EventOther                         (TNetworkEvent* );      // Debug event
    void EventDataAvail                 (TNetworkEvent* = nil); 

// OPEN TRANSPORT CALLBACK
    static pascal void NotifyProc (TNetworkSession* , OTEventCode , OTResult , void* );

// PROTECTED FIELDS
protected:
    EndpointRef             fEndPoint;                  // Endpoint ref
    TEndpointInfo           fInfo;                          // Endpoint information
    TNetworkIOStream    fioStream;
    TNetworkAcceptor*   fServer;                        // back pointer to server info
    ThreadTaskRef           fThreadTaskRef;         // thread task ref
    TCall                       fCallInfo;
    TDiscon                     fDisconInfo;
    UInt8*                      fData;
};


#endif
```

[Next](%E2%80%A2OTClasses-TNetworkStream.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkSession.cp.md)

