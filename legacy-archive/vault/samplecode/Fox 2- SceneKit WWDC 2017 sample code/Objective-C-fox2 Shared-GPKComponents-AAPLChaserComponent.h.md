---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_GPKComponents_AAPLChaserComponent_h.html
archived_at: '2026-07-26T19:54:16.787656Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-GPKComponents-AAPLScaredComponent.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLBaseComponent.m.md)

# Objective-C/fox2 Shared/GPKComponents/AAPLChaserComponent.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is a simple behavior for enemies to chase the character when the player is detected.
 */

#import <GameplayKit/GameplayKit.h>
#import "AAPLBaseComponent.h"
#import "AAPLPlayerComponent.h"

@interface AAPLChaserComponent : AAPLBaseComponent
@property AAPLPlayerComponent *player;
@property GKInspectable float hitDistance;
@property GKInspectable float chaseDistance;
@property GKInspectable float chaseSpeed;
@property GKInspectable float wanderSpeed;
@property GKInspectable float mass;
@property GKInspectable float maxAcceleration;
@end
```

[Next](Objective-C-fox2%20Shared-GPKComponents-AAPLScaredComponent.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLBaseComponent.m.md)

