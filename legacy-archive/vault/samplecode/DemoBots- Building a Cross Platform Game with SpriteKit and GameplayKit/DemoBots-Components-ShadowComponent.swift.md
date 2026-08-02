---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_ShadowComponent_swift.html
archived_at: '2026-07-18T03:06:17.644540Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-ChargeComponent.swift.md)[Previous](DemoBots-Components-IntelligenceComponent.swift.md)

# DemoBots/Components/ShadowComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` that provides a shadow node for its entity.
*/

import SpriteKit
import GameplayKit

class ShadowComponent: GKComponent {
    // MARK: Properties

    /**
        An `SKSpriteNode` that allows an entity to have a shadow in a scene. The node is
        added to the scene when the component's entity is added to a `LevelScene`
        via `addEntity(_:)`.
    */
    let node: SKSpriteNode

    init(texture: SKTexture, size: CGSize, offset: CGPoint) {
        node = SKSpriteNode(texture: texture)
        node.alpha = 0.25
        node.size = size
        node.position = offset
        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

}
```

[Next](DemoBots-Components-ChargeComponent.swift.md)[Previous](DemoBots-Components-IntelligenceComponent.swift.md)

