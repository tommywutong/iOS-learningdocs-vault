---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_AAPLCharacter_h.html
archived_at: '2026-07-26T19:54:16.756991Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-AAPLOverlay.m.md)[Previous](Objective-C-fox2%20Shared-AAPLOverlay.h.md)

# Objective-C/fox2 Shared/AAPLCharacter.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class manages the main character, including its animations, sounds and direction.
 */

@import Foundation;

@interface AAPLCharacter : NSObject

- (instancetype)initWithScene:(SCNScene*)scene;

@property(nonatomic, readonly) SCNNode *node; //the top level node of the character
@property(nonatomic, readonly) float baseAltitude; //the altitude of the character, ignoring jumps

// actions
@property(nonatomic) BOOL jump;
@property vector_float2 direction;
@property(nonatomic) BOOL burning;

// attack
- (void)attack;
- (bool)isAttacking;

// updating the character
- (void)updateAtTime:(NSTimeInterval)time withRenderer:(id <SCNSceneRenderer>)renderer;
- (void)resetCharacterPosition;

// contact with enemy
- (void)wasTouchedByEnemy;
- (void)didHitEnemy;

@property(nonatomic) SCNPhysicsWorld* physicsWorld;

// utils
+ (SCNAnimationPlayer *)loadAnimationFromSceneNamed:(NSString *)sceneName;

@end
```

[Next](Objective-C-fox2%20Shared-AAPLOverlay.m.md)[Previous](Objective-C-fox2%20Shared-AAPLOverlay.h.md)

