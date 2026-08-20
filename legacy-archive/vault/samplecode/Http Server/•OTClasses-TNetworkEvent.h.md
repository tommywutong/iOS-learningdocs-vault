---
title: Http Server
apple_id: DTS10000238
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Http_Server/Listings/_OT_Classes_TNetworkEvent_h.html
archived_at: '2026-07-18T03:11:59.685116Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Http Server](Http%20Server.md)


[Next](%E2%80%A2OTClasses-TNetworkEventHandler.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEvent.cp.md)

# •OT_Classes/TNetworkEvent.h

```c
//  TNetworkEvent.h - Macintosh OpenTransport network class object
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

#ifndef _H_TNETWORKEVENT
#define _H_TNETWORKEVENT

#include <OSUtils.h>
#include <OpenTransport.h>
#include "TList.h"
#include "TCachedStorage.h"

//
// TNetworkEvent  - OpenTransport Network Event Base class 
//
class TNetworkEvent  : public TLink, TCachedStorage<TNetworkEvent>
{

public:
//  CONSTRUCTORS 
    TNetworkEvent (OTEventCode theEvent,  OTResult theResult, void* theParam):
                    fEvent (theEvent),
                    fResult(theResult),
                    fParam (theParam)
                        { ::OTGetTimeStamp(&fTime); };
// PRIVATE FIELDS
public:
    const OTEventCode   fEvent;
    const OTResult      fResult;
    const void*             fParam;
                OTTimeStamp fTime;


};


#endif
```

[Next](%E2%80%A2OTClasses-TNetworkEventHandler.cp.md)[Previous](%E2%80%A2OTClasses-TNetworkEvent.cp.md)

