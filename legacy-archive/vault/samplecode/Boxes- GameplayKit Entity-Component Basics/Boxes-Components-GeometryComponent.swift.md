---
title: 'Boxes: GameplayKit Entity-Component Basics'
apple_id: TP40016459
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Listings/Boxes_Components_GeometryComponent_swift.html
archived_at: '2026-07-18T03:02:16.155558Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Boxes: GameplayKit Entity-Component Basics](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)


[Next](Boxes-Components-ParticleComponent.swift.md)[Previous](Boxes-Components-PlayerControlComponent.swift.md)

# Boxes/Components/GeometryComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A component that attaches to an entity. This component controls a geometry node's physics body.
*/

import SceneKit
import GameplayKit

class GeometryComponent: GKComponent {
    // MARK: Properties

    /// A reference to the box in the scene that the entity controls.
    let geometryNode: SCNNode

    // MARK: Initialization

    init(geometryNode: SCNNode) {
        self.geometryNode = geometryNode
        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: Methods

    /// Applies an upward impulse to the entity's box node, causing it to jump.
    func applyImpulse(_ vector: SCNVector3) {
        geometryNode.physicsBody?.applyForce(vector, asImpulse: true)
    }
}
```

[Next](Boxes-Components-ParticleComponent.swift.md)[Previous](Boxes-Components-PlayerControlComponent.swift.md)

