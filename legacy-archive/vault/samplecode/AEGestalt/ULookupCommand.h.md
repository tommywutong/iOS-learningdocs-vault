---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/ULookupCommand_h.html
archived_at: '2026-07-18T02:59:28.267775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](Document%20Revision%20History.md)[Previous](ULookupCommand.cp.md)

# ULookupCommand.h

```c
//  ULookupCommand.h
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the class for TLookup command, used for
//  doing the query over the network
//
//  <1>     khs     1.0     First final version


#ifndef __ULOOKUPCOMMAND__
#define __ULOOKUPCOMMAND__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif

#ifndef __UAEDOCUMENT__
#include "UAEDocument.h"
#endif

class TAEDocument;

DeclareClassDesc(TLookupCommand);

class TLookupCommand : public TCommand
{

    DeclareClass(TLookupCommand);

public:
    TLookupCommand();
    virtual void ILookupCommand(CommandNumber,
                                       TAEDocument*);
    virtual void DoIt();

    TAEDocument* fDocument;
};

#endif
```

[Next](Document%20Revision%20History.md)[Previous](ULookupCommand.cp.md)

