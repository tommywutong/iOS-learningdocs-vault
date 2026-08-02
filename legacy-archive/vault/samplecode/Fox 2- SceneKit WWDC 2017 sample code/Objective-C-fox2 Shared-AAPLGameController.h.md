---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_AAPLGameController_h.html
archived_at: '2026-07-26T19:54:16.698720Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-AAPLCharacter.m.md)[Previous](Objective-C-fox2%20macOS-main.m.md)

# Objective-C/fox2 Shared/AAPLGameController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class serves as the app's source of control flow.
 */

#import <SceneKit/SceneKit.h>

#if TARGET_OS_IPHONE
#import "AAPLPadOverlay.h"
#import "AAPLButtonOverlay.h"
#endif
#import "AAPLMenu.h"

#if TARGET_OS_IOS
@class AAPLControlOverlay;
#endif

// Collision bit masks
typedef NS_OPTIONS(NSUInteger, AAPLBitmask) {
    AAPLBitmaskCharacter        = 1UL << 0, // the main character
    AAPLBitmaskCollision        = 1UL << 1, // the ground and walls
    AAPLBitmaskEnemy            = 1UL << 2, // the enemies
    AAPLBitmaskTrigger          = 1UL << 3, // the box that triggers camera changes and other actions
    AAPLBitmaskCollectable      = 1UL << 4, // the collectables (gems and key)
};

#if TARGET_OS_IPHONE
@interface AAPLGameController : NSObject <SCNSceneRendererDelegate, AAPLMenuDelegate, AAPLPadOverlayDelegate, AAPLButtonOverlayDelegate>
#else
@interface AAPLGameController : NSObject <SCNSceneRendererDelegate, AAPLMenuDelegate>
#endif

- (instancetype)initWithSCNView:(SCNView *)view;

@property (strong, readonly) SCNScene *scene;
@property (strong, readonly) id <SCNSceneRenderer> sceneRenderer;

// reset the game
- (void)resetPlayerPosition;

// the character and camera direction driven by the controller
@property vector_float2 characterDirection;
@property vector_float2 cameraDirection;

// actions driven by the controller
- (void)controllerJump:(BOOL)jump;
- (void)controllerAttack;

@end
```

[Next](Objective-C-fox2%20Shared-AAPLCharacter.m.md)[Previous](Objective-C-fox2%20macOS-main.m.md)

