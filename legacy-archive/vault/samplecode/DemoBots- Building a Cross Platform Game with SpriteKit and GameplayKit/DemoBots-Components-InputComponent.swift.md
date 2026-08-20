---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_InputComponent_swift.html
archived_at: '2026-07-18T03:06:16.883511Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-FlyingBotPreAttackState.swift.md)[Previous](DemoBots-Components-CompassDirection.swift.md)

# DemoBots/Components/InputComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` that enables an entity to accept control input from device-specific sources.
*/

import SpriteKit
import GameplayKit

class InputComponent: GKComponent, ControlInputSourceDelegate {
    // MARK: Types

    struct InputState {
        var translation: MovementKind?
        var rotation: MovementKind?
        var beamIsTriggered = false
        var allowsStrafing = false

        static let noInput = InputState()
    }

    // MARK: Properties

    /**
        `InputComponent` has the ability to ignore input when disabled.

        This is used to prevent the player from moving or firing while
        being attacked.
    */
    var isEnabled = true {
        didSet {
            if isEnabled {
                // Apply the current input state to the movement and beam components.
                applyInputState(state: state)
            }
            else {
                // Apply a state of no input to the movement and beam components.
                applyInputState(state: InputState.noInput)
            }
        }
    }

    var state = InputState() {
        didSet {
            if isEnabled {
                applyInputState(state: state)
            }
        }
    }

    // MARK: ControlInputSourceDelegate

    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateDisplacement displacement: float2) {
        state.translation = MovementKind(displacement: displacement)
    }

    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateAngularDisplacement angularDisplacement: float2) {
        state.rotation = MovementKind(displacement: angularDisplacement)
    }

    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateWithRelativeDisplacement relativeDisplacement: float2) {
        /*
            Create a `MovementKind` instance indicating whether the displacement
            should translate the entity forwards or backwards from the direction
            it is facing.
        */
        state.translation = MovementKind(displacement: relativeDisplacement, relativeToOrientation: true)
    }

    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateWithRelativeAngularDisplacement relativeAngularDisplacement: float2) {
        /*
            Create a `MovementKind` instance indicating whether the displacement
            should rotate the entity clockwise or counter-clockwise from the direction
            it is facing.
        */
        state.rotation = MovementKind(displacement: relativeAngularDisplacement, relativeToOrientation: true)
    }

    func controlInputSourceDidBeginAttacking(_ controlInputSource: ControlInputSourceType) {
        state.allowsStrafing = controlInputSource.allowsStrafing
        state.beamIsTriggered = true
    }

    func controlInputSourceDidFinishAttacking(_ controlInputSource: ControlInputSourceType) {
        state.beamIsTriggered = false
    }

    // MARK: Convenience

    func applyInputState(state: InputState) {
        if let movementComponent = entity?.component(ofType: MovementComponent.self) {
            movementComponent.allowsStrafing = state.allowsStrafing
            movementComponent.nextRotation = state.rotation
            movementComponent.nextTranslation = state.translation
        }

        if let beamComponent = entity?.component(ofType: BeamComponent.self) {
            beamComponent.isTriggered = state.beamIsTriggered
        }
    }
}
```

[Next](DemoBots-Components-FlyingBotPreAttackState.swift.md)[Previous](DemoBots-Components-CompassDirection.swift.md)

