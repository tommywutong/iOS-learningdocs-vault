---
title: DelegateOnlyComponentOld
apple_id: DTS10000354
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/DelegateOnlyComponentOld/Listings/MyComponent_h.html
archived_at: '2026-07-18T03:06:14.947672Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DelegateOnlyComponentOld](DelegateOnlyComponentOld.md)


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
                7/28/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifdef THINK_C
#define     applec
#endif

#define     kDEBUGME                0

#define     kMyComponentSpec        1L
#define     kMyComponentVersion     0L

typedef struct  {                       
    //  Component stuff
    ComponentInstance   delegate;               //  keep track who we are delegating it to.
    ComponentInstance   self;                   //  self instance needed by MediaInitialize

    //  Characteristics
    WindowPtr           backWindow;
    CGrafPtr            moviePort;
    short               windowKind;

    Boolean             fadeStatus;
    Handle              handleBarStorage;
    Boolean             mcVisible;
    Boolean             mcAttached;
    Boolean             firstTime;
} PrivateGlobals;

/* ------------------------------------------------------------------------- */

pascal ComponentResult MyOpen(ComponentInstance self);
pascal ComponentResult MyClose(Handle storage,ComponentInstance self);
pascal ComponentResult MyCanDo(short selector);
pascal ComponentResult MyVersion(void);
pascal ComponentResult MyRegister(void );
pascal ComponentResult MyTarget(Handle storage, ComponentInstance self);
```

[Next](Document%20Revision%20History.md)[Previous](MyComponent.c.md)

