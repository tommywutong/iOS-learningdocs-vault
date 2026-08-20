---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_HTTP_Server_THTTPServer_h.html
archived_at: '2026-07-18T03:11:58.175441Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2MacClasses-TBackGroundApp.cp.md)[Previous](%E2%80%A2HTTP%20Server-THTTPServer.cp.md)

# •HTTP Server/THTTPServer.h

```c
//  THTTPServer.h - Macintosh OpenTransport Network HTTP Server class object
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

#ifndef _H_THTTPSERVER
#define _H_THTTPSERVER

#include "TNetworkServerApp.h"
#include "TNetworkAcceptor.h"

//
// THTTPServer  - OpenTransport HTTP Acceptor class 
//
class THTTPServer : public TNetworkAcceptor
{
//  CONSTRUCTORS AND DESTRUCTORS
public:
            THTTPServer();
    virtual ~THTTPServer();

// HIGH LEVEL FUNCTIONS
public:
    virtual TNetworkSession* SessionFactory();

};

//
// THTTPSession  - OpenTransport HTTP Session class 
//
class THTTPSession : public TNetworkSession
{
//  CONSTRUCTORS AND DESTRUCTORS
public:
             THTTPSession(THTTPServer*);
    virtual ~THTTPSession();

// HIGH LEVEL FUNCTIONS
public:
    virtual void*   Run();          // thread task
};



//
// THTTPServerApp  - Macintosh OpenTransport Network HTTP Server Application class object
//
class THTTPServerApp : public TNetworkServerApp
{

//  CONSTRUCTORS AND DESTRUCTORS
public:
             THTTPServerApp();
    virtual ~THTTPServerApp();

// HIGH LEVEL FUNCTIONS
public:
    virtual void Start();           // start the application and let it run

// PRIVATE FIELDS
private:
    THTTPServer*    fServer;
    TNetworkEndpointDescriptor fDescriptor;
};


#endif
```

[Next](%E2%80%A2MacClasses-TBackGroundApp.cp.md)[Previous](%E2%80%A2HTTP%20Server-THTTPServer.cp.md)

