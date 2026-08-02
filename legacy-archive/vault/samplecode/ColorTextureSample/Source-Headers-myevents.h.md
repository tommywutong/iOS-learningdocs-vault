---
title: ColorTextureSample
apple_id: DTS10000131
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorTextureSample/Listings/Source_Headers_myevents_h.html
archived_at: '2026-07-18T03:04:02.489290Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorTextureSample](ColorTextureSample.md)


[Next](Source-Headers-MyGlobals.h.md)[Previous](Source-Headers-misc.h.md)

# Source/Headers/myevents.h

```c
//
// Events.h
//

#include <Events.h>
#include <AEDataModel.h>

extern void HandleEvents(void);
extern void HandleMouseDown(void);
extern void HandleNullEvent(void);
extern void HandleKeyDown(char);


extern  pascal OSErr MyAE_QuitApplication(AppleEvent *theAppleEvent, AppleEvent *reply,
                            SInt32 handlerRefcon);
```

[Next](Source-Headers-MyGlobals.h.md)[Previous](Source-Headers-misc.h.md)

