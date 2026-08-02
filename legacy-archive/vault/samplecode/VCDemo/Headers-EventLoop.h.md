---
title: VCDemo
apple_id: DTS10000128
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VCDemo/Listings/Headers_EventLoop_h.html
archived_at: '2026-07-18T03:27:40.134992Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VCDemo](VCDemo.md)


[Next](Headers-MenuDispatch.h.md)[Previous](VCDemo.md)

# Headers/EventLoop.h

```c
/*
    EventLoop.h

    Global variables

    © 1995 Apple Computer, Inc.
*/

#include "QD3DViewer.h"

enum
{
    kContainerFull,
    kContainerInsetView,
    kContainerFourView
};

typedef struct TVCDemoData
{
    int             containerStyle;
    TQ3ViewerObject viewer1;    
    TQ3ViewerObject viewer2;    
    TQ3ViewerObject viewer3;    
    TQ3ViewerObject viewer4;    
} TVCDemoData, *TVCDemoDataPtr, **TVCDemoDataHdl;

extern Boolean      WNE_available;      /* true if WaitNextEvent is available */
extern Boolean      Done;               /* Set to true when the user quits                                  */
extern Boolean      KeyPressed;         /* true if user pressed a key this time through event loop          */
extern char         KeyValue;           /* the ascii character last typed                                   */
extern Boolean      BackgroundFlag;     /* true if the app is currently in the background */

/* EOF */
```

[Next](Headers-MenuDispatch.h.md)[Previous](VCDemo.md)

