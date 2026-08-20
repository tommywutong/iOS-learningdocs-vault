---
title: MyComponentOld
apple_id: DTS10000355
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyComponentOld/Listings/MyComponentRoutines_h.html
archived_at: '2026-07-18T03:16:34.136287Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyComponentOld](MyComponentOld.md)


[Next](Document%20Revision%20History.md)[Previous](MyComponentRoutines.c.md)

# MyComponentRoutines.h

```
/*
    File:       MyComponentRoutines.h

    Contains:   simple component sample.

    Written by: John Wang   

    Copyright:  Copyright © 1994-1999 by Apple Computer, Inc., All Rights Reserved.

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

#ifdef THINK_C
#define     applec
#endif

#define     kMyProcedureSelect      1

/* ------------------------------------------------------------------------- */

pascal ComponentResult MyProcedure(Handle storage);
```

[Next](Document%20Revision%20History.md)[Previous](MyComponentRoutines.c.md)

