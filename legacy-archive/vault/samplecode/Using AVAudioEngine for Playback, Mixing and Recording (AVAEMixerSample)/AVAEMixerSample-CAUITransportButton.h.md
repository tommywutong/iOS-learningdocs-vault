---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_CAUITransportButton_h.html
archived_at: '2026-07-18T02:59:59.120415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-ReverbViewController.m.md)[Previous](AVAEMixerSample-AudioViewController.m.md)

# AVAEMixerSample/CAUITransportButton.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This UIButton subclass programatically draws a transport button with a particular drawing style.
         It features a fill color that can be an accent color.
         If the button has the recordEnabledButtonStyle, it pulses on and off.

         These buttons resize themselves dynamically at runtime so that their bounds is a minimum of 44 x 44 pts
         in order to make them easy to press.
         The button image will draw at the original size specified in the storyboard
*/

@import UIKit;

typedef enum {
    rewindButtonStyle = 1,
    pauseButtonStyle,
    playButtonStyle,
    recordButtonStyle,
    recordEnabledButtonStyle,
    stopButtonStyle
} CAUITransportButtonStyle;

@interface CAUITransportButton : UIButton {
    CAUITransportButtonStyle drawingStyle;
    CGColorRef fillColor;

    CGRect imageRect;
};

@property CAUITransportButtonStyle drawingStyle;
@property CGColorRef fillColor;

@end
```

[Next](AVAEMixerSample-ReverbViewController.m.md)[Previous](AVAEMixerSample-AudioViewController.m.md)

