---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_CAAVAudioUnitView_m.html
archived_at: '2026-07-18T02:59:58.991860Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-SequencerViewController.m.md)[Previous](AVAEMixerSample-CAAVAudioUnitView.h.md)

# AVAEMixerSample/CAAVAudioUnitView.m

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This subclass of UIView adds rounded corners to the view
*/

#import "CAAVAudioUnitView.h"
#define kRoundedCornerRadius    10

@implementation CAAVAudioUnitView

- (void)setNeedsLayout
{
    [super setNeedsLayout];

    UIBezierPath *fillPath = [UIBezierPath bezierPathWithRoundedRect: self.bounds byRoundingCorners:(UIRectCorner)(UIRectCornerAllCorners) cornerRadii:CGSizeMake(kRoundedCornerRadius, kRoundedCornerRadius)];

    CAShapeLayer *pathLayer = [[CAShapeLayer alloc] init];
    pathLayer.path = fillPath.CGPath;
    pathLayer.frame = fillPath.bounds;

    self.layer.mask = pathLayer;
}

@end
```

[Next](AVAEMixerSample-SequencerViewController.m.md)[Previous](AVAEMixerSample-CAAVAudioUnitView.h.md)

