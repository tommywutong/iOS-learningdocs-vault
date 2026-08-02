---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TAddr_cp.html
archived_at: '2026-07-18T03:11:58.851710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TAddr.h.md)[Previous](%E2%80%A2MacClasses-TThread.h.md)

# •OT_Classes/TAddr.cp

```c
//  TAddrInet.cp - Macintosh OpenTransport network "address family independent" class object
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

#include "TAddr.h"
#include "TAddrInet.h"


// ---------------------------------------------------------------------------
//   TAddr::Factory( Type )
// ---------------------------------------------------------------------------
//  create an address of type

TAddr* TAddr::Factory(OTAddressType type)
{
    switch(type)
    {
        case AF_INET: 
            return new TAddrInet();

        default:
            return nil;
    }

};


// ---------------------------------------------------------------------------
//   TAddr::Factory( TNetbuf )
// ---------------------------------------------------------------------------
//  create an address from Netbuf

TAddr* TAddr::Factory(TNetbuf* n)
{
    OTAddress* addr = (OTAddress*) n->buf;

    switch(addr->fAddressType)
    {
        case AF_INET: 
            InetAddress* Iaddr = (InetAddress*) n->buf;
            return new TAddrInet(Iaddr->fHost,Iaddr->fPort);

        default:
            return nil;
    }

};


// ---------------------------------------------------------------------------
//   TAddr::TaddrToNetbuf( TNetbuf* )
// ---------------------------------------------------------------------------
//  convert an address to Netbuf

void  TAddr::ToNetbuf(TNetbuf* n)
{
    n->buf      =  (UInt8*) this->GetAddr();
    n->len      = this->GetSize();
    n->maxlen   = this->GetMaxSize();
}
```

[Next](%E2%80%A2OTClasses-TAddr.h.md)[Previous](%E2%80%A2MacClasses-TThread.h.md)

