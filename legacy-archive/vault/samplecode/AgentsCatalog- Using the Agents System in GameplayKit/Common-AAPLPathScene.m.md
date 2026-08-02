---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLPathScene_m.html
archived_at: '2026-07-18T03:00:53.701274Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLFlockScene.m.md)[Previous](Common-AAPLSeparateScene.h.md)

# Common/AAPLPathScene.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Non-interactive demonstration of path-following behavior.
 */

#import "AAPLPathScene.h"
#import "AAPLAgentNode.h"

@implementation AAPLPathScene

- (NSString *)sceneName {
    return @"FOLLOW PATH";
}

- (void)didMoveToView:(nonnull SKView *)view {
    [super didMoveToView:view];

    AAPLAgentNode *follower = [[AAPLAgentNode alloc] initWithScene:self
                                                          radius:AAPLDefaultAgentRadius
                                                        position:CGPointMake(CGRectGetMidX(self.frame),
                                                                             CGRectGetMidY(self.frame))];
    follower.color = [SKColor cyanColor];

    // A closed path with a few arbitrary points relative to the center of the scene.
    vector_float2 center = { CGRectGetMidX(self.frame), CGRectGetMidY(self.frame) };
    vector_float2 points[10] = {
        { center.x, center.y + 50 },
        { center.x + 50, center.y + 150 },
        { center.x + 100, center.y + 150 },
        { center.x + 200, center.y + 200 },
        { center.x + 350, center.y + 150 },
        { center.x + 300, center.y },
        { center.x, center.y - 200 },
        { center.x - 200, center.y - 100 },
        { center.x - 200, center.y },
        { center.x - 100, center.y + 50 }
    };

    // Create a behavior that makes the agent follow along the path. 
    GKPath *path = [GKPath pathWithPoints:points count:10 radius:AAPLDefaultAgentRadius cyclical:YES];

    follower.agent.behavior = [GKBehavior behaviorWithGoal:[GKGoal goalToFollowPath:path maxPredictionTime:1.5 forward:YES] weight:1];
    [self.agentSystem addComponent:follower.agent];

    // Draw the path.
    CGPoint cgPoints[11];
    for (NSInteger i = 0; i < 10; i++){
        cgPoints[i] = CGPointMake(points[i].x, points[i].y);
    }
    cgPoints[10] = cgPoints[0]; // Repeat the last point to create a closed path.
    SKShapeNode* pathShape = [SKShapeNode shapeNodeWithPoints:cgPoints count:11];
    pathShape.lineWidth = 2;
    pathShape.strokeColor = [SKColor magentaColor];
    [self addChild:pathShape];
}

@end
```

[Next](Common-AAPLFlockScene.m.md)[Previous](Common-AAPLSeparateScene.h.md)

