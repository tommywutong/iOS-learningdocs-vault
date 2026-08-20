---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkEndpointDescriptor_h.html
archived_at: '2026-07-18T03:11:59.450716Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkEvent.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEndpointDescriptor.cp.md)

# •OT_Classes/TNetworkEndpointDescriptor.h

```c
//  TNetworkEndpointDescriptor.h - Macintosh OpenTransport network Endpoint Descriptor class object
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

#ifndef _H_TNetworkEndpointDescriptor
#define _H_TNetworkEndpointDescriptor

#include <OpenTransport.h>
#include "Taddr.h"


//
// TNetworkEndpointDescriptor  - OpenTransport network Endpoint Descriptor class 
//
class TNetworkEndpointDescriptor 
{

public:

//  CONSTRUCTORS AND DESTRUCTORS
            TNetworkEndpointDescriptor():
                                fState(S_UNINIT),
                                fConfig(kOTInvalidConfigurationPtr),
                                fAddress(NULL) {};

            ~TNetworkEndpointDescriptor();

// HIGH LEVEL FUNCTIONS
public:
    void*       Stream();
    void        Unstream(void* in);

    OTResult    Validate();

    Boolean     Filter(TCall*);
    Boolean     ValidateBind(TBind*,TBind*);


// ACCESSORS
    OTConfiguration*    GetConfiguration() const;
    TAddr*              GetLocalAddress();
    char*               GetServiceName()  { return fServiceName; };


// PRIVATE FIELDS
private:
 enum EState { S_UNINIT, S_INIT } ;
    EState              fState;
    OTConfiguration*    fConfig;    
    TAddr*              fAddress;       
    char                fServiceName[255];

};


#endif
```

[Next](%E2%80%A2OTClasses-TNetworkEvent.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEndpointDescriptor.cp.md)

