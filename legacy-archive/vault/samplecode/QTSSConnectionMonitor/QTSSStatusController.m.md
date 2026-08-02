---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/QTSSStatusController_m.html
archived_at: '2026-07-18T03:21:18.606038Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](QTSSStatusView.h.md)[Previous](QTSSStatusController.h.md)

# QTSSStatusController.m

```objc
#import "QTSSStatusController.h"
#import "QTSSStatusView.h"

@implementation QTSSStatusController

- (void)awakeFromNib
{
    isStarted = NO;
}

- (id)myAdminProtocolObj
{
    return myAdminProtocolObj;
}

- (BOOL)isStarted
{
    return isStarted;
}

- (void)setMyAdminProtocolObj:(id)obj
{
    [obj retain];
    if (myAdminProtocolObj)
        [myAdminProtocolObj release];
    myAdminProtocolObj = obj;
}

- (void)start
{
    [myWindow makeKeyAndOrderFront:self];
    isStarted = YES;
}

- (void)dealloc
{
    if (myAdminProtocolObj)
        [myAdminProtocolObj release];
}

@end
```

[Next](QTSSStatusView.h.md)[Previous](QTSSStatusController.h.md)

