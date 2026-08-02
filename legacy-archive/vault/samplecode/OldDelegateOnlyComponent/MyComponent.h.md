---
title: OldDelegateOnlyComponent
apple_id: DTS10000331
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/OldDelegateOnlyComponent/Listings/MyComponent_h.html
archived_at: '2026-07-18T03:17:31.375085Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OldDelegateOnlyComponent](OldDelegateOnlyComponent.md)


[Next](MyComponentRoutines.c.md)[Previous](MyComponent.c.md)

# MyComponent.h

```
/*
    File:       MyComponent.h

    Contains:   simple component sample.

    Written by: John Wang

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     03/22/94    JW      Created.

    To Do:

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

[Next](MyComponentRoutines.c.md)[Previous](MyComponent.c.md)

