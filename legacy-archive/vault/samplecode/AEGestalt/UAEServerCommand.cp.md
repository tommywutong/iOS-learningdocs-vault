---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UAEServerCommand_cp.html
archived_at: '2026-07-18T02:59:27.785843Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UAEServerCommand.h.md)[Previous](UAEGestalt.h.md)

# UAEServerCommand.cp

```c
//  Copyright © 1991-92 Apple Computer, Inc. All rights reserved.
//  UAEServerCommand.cp
//  Kent Sandvik DTS
//  This file contains the TAEServer member functions, for serving
//  incoming Apple events.
//
//  <1>     khs     1.0     First final version


#ifndef __UAESERVERCOMMAND__
#include "UAEServerCommand.h"
#endif


//  Empty constructor - for avoiding ptabs in global data space

#undef Inherited
#define Inherited TServerCommand

#pragma segment ARes
DefineClass(TAEServerCommand, TServerCommand);

TAEServerCommand::TAEServerCommand()
{
}


//  Process the incoming client AppleEvent, and return the needed information,
//  in our case the gConfiguration structure resident in memory.
#pragma segment ADoCommand
void TAEServerCommand::DoIt()
{
    fReply->WriteParameterPtr(kAEConfig, typeConfig, (Ptr) & gConfiguration, sizeof(gConfiguration));
    fReply->Send();
}
```

[Next](UAEServerCommand.h.md)[Previous](UAEGestalt.h.md)

