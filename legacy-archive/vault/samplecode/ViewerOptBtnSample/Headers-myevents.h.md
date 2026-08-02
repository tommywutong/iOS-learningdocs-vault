---
title: ViewerOptBtnSample
apple_id: DTS10000139
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerOptBtnSample/Listings/Headers_myevents_h.html
archived_at: '2026-07-18T03:28:00.780202Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerOptBtnSample](ViewerOptBtnSample.md)


[Next](Headers-MyGlobals.h.md)[Previous](Headers-misc.h.md)

# Headers/myevents.h

```c
//
// Events.h
//
#include <AppleEvents.h>

extern void HandleEvents(void);


extern  pascal OSErr MyAE_QuitApplication(AppleEvent *theAppleEvent, AppleEvent *reply,
                            SInt32 handlerRefcon);
```

[Next](Headers-MyGlobals.h.md)[Previous](Headers-misc.h.md)

