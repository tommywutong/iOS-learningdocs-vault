---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_PlayerBotHitState_swift.html
archived_at: '2026-07-18T03:06:17.340417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-TaskBotBehavior.swift.md)[Previous](DemoBots-Components-RulesComponent.swift.md)

# DemoBots/Components/PlayerBotHitState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used to represent the player when hit by a `TaskBot` attack.
*/

import SpriteKit
import GameplayKit

class PlayerBotHitState: GKState {
    // MARK: Properties

    unowned var entity: PlayerBot

    /// The amount of time the `PlayerBot` has been in the "hit" state.
    var elapsedTime: TimeInterval = 0.0

    /// The `AnimationComponent` associated with the `entity`.
    var animationComponent: AnimationComponent {
        guard let animationComponent = entity.component(ofType: AnimationComponent.self) else { fatalError("A PlayerBotHitState's entity must have an AnimationComponent.") }
        return animationComponent
    }

    // MARK: Initializers

    required init(entity: PlayerBot) {
        self.entity = entity
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Reset the elapsed "hit" duration on entering this state.
        elapsedTime = 0.0

        // Request the "hit" animation for this `PlayerBot`.
        animationComponent.requestedAnimationState = .hit
    }

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        // Update the amount of time the `PlayerBot` has been in the "hit" state.
        elapsedTime += seconds

        // When the `PlayerBot` has been in this state for long enough, transition to the appropriate next state.
        if elapsedTime >= GameplayConfiguration.PlayerBot.hitStateDuration {
            if entity.isPoweredDown {
                stateMachine?.enter(PlayerBotRechargingState.self)
            }
            else {
                stateMachine?.enter(PlayerBotPlayerControlledState.self)
            }
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is PlayerBotPlayerControlledState.Type, is PlayerBotRechargingState.Type:
                return true

            default:
                return false
        }
    }
}
```

[Next](DemoBots-Components-TaskBotBehavior.swift.md)[Previous](DemoBots-Components-RulesComponent.swift.md)

