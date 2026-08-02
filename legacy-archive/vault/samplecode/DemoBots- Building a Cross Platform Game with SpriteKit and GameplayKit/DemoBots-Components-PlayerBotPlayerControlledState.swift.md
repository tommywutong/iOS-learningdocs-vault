---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_PlayerBotPlayerControlledState_swift.html
archived_at: '2026-07-18T03:06:17.399140Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-RenderComponent.swift.md)[Previous](DemoBots-Components-PlayerBotAppearState.swift.md)

# DemoBots/Components/PlayerBotPlayerControlledState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used to represent the `PlayerBot` when ready for control input from the player.
*/

import SpriteKit
import GameplayKit

class PlayerBotPlayerControlledState: GKState {
    // MARK: Properties

    unowned var entity: PlayerBot

    /// The `AnimationComponent` associated with the `entity`.
    var animationComponent: AnimationComponent {
        guard let animationComponent = entity.component(ofType: AnimationComponent.self) else { fatalError("A PlayerBotPlayerControlledState's entity must have an AnimationComponent.") }
        return animationComponent
    }

    /// The `MovementComponent` associated with the `entity`.
    var movementComponent: MovementComponent {
        guard let movementComponent = entity.component(ofType: MovementComponent.self) else { fatalError("A PlayerBotPlayerControlledState's entity must have a MovementComponent.") }
        return movementComponent
    }

    /// The `InputComponent` associated with the `entity`.
    var inputComponent: InputComponent {
        guard let inputComponent = entity.component(ofType: InputComponent.self) else { fatalError("A PlayerBotPlayerControlledState's entity must have an InputComponent.") }
        return inputComponent
    }

    // MARK: Initializers

    required init(entity: PlayerBot) {
        self.entity = entity
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Turn on controller input for the `PlayerBot` when entering the player-controlled state.
        inputComponent.isEnabled = true
    }

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        /*
            Assume an animation of "idle" that can then be overwritten by the movement
            component in response to user input.
        */
        animationComponent.requestedAnimationState = .idle
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is PlayerBotHitState.Type, is PlayerBotRechargingState.Type:
                return true

            default:
                return false
        }
    }

    override func willExit(to nextState: GKState) {
        super.willExit(to: nextState)

        // Turn off controller input for the `PlayerBot` when leaving the player-controlled state.
        entity.component(ofType: InputComponent.self)?.isEnabled = false

        // `movementComponent` is a computed property. Declare a local version so we don't compute it multiple times.
        let movementComponent = self.movementComponent

        // Cancel any planned movement or rotation when leaving the player-controlled state.
        movementComponent.nextTranslation = nil
        movementComponent.nextRotation = nil
    }
}
```

[Next](DemoBots-Components-RenderComponent.swift.md)[Previous](DemoBots-Components-PlayerBotAppearState.swift.md)

