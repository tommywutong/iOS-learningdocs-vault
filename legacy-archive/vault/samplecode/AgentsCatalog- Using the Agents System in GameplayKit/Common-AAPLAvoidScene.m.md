---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLAvoidScene_m.html
archived_at: '2026-07-18T03:00:53.312094Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLFlockScene.h.md)[Previous](Common-AAPLGameScene.m.md)

# Common/AAPLAvoidScene.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Demonstrates avoid-obstacles behavior. Click (OS X) or touch (iOS) and drag and the agent follows the mouse/touch location, but avoids passing through the red obstacles.
 */

#import "AAPLAvoidScene.h"
#import "AAPLAgentNode.h"

@interface AAPLAvoidScene ()
@property AAPLAgentNode *player;
@property GKGoal *seekGoal;
@end

@implementation AAPLAvoidScene

- (NSString *)sceneName {
    return @"AVOID OBSTACLES";
}

- (void)didMoveToView:(nonnull SKView *)view {
    [super didMoveToView:view];

    // Add three obstacles in a triangle formation around the center of the scene.
    NSArray<GKObstacle *> *obstacles = @[
                                         [self addObstacleAtPoint:CGPointMake(CGRectGetMidX(self.frame),
                                                                              CGRectGetMidY(self.frame) + 150)],
                                         [self addObstacleAtPoint:CGPointMake(CGRectGetMidX(self.frame) - 200,
                                                                              CGRectGetMidY(self.frame) - 150)],
                                         [self addObstacleAtPoint:CGPointMake(CGRectGetMidX(self.frame) + 200,
                                                                              CGRectGetMidY(self.frame) - 150)],
                                         ];

    // The player agent follows the tracking agent.
    self.player = [[AAPLAgentNode alloc] initWithScene:self
                                                radius:AAPLDefaultAgentRadius
                                              position:CGPointMake(CGRectGetMidX(self.frame),
                                                                   CGRectGetMidY(self.frame))];
    self.player.agent.behavior = [[GKBehavior alloc] init];
    [self.agentSystem addComponent:self.player.agent];

    // Create the seek goal, but add it to the behavior only in -setSeeking:.
    self.seekGoal = [GKGoal goalToSeekAgent:self.trackingAgent];

    // Add an avoid-obstacles goal with a high weight to keep the agent from overlapping the obstacles.
    [self.player.agent.behavior setWeight:100 forGoal:[GKGoal goalToAvoidObstacles:obstacles maxPredictionTime:1]];
}

- (GKObstacle *)addObstacleAtPoint:(CGPoint)point {
    SKShapeNode *circleShape = [SKShapeNode shapeNodeWithCircleOfRadius:AAPLDefaultAgentRadius];
    circleShape.lineWidth = 2.5;
    circleShape.fillColor = [SKColor grayColor];
    circleShape.strokeColor = [SKColor redColor];
    circleShape.zPosition = 1;
    circleShape.position = point;
    [self addChild:circleShape];

    GKCircleObstacle *obstacle = [GKCircleObstacle obstacleWithRadius:AAPLDefaultAgentRadius];
    obstacle.position = (vector_float2){point.x, point.y};

    return obstacle;
}

- (void)setSeeking:(BOOL)seeking {
    [super setSeeking:seeking];
    // Switch between enabling seek and stop goals so that the agent stops when not seeking.
    if (seeking) {
        [self.player.agent.behavior setWeight:1 forGoal:self.seekGoal];
        [self.player.agent.behavior setWeight:0 forGoal:self.stopGoal];
    }
    else {
        [self.player.agent.behavior setWeight:0 forGoal:self.seekGoal];
        [self.player.agent.behavior setWeight:1 forGoal:self.stopGoal];
    }
}

@end
```

[Next](Common-AAPLFlockScene.h.md)[Previous](Common-AAPLGameScene.m.md)

