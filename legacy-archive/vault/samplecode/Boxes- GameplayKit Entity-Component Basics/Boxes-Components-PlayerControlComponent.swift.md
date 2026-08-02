---
title: 'Boxes: GameplayKit Entity-Component Basics'
apple_id: TP40016459
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Listings/Boxes_Components_PlayerControlComponent_swift.html
archived_at: '2026-07-18T03:02:16.260336Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Boxes: GameplayKit Entity-Component Basics](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)


[Next](Boxes-Components-GeometryComponent.swift.md)[Previous](Boxes-Game.swift.md)

# Boxes/Components/PlayerControlComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A component that attaches to an entity. This component enables a geometry node to jump.
*/

import GameplayKit
import SceneKit

class PlayerControlComponent: GKComponent {
    // MARK: Properties

    /// A convenience property for the entity's geometry component.
    var geometryComponent: GeometryComponent? {
        return entity?.component(ofType: GeometryComponent.self)
    }

    // MARK: Methods

    /// Tells this entity's geometry component to jump.
    func jump() {
        let jumpVector = SCNVector3(x: 0, y: 2, z: 0)
        geometryComponent?.applyImpulse(jumpVector)
    }
}
```

[Next](Boxes-Components-GeometryComponent.swift.md)[Previous](Boxes-Game.swift.md)

