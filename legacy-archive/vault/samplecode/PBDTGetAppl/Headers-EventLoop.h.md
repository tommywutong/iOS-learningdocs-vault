---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Headers_EventLoop_h.html
archived_at: '2026-07-18T03:18:19.700848Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Headers-MenuDispatch.h.md)[Previous](PBDTGetAppl.md)

# Headers/EventLoop.h

```
/*

    Global variables for Event.c

*/

extern Boolean      WNE_available;      /* true if WaitNextEvent is available */
extern Boolean      Done;               /* Set to true when the user quits                                  */
extern Boolean      KeyPressed;         /* true if user pressed a key this time through event loop          */
extern char         KeyValue;           /* the ascii character last typed                                   */
extern Boolean      BackgroundFlag;     /* true if the app is currently in the background */
```

[Next](Headers-MenuDispatch.h.md)[Previous](PBDTGetAppl.md)

