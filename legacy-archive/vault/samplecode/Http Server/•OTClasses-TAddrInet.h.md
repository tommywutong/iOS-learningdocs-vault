---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TAddrInet_h.html
archived_at: '2026-07-18T03:11:58.773259Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TCachedStorage.cp.md)[Previous](%E2%80%A2OTClasses-TAddrInet.cp.md)

# •OT_Classes/TAddrInet.h

```c
//  TAddrInet.h - Macintosh OpenTransport network "address family independent" class object
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

#ifndef _H_TAddrInet
#define _H_TAddrInet

#include <OpenTptInternet.h>   
#include "TAddr.h"

//
// TAddrInet.h - "address family independent" class object
//
class TAddrInet : public TAddr
{

public:
//  CONSTRUCTORS AND DESTRUCTORS

    TAddrInet() {
             fAddress.fAddressType  = AF_INET;
             fAddress.fPort         = 0;
             fAddress.fHost         = kOTAnyInetAddress;
             };

    TAddrInet(InetPort thePort) {
             fAddress.fAddressType  = AF_INET;
             fAddress.fPort         = thePort;
             fAddress.fHost         = kOTAnyInetAddress;
             };

    TAddrInet(InetHost theHost, InetPort thePort){
             fAddress.fAddressType  = AF_INET;
             fAddress.fPort         = thePort;
             fAddress.fHost         = theHost;
             };

    TAddrInet(TNetbuf *theBuf) {
            InetAddress* data = (InetAddress*) theBuf->buf;
            fAddress = *data;
            };

public:
// ACCESSORS 
  size_t            GetMaxSize (void) const { return sizeof(InetAddress); }
  size_t            GetSize (void) const { return sizeof(InetAddress); }
  OTAddressType     GetType (void) const { return AF_INET; };
  OTAddress*        GetAddr (void) const { return (OTAddress*) &fAddress; };

// Equality/inequality tests
    friend Boolean operator== (const TAddrInet& a1, const TAddrInet& a2);
    friend Boolean operator!= (const TAddrInet& a1, const TAddrInet& a2);

// Assignment
    TAddrInet& operator= ( const TAddrInet& a);
//  TAddrInet& operator= ( const TNetbuf& n);

// Stream functions
    friend ostream &operator<< (ostream& s, const TAddrInet& a);
    friend istream &operator>> (istream& s, TAddrInet& a);

//  High Level functions
    virtual TAddr*  Clone();

// PRIVATE FIELDS
protected:
    InetAddress fAddress;
};


#endif
```

[Next](%E2%80%A2OTClasses-TCachedStorage.cp.md)[Previous](%E2%80%A2OTClasses-TAddrInet.cp.md)

