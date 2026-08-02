---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_ControlInputSource_swift.html
archived_at: '2026-07-18T03:06:17.949438Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Physics-ColliderType.swift.md)[Previous](DemoBots-BaseScene%2BKeyboardEventForwarding.swift.md)

# DemoBots/ControlInputSource.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Protocols that manage and respond to control input for the `PlayerBot` and for the game as a whole.
*/

import simd

enum ControlInputDirection: Int {
    case up = 0, down, left, right

    init?(vector: float2) {
        // Require sufficient displacement to specify direction.
        guard length(vector) >= 0.5 else { return nil }

        // Take the max displacement as the specified axis.
        if abs(vector.x) > abs(vector.y) {
            self = vector.x > 0 ? .right : .left
        }
        else {
            self = vector.y > 0 ? .up : .down
        }
    }
}

/// Delegate methods for responding to control input that applies to the game as a whole.
protocol ControlInputSourceGameStateDelegate: class {
    func controlInputSourceDidSelect(_ controlInputSource: ControlInputSourceType)
    func controlInputSource(_ controlInputSource: ControlInputSourceType, didSpecifyDirection: ControlInputDirection)
    func controlInputSourceDidTogglePauseState(_ controlInputSource: ControlInputSourceType)

    #if DEBUG
    func controlInputSourceDidToggleDebugInfo(_ controlInputSource: ControlInputSourceType)

    func controlInputSourceDidTriggerLevelSuccess(_ controlInputSource: ControlInputSourceType)
    func controlInputSourceDidTriggerLevelFailure(_ controlInputSource: ControlInputSourceType)
    #endif
}

/// Delegate methods for responding to control input that applies to the `PlayerBot`.
protocol ControlInputSourceDelegate: class {
    /**
        Update the `ControlInputSourceDelegate` with new displacement
        in a top down 2D coordinate system (x, y):
            Up:    (0.0, 1.0)
            Down:  (0.0, -1.0)
            Left:  (-1.0, 0.0)
            Right: (1.0, 0.0)
    */
    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateDisplacement displacement: float2)

    /**
        Update the `ControlInputSourceDelegate` with new angular displacement
        denoting both the requested angle, and magnitude with which to rotate.
        Measured in radians.
     */
    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateAngularDisplacement angularDisplacement: float2)

    /**
        Update the `ControlInputSourceDelegate` to move forward or backward
        relative to the orientation of the entity.
            Forward:  (0.0, 1.0)
            Backward: (0.0, -1.0)
     */
    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateWithRelativeDisplacement relativeDisplacement: float2)

    /**
        Update the `ControlInputSourceDelegate` with new angular displacement
        relative to the entity's existing orientation.
            Clockwise:        (-1.0, 0.0)
            CounterClockwise: (1.0, 0.0)
     */
    func controlInputSource(_ controlInputSource: ControlInputSourceType, didUpdateWithRelativeAngularDisplacement relativeAngularDisplacement: float2)

    /// Instructs the `ControlInputSourceDelegate` to cause the player to attack.
    func controlInputSourceDidBeginAttacking(_ controlInputSource: ControlInputSourceType)

    /// Instructs the `ControlInputSourceDelegate` to end the player's attack.
    func controlInputSourceDidFinishAttacking(_ controlInputSource: ControlInputSourceType)
}

/// A protocol to be adopted by classes that provide control input and notify their delegates when input is available.
protocol ControlInputSourceType: class {
    /// A delegate that receives information about actions that apply to the `PlayerBot`.
    weak var delegate: ControlInputSourceDelegate? { get set }

    /// A delegate that receives information about actions that apply to the game as a whole.
    weak var gameStateDelegate: ControlInputSourceGameStateDelegate? { get set }

    var allowsStrafing: Bool { get }

    func resetControlState()
}
```

[Next](DemoBots-Physics-ColliderType.swift.md)[Previous](DemoBots-BaseScene%2BKeyboardEventForwarding.swift.md)

