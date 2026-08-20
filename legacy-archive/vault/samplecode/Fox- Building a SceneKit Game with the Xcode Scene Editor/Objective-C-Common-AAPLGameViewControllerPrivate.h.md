---
title: 'Fox: Building a SceneKit Game with the Xcode Scene Editor'
apple_id: TP40016154
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: General
technology: SceneKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fox/Listings/Objective_C_Common_AAPLGameViewControllerPrivate_h.html
archived_at: '2026-07-18T03:08:52.621823Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox: Building a SceneKit Game with the Xcode Scene Editor](Fox-%20Building%20a%20SceneKit%20Game%20with%20the%20Xcode%20Scene%20Editor.md)


[Next](Objective-C-Common-AAPLGameControls.m.md)[Previous](Objective-C-Common-AAPLGameView.h.md)

# Objective-C/Common/AAPLGameViewControllerPrivate.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

*/

@import simd;
@import SceneKit;
@import GameController;

#import "AAPLGameViewController.h"
#import "AAPLCharacter.h"

@interface AAPLGameViewController() {
    // Nodes to manipulate the camera
    SCNNode *_cameraYHandle;
    SCNNode *_cameraXHandle;

    // The character
    AAPLCharacter *_character;

    // Game states
    BOOL _gameIsComplete;
    BOOL _lockCamera;

    SCNMaterial *_grassArea;
    SCNMaterial *_waterArea;
    NSArray<SCNNode *> *_flames;
    NSArray<SCNNode *> *_enemies;

    // Sounds
    SCNAudioSource *_collectPearlSound;
    SCNAudioSource *_collectFlowerSound;
    SCNAudioPlayer *_flameThrowerSound;
    SCNAudioSource *_victoryMusic;

    // Particles
    SCNParticleSystem *_confettiParticleSystem;
    SCNParticleSystem *_collectFlowerParticleSystem;

    NSUInteger _collectedPearlsCount;
    NSUInteger _collectedFlowersCount;

    // Collisions
    CGFloat _maxPenetrationDistance;
    SCNVector3 _replacementPosition;
    BOOL _replacementPositionIsValid;

    // For automatic camera animation
    SCNNode *_currentGround;
    SCNNode *_mainGround;
    NSMapTable<SCNNode *, NSValue *> *_groundToCameraPosition;

    // Game controls
    GCControllerDirectionPad *_controllerDPad;
    vector_float2 _controllerDirection;

#if !(TARGET_OS_IOS || TARGET_OS_TV)
    CGPoint _lastMousePosition;
#elif TARGET_OS_IOS
    UITouch *_padTouch;
    UITouch *_panningTouch;
#endif
}

- (void)panCamera:(CGPoint)direction;

@end

@interface AAPLGameViewController (GameControls) <AAPLKeyboardAndMouseEventsDelegate>

- (void)setupGameControllers;
@property(nonatomic, readonly) vector_float2 controllerDirection;

@end
```

[Next](Objective-C-Common-AAPLGameControls.m.md)[Previous](Objective-C-Common-AAPLGameView.h.md)

