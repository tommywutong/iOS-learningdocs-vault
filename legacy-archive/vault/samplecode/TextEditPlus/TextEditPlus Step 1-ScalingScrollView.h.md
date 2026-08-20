---
title: TextEditPlus
apple_id: DTS10004025
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/TextEditPlus/Listings/TextEditPlus_Step_1_ScalingScrollView_h.html
archived_at: '2026-07-18T03:26:35.543587Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextEditPlus](TextEditPlus.md)


[Next](TextEditPlus%20Step%201-ScalingScrollView.m.md)[Previous](TextEditPlus%20Step%201-Preferences.m.md)

# TextEditPlus Step 1/ScalingScrollView.h

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

[Next](TextEditPlus%20Step%201-ScalingScrollView.m.md)[Previous](TextEditPlus%20Step%201-Preferences.m.md)

