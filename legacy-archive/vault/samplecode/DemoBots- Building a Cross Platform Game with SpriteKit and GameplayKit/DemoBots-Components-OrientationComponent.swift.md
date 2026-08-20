---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_OrientationComponent_swift.html
archived_at: '2026-07-18T03:06:17.149561Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-BeamIdleState.swift.md)[Previous](DemoBots-Components-AnimationComponent.swift.md)

# DemoBots/Components/OrientationComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` that enables an animated entity to track its current orientation (i.e. the direction it is facing). This information is used when choosing an appropriate animation.
*/

import SpriteKit
import GameplayKit

class OrientationComponent: GKComponent {
    // MARK: Properties

    var zRotation: CGFloat = 0.0 {
        didSet {
            let twoPi = CGFloat(M_PI * 2)
            zRotation = (zRotation + twoPi).truncatingRemainder(dividingBy: twoPi)
        }
    }

    var compassDirection: CompassDirection {
        get {
            return CompassDirection(zRotation: zRotation)
        }

        set {
            zRotation = newValue.zRotation
        }
    }
}
```

[Next](DemoBots-Components-BeamIdleState.swift.md)[Previous](DemoBots-Components-AnimationComponent.swift.md)

