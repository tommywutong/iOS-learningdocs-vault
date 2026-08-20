---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Objective_C_Common_AAPLGameViewController_h.html
archived_at: '2026-07-18T03:08:52.672142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Objective-C-Common-AAPLGameViewController.m.md)[Previous](Objective-C-OSX-AAPLAppDelegate.h.md)

# Objective-C/Common/AAPLGameViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class manages most of the game logic.
*/

@import SceneKit;

#import "AAPLGameView.h"

// Collision bit masks
typedef NS_OPTIONS(NSUInteger, AAPLBitmask) {
    AAPLBitmaskCollision        = 1UL << 2,
    AAPLBitmaskCollectable      = 1UL << 3,
    AAPLBitmaskEnemy            = 1UL << 4,
    AAPLBitmaskSuperCollectable = 1UL << 5,
    AAPLBitmaskWater            = 1UL << 6
};

#if TARGET_OS_IOS || TARGET_OS_TV
typedef UIViewController AAPLViewController;
#else
typedef NSViewController AAPLViewController;
#endif

@interface AAPLGameViewController : AAPLViewController <SCNSceneRendererDelegate, SCNPhysicsContactDelegate>

@property (nonatomic, readonly) AAPLGameView *gameView;

@end
```

[Next](Objective-C-Common-AAPLGameViewController.m.md)[Previous](Objective-C-OSX-AAPLAppDelegate.h.md)

