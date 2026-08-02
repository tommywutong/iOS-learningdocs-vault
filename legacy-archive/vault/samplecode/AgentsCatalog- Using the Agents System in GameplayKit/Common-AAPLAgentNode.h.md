---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLAgentNode_h.html
archived_at: '2026-07-18T03:00:53.071918Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](README.md.md)[Previous](Common-AAPLFlockScene.m.md)

# Common/AAPLAgentNode.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A SpriteKit node whose position is managed by a GameplayKit agent. Also provides the standard appearance for agents in this demo.
 */

@import SpriteKit;
@import GameplayKit;

@interface AAPLAgentNode : SKNode <GKAgentDelegate>

- (instancetype)initWithScene:(SKScene *)scene radius:(float)radius position:(CGPoint)position;

@property (readonly) GKAgent2D *agent;
@property (nonatomic, readwrite) SKColor *color;
@property (nonatomic) BOOL drawsTrail;

@end
```

[Next](README.md.md)[Previous](Common-AAPLFlockScene.m.md)

