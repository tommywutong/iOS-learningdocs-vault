---
title: FogStyleSample
apple_id: DTS10000134
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/FogStyleSample/Listings/Headers_myevents_h.html
archived_at: '2026-07-18T03:08:47.337102Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FogStyleSample](FogStyleSample.md)


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

