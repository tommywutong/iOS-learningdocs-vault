---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TAddrInet_cp.html
archived_at: '2026-07-18T03:11:58.715504Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TAddrInet.h.md)[Previous](%E2%80%A2OTClasses-TAddr.h.md)

# •OT_Classes/TAddrInet.cp

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

#include "TAddrInet.h"


// ---------------------------------------------------------------------------
//   Clone()
// ---------------------------------------------------------------------------
//  Clone
TAddr*  TAddrInet::Clone()
{
    return new TAddrInet(fAddress.fHost, fAddress.fPort);
};

// ---------------------------------------------------------------------------
//   operator==
// ---------------------------------------------------------------------------
//  Equality check

Boolean operator== (const TAddrInet& a1, const TAddrInet& a2)
{
    return (    ((a1.fAddress.fAddressType == AF_INET) && (a2.fAddress.fAddressType == AF_INET)) 
                &&(a1.fAddress.fPort == a2.fAddress.fPort) 
                && ( (a1.fAddress.fHost == a2.fAddress.fHost) 
                    || (a1.fAddress.fHost == kOTAnyInetAddress) 
                    || (a2.fAddress.fHost == kOTAnyInetAddress))) ;
};

// ---------------------------------------------------------------------------
//   operator!=
// ---------------------------------------------------------------------------
//  Non Equality check
Boolean operator!= (const TAddrInet& a1, const TAddrInet& a2)
{
    return !(    ((a1.fAddress.fAddressType == AF_INET) && (a2.fAddress.fAddressType == AF_INET)) 
                &&(a1.fAddress.fPort == a2.fAddress.fPort) 
                && ( (a1.fAddress.fHost == a2.fAddress.fHost) 
                    || (a1.fAddress.fHost == kOTAnyInetAddress) 
                    || (a2.fAddress.fHost == kOTAnyInetAddress))) ;
};

// ---------------------------------------------------------------------------
//   operator= 
// ---------------------------------------------------------------------------
//  Asignment

TAddrInet& TAddrInet::operator= ( const TAddrInet& a)
{
    fAddress.fAddressType   = a.fAddress.fAddressType;
    fAddress.fPort          = a.fAddress.fPort;
    fAddress.fHost          = a.fAddress.fHost;
    return *this;
}


//TAddrInet& TAddrInet::operator= ( const TNetbuf* n)
//{
//  InetAddress* data = (InetAddress*) n->buf;
//  fAddress = *data;
//  return *this;
//};


// ---------------------------------------------------------------------------
//   operator<<
// ---------------------------------------------------------------------------
//  Stream out
ostream &operator<< (ostream& s, const TAddrInet& a)
{
    char    buf[32];

    ::OTInetHostToString( a.fAddress.fHost, buf); 
    s << buf << " :" << a.fAddress.fPort;
    return s;
};


// ---------------------------------------------------------------------------
//   operator>>
// ---------------------------------------------------------------------------
//  Stream input



istream &operator>> (istream& s, TAddrInet& a)
{
    char    buf[32];
    s >> buf;

    a.fAddress.fAddressType = AF_INET;
    a.fAddress.fPort  =  0; // **** FIX THIS **** this to support Port Stream in..
    ::OTInetStringToHost( buf, &a.fAddress.fHost); 

    return s   ;
};
```

[Next](%E2%80%A2OTClasses-TAddrInet.h.md)[Previous](%E2%80%A2OTClasses-TAddr.h.md)

