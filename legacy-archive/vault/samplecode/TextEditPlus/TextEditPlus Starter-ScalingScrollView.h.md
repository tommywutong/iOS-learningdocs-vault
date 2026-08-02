---
title: TextEditPlus
apple_id: DTS10004025
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/TextEditPlus/Listings/TextEditPlus_Starter_ScalingScrollView_h.html
archived_at: '2026-07-18T03:26:33.104750Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextEditPlus](TextEditPlus.md)


[Next](TextEditPlus%20Starter-ScalingScrollView.m.md)[Previous](TextEditPlus%20Starter-Preferences.m.md)

# TextEditPlus Starter/ScalingScrollView.h

```objc
#import <Cocoa/Cocoa.h>

@class NSPopUpButton;

@interface ScalingScrollView : NSScrollView {
    NSPopUpButton *_scalePopUpButton;
    float scaleFactor;
}

- (void)scalePopUpAction:(id)sender;
- (void)setScaleFactor:(float)factor adjustPopup:(BOOL)flag;
- (float)scaleFactor;

@end
```

[Next](TextEditPlus%20Starter-ScalingScrollView.m.md)[Previous](TextEditPlus%20Starter-Preferences.m.md)

