---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLGameScene_h.html
archived_at: '2026-07-18T03:00:53.561099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLSeparateScene.h.md)[Previous](Common-AAPLSeekScene.h.md)

# Common/AAPLGameScene.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Common superclass for the scenes in this demo. Manages an update loop for agents, and provides a mouse/touch tracking agent for use in some of the demo scenes.
 */

@import SpriteKit;
@import GameplayKit;

typedef NS_ENUM(NSInteger, AAPLSceneType) {
    AAPLSceneTypeSeek = 0,
    AAPLSceneTypeWander,
    AAPLSceneTypeFlee,
    AAPLSceneTypeAvoid,
    AAPLSceneTypeSeparate,
    AAPLSceneTypeAlign,
    AAPLSceneTypeFlock,
    AAPLSceneTypePath,

    AAPLSceneTypesCount
};

const static float AAPLDefaultAgentRadius = 40.0f;

@interface AAPLGameScene : SKScene

+ (AAPLGameScene *)sceneWithType:(AAPLSceneType)sceneType size:(CGSize)size;

@property (nonatomic, readonly) NSString *sceneName;

// A component system to manage per-frame updates for all agents.
@property (nonatomic, readonly) GKComponentSystem *agentSystem;

// An agent whose position tracks that of mouseDragged (OS X) or touchesMoved (iOS) events.
// This agent has no display representation, but can be used to make other agents follow the mouse/touch.
@property (nonatomic, readonly) GKAgent2D *trackingAgent;

// YES when the mouse is dragging (OS X) or a touch is moving
@property (nonatomic, getter=isSeeking) BOOL seeking;

@property (nonatomic, readonly) GKGoal *stopGoal;

@end
```

[Next](Common-AAPLSeparateScene.h.md)[Previous](Common-AAPLSeekScene.h.md)

