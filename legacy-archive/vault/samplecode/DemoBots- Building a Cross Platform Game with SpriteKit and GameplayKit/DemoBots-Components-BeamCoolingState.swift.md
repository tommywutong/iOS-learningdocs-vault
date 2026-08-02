---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_BeamCoolingState_swift.html
archived_at: '2026-07-18T03:06:16.219151Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-PhysicsComponent.swift.md)[Previous](DemoBots-Components-GroundBotAttackState.swift.md)

# DemoBots/Components/BeamCoolingState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The state the beam enters when it overheats from being used for too long.
*/

import SpriteKit
import GameplayKit

class BeamCoolingState: GKState {
    // MARK: Properties

    unowned var beamComponent: BeamComponent

    /// The amount of time the beam has been cooling down.
    var elapsedTime: TimeInterval = 0.0

    // MARK: Initializers

    required init(beamComponent: BeamComponent) {
        self.beamComponent = beamComponent
    }

    // MARK: GKState life cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        elapsedTime = 0.0
    }

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        elapsedTime += seconds

        // If the beam has spent long enough cooling down, enter `BeamIdleState`.
        if elapsedTime >= GameplayConfiguration.Beam.coolDownDuration {
            stateMachine?.enter(BeamIdleState.self)
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is BeamIdleState.Type, is BeamFiringState.Type:
                return true

            default:
                return false
        }
    }

    override func willExit(to nextState: GKState) {
        super.willExit(to: nextState)

        if let playerBot = beamComponent.entity as? PlayerBot {
            beamComponent.beamNode.update(withBeamState: nextState, source: playerBot)
        }
    }
}
```

[Next](DemoBots-Components-PhysicsComponent.swift.md)[Previous](DemoBots-Components-GroundBotAttackState.swift.md)

