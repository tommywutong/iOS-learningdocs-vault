---
title: CarbonInCocoa
apple_id: DTS10000381
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/CarbonInCocoa/Listings/MyController_h.html
archived_at: '2026-07-18T03:02:54.627729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CarbonInCocoa](CarbonInCocoa.md)


[Next](MyController.m.md)[Previous](main.m.md)

# MyController.h

```objc
#import <Cocoa/Cocoa.h>
#include <Carbon/Carbon.h>

@interface MyController : NSObject
{
    WindowRef   window;
    NSWindow *cocoaFromCarbonWin;
}
@end
```

[Next](MyController.m.md)[Previous](main.m.md)

