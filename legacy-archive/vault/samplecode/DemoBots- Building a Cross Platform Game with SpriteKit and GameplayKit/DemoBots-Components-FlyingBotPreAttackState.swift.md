---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_FlyingBotPreAttackState_swift.html
archived_at: '2026-07-18T03:06:16.605025Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-GroundBotPreAttackState.swift.md)[Previous](DemoBots-Components-InputComponent.swift.md)

# DemoBots/Components/FlyingBotPreAttackState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The state `FlyingBot`s are in immediately prior to starting their blast cloud attack.
*/

import SpriteKit
import GameplayKit

class FlyingBotPreAttackState: GKState {
    // MARK: Properties

    unowned var entity: FlyingBot

    /// The amount of time the `FlyingBot` has been in its "pre-attack" state.
    var elapsedTime: TimeInterval = 0.0

    /// The `AnimationComponent` associated with the `entity`.
    var animationComponent: AnimationComponent {
        guard let animationComponent = entity.component(ofType: AnimationComponent.self) else { fatalError("A FlyingBotPreAttackState's entity must have an AnimationComponent.") }
        return animationComponent
    }

    // MARK: Initializers

    required init(entity: FlyingBot) {
        self.entity = entity
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Reset the tracking of how long the `TaskBot` has been in a "pre-attack" state.
        elapsedTime = 0.0

        // Request the "attack" animation for this `FlyingBot`.
        animationComponent.requestedAnimationState = .attack
    }

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        // Update the time that the `TaskBot` has been in its "pre-attack" state.
        elapsedTime += seconds

        /*
            If the `TaskBot` has been in its "pre-attack" state for long enough,
            move to the attack state.
        */
        if elapsedTime >= GameplayConfiguration.TaskBot.preAttackStateDuration {
            stateMachine?.enter(FlyingBotBlastState.self)
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is TaskBotAgentControlledState.Type, is FlyingBotBlastState.Type, is TaskBotZappedState.Type:
                return true

            default:
                return false
        }
    }
}
```

[Next](DemoBots-Components-GroundBotPreAttackState.swift.md)[Previous](DemoBots-Components-InputComponent.swift.md)

