---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_PlayerViewController_h.html
archived_at: '2026-07-18T02:59:59.714422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](README.md.md)[Previous](AVAEMixerSample-CAAVParameterView.m.md)

# AVAEMixerSample/PlayerViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The PlayerViewController class provides specific UI Elements to interact with the PlayerNode.

                UISlider            *playerVolumeSlider;    Sets the volume on the player
                UISlider            *playerPanSlider;       Sets the pan on the player
                UIButton            *playerPlayButton;      Toggles the player state
                UISegmentedControl  *playerSegmentControl;  Provides a selection for different buffers/files
*/

#import "AudioViewController.h"

@interface PlayerViewController : AudioViewController

@end
```

[Next](README.md.md)[Previous](AVAEMixerSample-CAAVParameterView.m.md)

