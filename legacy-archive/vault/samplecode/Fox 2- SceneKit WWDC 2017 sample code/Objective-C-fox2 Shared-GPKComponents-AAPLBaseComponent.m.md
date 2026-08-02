---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_GPKComponents_AAPLBaseComponent_m.html
archived_at: '2026-07-26T19:54:16.783420Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-GPKComponents-AAPLChaserComponent.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLPlayerComponent.h.md)

# Objective-C/fox2 Shared/GPKComponents/AAPLBaseComponent.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 GKComponent subclass that encapsulates code shared by other custom components.
 */

#import "AAPLBaseComponent.h"

#define EnemyAltitude -0.46

@implementation GKAgent2D (AAPL_Scenekit)
- (matrix_float4x4) transform {
    simd_quatf quat = simd_quaternion(-(float)(self.rotation - (M_PI/2)), simd_make_float3(0, 1, 0));
    matrix_float4x4 transform = simd_matrix4x4(quat);
    transform.columns[3] = simd_make_float4(self.position.x, EnemyAltitude, self.position.y , 1);
    return transform;
}

- (void) setTransform:(matrix_float4x4)transform {
    simd_quatf quatf = simd_quaternion(transform);
    self.rotation = - (simd_angle(quatf) + (M_PI/2));
    self.position = transform.columns[3].xz;
}

@end

@implementation AAPLBaseComponent

- (instancetype)init{
    if (self = [super init]) {
        _agent = [[GKAgent2D alloc] init];
        _autoMoveNode = YES;
    }

    return self;
}

- (BOOL)isDead
{
    return NO;
}

- (void)positionAgentFromNode
{
    GKSCNNodeComponent *nodeComponent = (GKSCNNodeComponent *)[self.entity componentForClass:GKSCNNodeComponent.class];
    SCNNode *node = nodeComponent.node;
    self.agent.transform = node.simdTransform;

}

- (void)positionNodeFromAgent
{
    GKSCNNodeComponent *nodeComponent = (GKSCNNodeComponent *)[self.entity componentForClass:GKSCNNodeComponent.class];
    SCNNode *node = nodeComponent.node;
    node.simdTransform = self.agent.transform;
}

- (void)constrainPosition
{
    simd_float2 position = self.agent.position;
    if (position.x > 2)
        position.x = 2;
    if (position.x < -2)
        position.x = -2;
    if (position.y > 12.5)
        position.y = 12.5;
    if (position.y < 8.5)
        position.y = 8.5;
    self.agent.position = position;
}

- (void)updateWithDeltaTime:(NSTimeInterval)seconds
{
    if ([self isDead]) {
        return;
    }

    [self.agent updateWithDeltaTime:seconds];
    [self constrainPosition];
    if (self.autoMoveNode)
        [self positionNodeFromAgent];
    [super updateWithDeltaTime:seconds];
}

@end
```

[Next](Objective-C-fox2%20Shared-GPKComponents-AAPLChaserComponent.h.md)[Previous](Objective-C-fox2%20Shared-GPKComponents-AAPLPlayerComponent.h.md)

