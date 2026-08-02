---
title: MyRegisterComponent
apple_id: DTS10000819
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyRegisterComponent/Listings/MyComponent_h.html
archived_at: '2026-07-18T03:16:43.882266Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyRegisterComponent](MyRegisterComponent.md)


[Next](Document%20Revision%20History.md)[Previous](MyComponent.c.md)

# MyComponent.h

```
/*
    File:       MyComponent.h

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
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1
                03/14/94    JW      Re-Created for Universal Headers.

*/

#ifdef THINK_C
#define     applec
#endif

#define     kDEBUGME                0

#define     kMyComponentSpec        1L
#define     kMyComponentVersion     0L

typedef struct  {                       
    //  Component stuff
    ComponentInstance   self;                   //  self instance needed if targeted
} PrivateGlobals;

/* ------------------------------------------------------------------------- */

pascal ComponentResult MyOpen(ComponentInstance self);
pascal ComponentResult MyClose(Handle storage,ComponentInstance self);
pascal ComponentResult MyCanDo(short selector);
pascal ComponentResult MyVersion(void);
pascal ComponentResult MyRegister(Handle storage);
```

[Next](Document%20Revision%20History.md)[Previous](MyComponent.c.md)

