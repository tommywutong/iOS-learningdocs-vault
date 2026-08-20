---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/QTSSStatusController_h.html
archived_at: '2026-07-18T03:21:18.574528Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](QTSSStatusController.m.md)[Previous](LoginWindowController.m.md)

# QTSSStatusController.h

```objc
/* QTSSStatusController */

#import <Cocoa/Cocoa.h>

@interface QTSSStatusController : NSObject
{
    id myAdminProtocolObj;
    IBOutlet NSWindow *myWindow;
    BOOL isStarted;
}

- (id)myAdminProtocolObj;
- (BOOL)isStarted;
- (void)setMyAdminProtocolObj:(id)obj;
- (void)start;

@end
```

[Next](QTSSStatusController.m.md)[Previous](LoginWindowController.m.md)

