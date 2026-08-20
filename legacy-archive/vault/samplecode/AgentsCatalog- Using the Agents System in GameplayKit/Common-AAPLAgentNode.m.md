---
title: 'AgentsCatalog: Using the Agents System in GameplayKit'
apple_id: TP40016141
resource_type: Sample Code
platform: iOS|macOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Listings/Common_AAPLAgentNode_m.html
archived_at: '2026-07-18T03:00:53.102600Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AgentsCatalog: Using the Agents System in GameplayKit](AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md)


[Next](Common-AAPLSeekScene.m.md)[Previous](Common-AAPLFleeScene.h.md)

# Common/AAPLAgentNode.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A SpriteKit node whose position is managed by a GameplayKit agent. Also provides the standard appearance for agents in this demo.
 */

#import "AAPLAgentNode.h"

@interface AAPLAgentNode ()
@property SKShapeNode *triangleShape;
@property SKEmitterNode *particles;
@property CGFloat defaultParticleRate;
@end

@implementation AAPLAgentNode

#pragma mark - Initialization

- (instancetype)initWithScene:(SKScene *)scene radius:(float)radius position:(CGPoint)position {
    self = [super init];

    if (self) {
        self.position = position;
        self.zPosition = 10;
        [scene addChild:self];

        // An agent to manage the movement of this node in a scene.
        _agent = [[GKAgent2D alloc] init];
        _agent.radius = radius;
        _agent.position = (vector_float2){position.x, position.y};
        _agent.delegate = self;
        _agent.maxSpeed = 100;
        _agent.maxAcceleration = 50;

        // A circle to represent the agent's radius in the agent simulation.
        SKShapeNode *circleShape = [SKShapeNode shapeNodeWithCircleOfRadius:radius];
        circleShape.lineWidth = 2.5;
        circleShape.fillColor = [SKColor grayColor];
        circleShape.zPosition = 1;
        [self addChild:circleShape];

        // A triangle to represent the agent's heading (rotation) in the agent simulation.
        CGPoint points[4];
        const static float triangleBackSideAngle = (135.0f / 360.0f) * (2 * M_PI);
        points[0] = CGPointMake(radius,0); // Tip.
        points[1] = CGPointMake(radius * cos(triangleBackSideAngle), radius * sin(triangleBackSideAngle)); // Back bottom.
        points[2] = CGPointMake(radius * cos(triangleBackSideAngle), -radius * sin(triangleBackSideAngle)); // Back top.
        points[3] = CGPointMake(radius, 0); // Back top.
        _triangleShape = [SKShapeNode shapeNodeWithPoints:points count:4];
        _triangleShape.lineWidth = 2.5;
        _triangleShape.zPosition = 1;
        [self addChild:_triangleShape];

        // A particle effect to leave a trail behind the agent as it moves through the scene.
        _particles = [SKEmitterNode nodeWithFileNamed:@"Trail.sks"];
        _defaultParticleRate = _particles.particleBirthRate;
        _particles.position = CGPointMake(-radius + 5, 0);
        _particles.targetNode = scene;
        _particles.zPosition = 0;
        [self addChild:_particles];
    }

    return self;
}

- (void)setColor:(SKColor *)color {
    self.triangleShape.strokeColor = color;
}

- (SKColor *)color {
    return self.triangleShape.strokeColor;
}

- (void)setDrawsTrail:(BOOL)drawsTrail {
    _drawsTrail = drawsTrail;
    if (_drawsTrail) {
        self.particles.particleBirthRate = self.defaultParticleRate;
    }
    else {
        self.particles.particleBirthRate = 0;
    }
}

#pragma mark - GKAgentDelegate

- (void)agentWillUpdate:(nonnull GKAgent *)agent {
    // All changes to agents in this app are driven by the agent system, so
    // there's no other changes to pass into the agent system in this method.
}

- (void)agentDidUpdate:(nonnull GKAgent2D *)agent {
    // Agent and sprite use the same coordinate system (in this app),
    // so just convert vector_float2 position to CGPoint.
    self.position = CGPointMake(agent.position.x, agent.position.y);
    self.zRotation = agent.rotation;
}

@end
```

[Next](Common-AAPLSeekScene.m.md)[Previous](Common-AAPLFleeScene.h.md)

