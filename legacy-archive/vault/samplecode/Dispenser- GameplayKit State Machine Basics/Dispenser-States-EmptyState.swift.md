---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_EmptyState_swift.html
archived_at: '2026-07-18T03:07:03.720395Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser-States-PartiallyFullState.swift.md)[Previous](Dispenser-States-RefillingState.swift.md)

# Dispenser/States/EmptyState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state for use in a dispenser's state machine. This state represents when the dispenser is empty. It flashes the dispenser's warning light.
*/

import SpriteKit
import GameplayKit

class EmptyState: DispenserState {
    // MARK: Properties

    /// Keeps track of time between indicator light toggles.
    var flashTimeCounter: TimeInterval = 0

    /// Defines the time interval between when the light is toggled.
    static let flashInterval = 0.6

    /// Changes the color of the indicator light to red or black when toggled.
    var lightOn = true {
        didSet {
            if lightOn {
                let redColor = SKColor.red
                changeIndicatorLightToColor(redColor)
            }
            else {
                let blackColor = SKColor.black
                changeIndicatorLightToColor(blackColor)
            }
        }
    }

    // MARK: Initialization

    required init(game: GameScene) {
        super.init(game: game, associatedNodeName: "EmptyState")
    }

    // MARK: GKState overrides

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Turn on the indicator light with a red color.
        let red = SKColor.red
        changeIndicatorLightToColor(red)
    }

    override func willExit(to nextState: GKState) {
        super.willExit(to: nextState)

        // Turn on the indicator light with a green color.
        let black = SKColor.black
        changeIndicatorLightToColor(black)
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        // This state can only transition to the refilling state. 
        return stateClass is RefillingState.Type
    }

    override func update(deltaTime: TimeInterval) {
        // Keep track of the time since the last update.
        flashTimeCounter += deltaTime

        /*
            If an interval of `flashInterval` has passed since the previous update,
            toggle the indicator light and reset the time counter.
        */
        if flashTimeCounter > EmptyState.flashInterval {
            lightOn = !lightOn
            flashTimeCounter = 0
        }
    }
}
```

[Next](Dispenser-States-PartiallyFullState.swift.md)[Previous](Dispenser-States-RefillingState.swift.md)

