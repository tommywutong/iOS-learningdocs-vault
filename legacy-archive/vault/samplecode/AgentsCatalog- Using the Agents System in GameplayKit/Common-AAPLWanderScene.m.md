---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLWanderScene_m.html
archived_at: '2026-07-18T03:00:53.981481Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLAlignScene.h.md)[Previous](Common-AAPLPathScene.h.md)

# Common/AAPLWanderScene.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Non-interactive demonstration of wander behavior.
 */

#import "AAPLWanderScene.h"
#import "AAPLAgentNode.h"

@implementation AAPLWanderScene

- (NSString *)sceneName {
    return @"WANDERING";
}

- (void)didMoveToView:(nonnull SKView *)view {
    [super didMoveToView:view];

    // The wanderer agent simply moves aimlessly through the scene.
    AAPLAgentNode *wanderer = [[AAPLAgentNode alloc] initWithScene:self
                                                          radius:AAPLDefaultAgentRadius
                                                        position:CGPointMake(CGRectGetMidX(self.frame),
                                                                             CGRectGetMidY(self.frame))];
    wanderer.color = [SKColor cyanColor];
    wanderer.agent.behavior = [GKBehavior behaviorWithGoal:[GKGoal goalToWander:10] weight:100];
    [self.agentSystem addComponent:wanderer.agent];
}

@end
```

[Next](Common-AAPLAlignScene.h.md)[Previous](Common-AAPLPathScene.h.md)

