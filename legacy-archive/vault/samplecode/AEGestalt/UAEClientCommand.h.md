---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UAEClientCommand_h.html
archived_at: '2026-07-18T02:59:27.502880Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UAEDocument.cp.md)[Previous](UAEClientCommand.cp.md)

# UAEClientCommand.h

```c
//  UAEClientCommand.h
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the TAEClientCommand class, the client
//  Apple event class which makes the query over the network to the server
//
//  <1>     khs     1.0     First final version


#ifndef __UAECLIENTCOMMAND__
#define __UAECLIENTCOMMAND__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif

#ifndef __UAEDOCUMENT__
#include "UAEDocument.h"
#endif


class TAEDocument;

DeclareClassDesc(TAEClientCommand);

class TAEClientCommand : public TClientCommand
{

    DeclareClass(TAEClientCommand);

public:
    TAEClientCommand();
    virtual void IAEClientCommand(CommandNumber,
                                         TAEDocument* ,
                                         AEEventID);

    virtual void ProcessReply(TAppleEvent*);

    TAEDocument* fDocument;
};

#endif
```

[Next](UAEDocument.cp.md)[Previous](UAEClientCommand.cp.md)

