---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/QTSSStatusView_h.html
archived_at: '2026-07-18T03:21:18.652828Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](QTSSStatusView.m.md)[Previous](QTSSStatusController.m.md)

# QTSSStatusView.h

```objc
/* QTSSStatusView */

#import <Cocoa/Cocoa.h>

@interface QTSSStatusView : NSView
{
    IBOutlet NSTextField *myCountField;
    IBOutlet NSTextField *myMaxField;
    NSMutableArray *myConnectionValues;
    NSTimer *myTimer;
    NSColor *myColor;
    id myStatusController;
}

- (NSColor *)myColor;
- (void)setMyColor:(NSColor *)color;
- (void)timerFired;

@end
```

[Next](QTSSStatusView.m.md)[Previous](QTSSStatusController.m.md)

