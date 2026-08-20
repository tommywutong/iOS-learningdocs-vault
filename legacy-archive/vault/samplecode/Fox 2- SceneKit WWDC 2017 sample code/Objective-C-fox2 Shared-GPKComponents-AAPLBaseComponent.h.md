---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_GPKComponents_AAPLBaseComponent_h.html
archived_at: '2026-07-26T19:54:16.828526Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-UI-AAPLSlider.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLChaserComponent.m.md)

# Objective-C/fox2 Shared/GPKComponents/AAPLBaseComponent.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 GKComponent subclass that encapsulates code shared by other custom components.
 */

#import <GameplayKit/GameplayKit.h>

@interface GKAgent2D (AAPL_Scenekit)
@property matrix_float4x4 transform;
@end

@interface AAPLBaseComponent : GKComponent

@property (readonly) GKAgent2D*agent;
@property BOOL autoMoveNode;

- (void)positionAgentFromNode;
- (void)positionNodeFromAgent;
- (BOOL)isDead;

@end
```

[Next](Objective-C-fox2%20Shared-UI-AAPLSlider.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLChaserComponent.m.md)

