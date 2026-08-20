---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkEndpointDescriptor_cp.html
archived_at: '2026-07-18T03:11:59.402387Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkEndpointDescriptor.h.md)[Previous](%E2%80%A2OTClasses-TNetworkAcceptor.h.md)

# •OT_Classes/TNetworkEndpointDescriptor.cp

```c
//  TNetworkEndpointDescriptor.cp - Macintosh OpenTransport network Endpoint Descriptor class object
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

#include "TNetworkEndpointDescriptor.h"
#include "TNetworkException.h"

#include "TAddrInet.h"


// ---------------------------------------------------------------------------
//   ~TNetworkEndpointDescriptor
// ---------------------------------------------------------------------------
//  Destructor
TNetworkEndpointDescriptor::~TNetworkEndpointDescriptor()
{   
    if(fAddress) delete fAddress;               
    if(fConfig) OTDestroyConfiguration(fConfig); 
}


// ---------------------------------------------------------------------------
//   Stream
// ---------------------------------------------------------------------------
//  write out descriptor info to stream

void*  TNetworkEndpointDescriptor::Stream()
{
    return nil;
}

// ---------------------------------------------------------------------------
//   Unstream
// ---------------------------------------------------------------------------
//  read in descriptor info from stream


void   TNetworkEndpointDescriptor::Unstream(void* in)
{
// ADD REAL CODE HERE   
    ThrowIfOTInvalidConfig( fConfig  =  ::OTCreateConfiguration("tcp" ) );
    fAddress = new TAddrInet(kOTAnyInetAddress, 80);
    fState   = S_INIT;

}


// ---------------------------------------------------------------------------
//   GetConfiguration
// ---------------------------------------------------------------------------
//  Get Session Configutaration

OTConfiguration* TNetworkEndpointDescriptor::GetConfiguration() const
{
    ThrowIfOTInvalidConfig(fConfig);

    return OTCloneConfiguration( fConfig );
}



// ---------------------------------------------------------------------------
//   GetLocalAddress
// ---------------------------------------------------------------------------
//  Get Session Local Address

TAddr* TNetworkEndpointDescriptor::GetLocalAddress() 
{
    if( fState != S_INIT) ThrowMsg ("TNetworkEndpointDescriptor::GetLocalAddress - Not Initilized");
    return fAddress;
}

// ---------------------------------------------------------------------------
//   TNetworkEndpointDescriptor::Filter( call )
// ---------------------------------------------------------------------------
//  Do you want to accept this connection 

Boolean TNetworkEndpointDescriptor::Filter(TCall* callInfo)
{
    return true;
}



// ---------------------------------------------------------------------------
//   TNetworkEndpointDescriptor::ValidateBind( reqAddr, retAddr )
// ---------------------------------------------------------------------------
//  Check if bind was acceptable

Boolean TNetworkEndpointDescriptor::ValidateBind (TBind* reqAddr, TBind* retAddr)
{
    InetAddress* request = (InetAddress*) reqAddr->addr.buf;
    InetAddress* reply  =  (InetAddress*) retAddr->addr.buf;

    return ( request->fPort == reply->fPort );  ///**** FIX THIS LATER *****
}
```

[Next](%E2%80%A2OTClasses-TNetworkEndpointDescriptor.h.md)[Previous](%E2%80%A2OTClasses-TNetworkAcceptor.h.md)

