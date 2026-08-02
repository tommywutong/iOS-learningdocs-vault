---
title: Quartz Composer WWDC 2005 TextEdit
apple_id: DTS10003654
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzComposer_WWDC_TextEdit/Listings/TextEdit_03_ScalingScrollView_h.html
archived_at: '2026-07-18T03:21:34.192533Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer WWDC 2005 TextEdit](Quartz%20Composer%20WWDC%202005%20TextEdit.md)


[Next](TextEdit03-ScalingScrollView.m.md)[Previous](TextEdit03-Preferences.m.md)

# TextEdit_03/ScalingScrollView.h

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

[Next](TextEdit03-ScalingScrollView.m.md)[Previous](TextEdit03-Preferences.m.md)

