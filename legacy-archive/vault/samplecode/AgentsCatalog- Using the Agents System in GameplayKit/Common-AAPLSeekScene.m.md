---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLSeekScene_m.html
archived_at: '2026-07-18T03:00:53.782537Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLFleeScene.m.md)[Previous](Common-AAPLAgentNode.m.md)

# Common/AAPLSeekScene.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Demonstrates seek behavior. Click (OS X) or touch (iOS) and drag and the agent follows the mouse/touch location.
 */

#import "AAPLSeekScene.h"
#import "AAPLAgentNode.h"

@interface AAPLSeekScene ()
@property AAPLAgentNode *player;
@property GKGoal *seekGoal;
@end

@implementation AAPLSeekScene

- (NSString *)sceneName {
    return @"SEEKING";
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

    // Create the seek goal, but add it to the behavior only in -setSeeking:.
    self.seekGoal = [GKGoal goalToSeekAgent:self.trackingAgent];
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

[Next](Common-AAPLFleeScene.m.md)[Previous](Common-AAPLAgentNode.m.md)

