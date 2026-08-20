---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_BeamIdleState_swift.html
archived_at: '2026-07-18T03:06:16.356867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-GroundBotAttackState.swift.md)[Previous](DemoBots-Components-OrientationComponent.swift.md)

# DemoBots/Components/BeamIdleState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The state of the `PlayerBot`'s beam when not in use.
*/

import SpriteKit
import GameplayKit

class BeamIdleState: GKState {
    // MARK: Properties

    unowned var beamComponent: BeamComponent

    // MARK: Initializers

    required init(beamComponent: BeamComponent) {
        self.beamComponent = beamComponent
    }

    // MARK: GKState life cycle

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        // If the beam has been triggered, enter `BeamFiringState`.
        if beamComponent.isTriggered {
            stateMachine?.enter(BeamFiringState.self)
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        return stateClass is BeamFiringState.Type
    }
}
```

[Next](DemoBots-Components-GroundBotAttackState.swift.md)[Previous](DemoBots-Components-OrientationComponent.swift.md)

