---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_iOS_AAPLPadOverlay_h.html
archived_at: '2026-07-26T19:54:17.097525Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20iOS-AAPLGameViewController.m.md)[Previous](Objective-C-fox2%20iOS-main.m.md)

# Objective-C/fox2 iOS/AAPLPadOverlay.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Exposes D-Pad game controller type functionality with screen-rendered buttons.
 */

#import <SpriteKit/SpriteKit.h>

@class AAPLPadOverlay;

@protocol AAPLPadOverlayDelegate <NSObject>

- (void)padOverlayVirtualStickInteractionDidStart:(AAPLPadOverlay*)padNode;
- (void)padOverlayVirtualStickInteractionDidChange:(AAPLPadOverlay*)padNode;
- (void)padOverlayVirtualStickInteractionDidEnd:(AAPLPadOverlay*)padNode;

@end

@interface AAPLPadOverlay : SKNode

// Default 100, 100
@property (nonatomic, assign) CGSize size;
// Range [-1, 1]
@property (nonatomic, assign) CGPoint stickPosition;
@property (nonatomic, readonly) CGSize stickSize;
@property (nonatomic, weak) id<AAPLPadOverlayDelegate> delegate;

@end
```

[Next](Objective-C-fox2%20iOS-AAPLGameViewController.m.md)[Previous](Objective-C-fox2%20iOS-main.m.md)

