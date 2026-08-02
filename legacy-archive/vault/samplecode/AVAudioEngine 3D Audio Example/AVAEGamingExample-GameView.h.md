---
title: AVAudioEngine 3D Audio Example
apple_id: TP40015163
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEGamingExample/Listings/AVAEGamingExample_GameView_h.html
archived_at: '2026-07-18T02:59:57.695855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVAudioEngine 3D Audio Example](AVAudioEngine%203D%20Audio%20Example.md)


[Next](AVAEGamingExample-GameView.m.md)[Previous](AVAEGamingExample-GameViewController.m.md)

# AVAEGamingExample/GameView.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    GameView
*/

@import SceneKit;

@class AudioEngine;

@interface GameView : SCNView

@property (strong) AudioEngine *gameAudioEngine;

@end
```

[Next](AVAEGamingExample-GameView.m.md)[Previous](AVAEGamingExample-GameViewController.m.md)

