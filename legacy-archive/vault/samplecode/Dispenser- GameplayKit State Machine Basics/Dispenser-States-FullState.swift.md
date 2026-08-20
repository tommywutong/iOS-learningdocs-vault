---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_FullState_swift.html
archived_at: '2026-07-18T03:07:03.799927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser-States-DispenserState.swift.md)[Previous](Dispenser-States-ServeState.swift.md)

# Dispenser/States/FullState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state for use in a dispenser's state machine. This state represents when the dispenser is full. It turns on the dispenser's indicator light.
*/

import SpriteKit
import GameplayKit

class FullState: DispenserState {

    // MARK: Initialization

    required init(game: GameScene) {
        super.init(game: game, associatedNodeName: "FullState")
    }

    // MARK: GKState overrides

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        // Turn on the indicator light with a green color.
        let greenColor = SKColor.green
        changeIndicatorLightToColor(greenColor)
    }

    override func willExit(to nextState: GKState) {
        super.willExit(to: nextState)

        // Turn off the indicator light.
        let blackColor = SKColor.black
        changeIndicatorLightToColor(blackColor)
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        // This state can only transition to the serve state. 
        return stateClass is ServeState.Type
    }
}
```

[Next](Dispenser-States-DispenserState.swift.md)[Previous](Dispenser-States-ServeState.swift.md)

