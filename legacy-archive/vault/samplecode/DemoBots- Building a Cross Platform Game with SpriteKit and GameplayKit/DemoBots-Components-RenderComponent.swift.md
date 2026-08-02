---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_RenderComponent_swift.html
archived_at: '2026-07-18T03:06:17.532295Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-BaseScene%2BScreenRecording.swift.md)[Previous](DemoBots-Components-PlayerBotPlayerControlledState.swift.md)

# DemoBots/Components/RenderComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` that provides an `SKNode` for an entity. This enables it to be represented in the SpriteKit world.
*/

import SpriteKit
import GameplayKit

class RenderComponent: GKComponent {
    // MARK: Properties

    // The `RenderComponent` vends a node allowing an entity to be rendered in a scene.
    let node = SKNode()

    // MARK: GKComponent

    override func didAddToEntity() {
        node.entity = entity
    }

    override func willRemoveFromEntity() {
        node.entity = nil
    }
}
```

[Next](DemoBots-BaseScene%2BScreenRecording.swift.md)[Previous](DemoBots-Components-PlayerBotPlayerControlledState.swift.md)

