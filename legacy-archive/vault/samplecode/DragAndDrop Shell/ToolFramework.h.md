---
title: DragAndDrop Shell
apple_id: DTS10000765
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DragAndDrop_Shell/Listings/ToolFramework_h.html
archived_at: '2026-07-18T03:07:09.563264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DragAndDrop Shell](DragAndDrop%20Shell.md)


[Next](Document%20Revision%20History.md)[Previous](ToolFramework.c.md)

# ToolFramework.h

```c
/*
    File:       ToolFramework.h

    Contains:   Simple AE framework for QuickTime related tools.

    Written by:     

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/28/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#pragma once
#include <Types.h>
#include <AppleEvents.h>
// FUNCTION PROTOTYPES
pascal void             InitMacEnvironment(long nMasters);
pascal Boolean      InitializeAppleEvents();
pascal void             MainEventLoop(void);

pascal OSErr        AEOpenHandler(AppleEvent *theMessage, AppleEvent *theReply, long refCon);
pascal OSErr        AEOpenDocHandler(AppleEvent *theMessage, AppleEvent *theReply, long refCon);
pascal OSErr        AEPrintHandler(AppleEvent *theMessage, AppleEvent *theReply, long refCon);
pascal OSErr        AEQuitHandler(AppleEvent *theMessage, AppleEvent *theReply, long refCon);

pascal OSErr        CheckForRequiredAEParams(AppleEvent *theEvent);
```

[Next](Document%20Revision%20History.md)[Previous](ToolFramework.c.md)

