---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_AAPLOverlay_h.html
archived_at: '2026-07-26T19:54:16.751704Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-AAPLCharacter.h.md)[Previous](Objective-C-fox2%20Shared-AAPLCharacter.m.md)

# Objective-C/fox2 Shared/AAPLOverlay.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class manages the 2D overlay (score).
*/

@import Foundation;
@import SpriteKit;

@class AAPLControlOverlay;
@class AAPLGameController;

@interface AAPLOverlay : SKScene

- (void)setupWithController:(AAPLGameController *)controller;
- (void)layout2DOverlay;

@property (nonatomic) NSUInteger collectedGemsCount;
@property (nonatomic, readonly) AAPLControlOverlay* controlOverlay;

- (void)didCollectKey;
- (void)showEndScreen;

#if TARGET_OS_IOS
- (void)showVirtualPad;
- (void)hideVirtualPad;
#endif

@end
```

[Next](Objective-C-fox2%20Shared-AAPLCharacter.h.md)[Previous](Objective-C-fox2%20Shared-AAPLCharacter.m.md)

