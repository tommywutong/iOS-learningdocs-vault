---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLSeparateScene_m.html
archived_at: '2026-07-18T03:00:53.878675Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLWanderScene.h.md)[Previous](Common-AAPLAvoidScene.h.md)

# Common/AAPLSeparateScene.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Demonstrates separation behavior. Click (OS X) or touch (iOS) and drag; the white agent follows the mouse/touch location, and the cyan agents attempt to maintain distance from the white agent.
 */

#import "AAPLSeparateScene.h"
#import "AAPLAgentNode.h"

@interface AAPLSeparateScene ()
@property AAPLAgentNode *player;
@property NSArray<AAPLAgentNode *> *friends;
@property GKGoal *separateGoal;
@property GKGoal *seekGoal;
@end

@implementation AAPLSeparateScene

- (NSString *)sceneName {
    return @"SEPARATION";
}

- (void)didMoveToView:(nonnull SKView *)view {
    [super didMoveToView:view];

    // The player agent follows the tracking agent.
    self.player = [[AAPLAgentNode alloc] initWithScene:self
                                            radius:AAPLDefaultAgentRadius
                                          position:CGPointMake(CGRectGetMidX(self.frame),
                                                               CGRectGetMidY(self.frame))];

    self.player.agent.behavior = [[GKBehavior alloc] init];
    [self.agentSystem addComponent:self.player.agent];
    self.player.agent.maxSpeed *= 1.2;

    // Create the seek goal, but add it to the behavior only in -setSeeking:.
    self.seekGoal = [GKGoal goalToSeekAgent:self.trackingAgent];

    // The friend agents attempt to maintain consistent separation from the player agent.
    self.friends = @[
        [self addFriendAtPoint:CGPointMake(CGRectGetMidX(self.frame) - 150, CGRectGetMidY(self.frame))],
        [self addFriendAtPoint:CGPointMake(CGRectGetMidX(self.frame) + 150, CGRectGetMidY(self.frame))],
    ];
    self.separateGoal = [GKGoal goalToSeparateFromAgents:@[self.player.agent] maxDistance:100 maxAngle:M_PI*2];
    GKBehavior *behavior = [GKBehavior behaviorWithGoal:self.separateGoal weight:100];
    for (AAPLAgentNode *friend in self.friends) {
        friend.agent.behavior = behavior;
    }
}

- (AAPLAgentNode *)addFriendAtPoint:(CGPoint)point {
    AAPLAgentNode *friend = [[AAPLAgentNode alloc] initWithScene:self
                                                          radius:AAPLDefaultAgentRadius
                                                        position:point];
    friend.color = [SKColor cyanColor];
    [self.agentSystem addComponent:friend.agent];
    return friend;
}

- (void)setSeeking:(BOOL)seeking {
    [super setSeeking:seeking];
    // Switch between enabling seek and stop goals so that the agents stop when not seeking.
    for (GKAgent2D *agent in self.agentSystem) {
        if (seeking) {
            [agent.behavior setWeight:1 forGoal:self.seekGoal];
            [agent.behavior setWeight:0 forGoal:self.stopGoal];
        }
        else {
            [agent.behavior setWeight:0 forGoal:self.seekGoal];
            [agent.behavior setWeight:1 forGoal:self.stopGoal];
        }
    }
}

@end
```

[Next](Common-AAPLWanderScene.h.md)[Previous](Common-AAPLAvoidScene.h.md)

