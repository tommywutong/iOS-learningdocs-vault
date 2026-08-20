---
title: GetPPPStatus
apple_id: DTS10000236
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GetPPPStatus/Listings/TrapUtils_h.html
archived_at: '2026-07-18T03:10:48.279340Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GetPPPStatus](GetPPPStatus.md)


[Next](Document%20Revision%20History.md)[Previous](TrapUtils.c.md)

# TrapUtils.h

```c
/*
    File:       TrapUtils.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/22/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef TRAP_UTILS
#define TRAP_UTILS



#include <OSUtils.h>
#include <Traps.h>


pascal Boolean  TrapAvailable       (UInt16 trapWord);
pascal void *   MyGetTrapAddress    (UInt16 trapWord);
pascal void     MySetTrapAddress    (UInt16 trapWord, void *);

#endif // TRAP_UTILS
```

[Next](Document%20Revision%20History.md)[Previous](TrapUtils.c.md)

