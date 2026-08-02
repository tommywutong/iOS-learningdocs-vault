---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UAEServerCommand_h.html
archived_at: '2026-07-18T02:59:27.840297Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UGrayFillAdorner.cp.md)[Previous](UAEServerCommand.cp.md)

# UAEServerCommand.h

```c
//  UAEServerCommand.h
//  Copyright © 1991-92 Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the TAEServerCommand class, used to
//  serve the incoming Apple event with needed information
//
//  <1>     khs     1.0     First final version


#ifndef __UAESERVERCOMMAND__
#define __UAESERVERCOMMAND__

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"
#endif

DeclareClassDesc(TAEServerCommand);

class TAEServerCommand : public TServerCommand
{

    DeclareClass(TAEServerCommand);

public:
    TAEServerCommand();
    virtual void DoIt();
};

#endif 
```

[Next](UGrayFillAdorner.cp.md)[Previous](UAEServerCommand.cp.md)

