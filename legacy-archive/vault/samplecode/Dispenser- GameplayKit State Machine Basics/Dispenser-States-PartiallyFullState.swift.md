---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_PartiallyFullState_swift.html
archived_at: '2026-07-18T03:07:03.861296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser-States-ServeState.swift.md)[Previous](Dispenser-States-EmptyState.swift.md)

# Dispenser/States/PartiallyFullState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state for use in a dispenser's state machine. This state represents when the dispenser is partially full.
*/

import SpriteKit
import GameplayKit

class PartiallyFullState: DispenserState {

    // MARK: Initialization

    required init(game: GameScene) {
        super.init(game: game, associatedNodeName: "PartiallyFullState")
    }

    // MARK: GKState overrides

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        // This state can only transition to the serve and refilling states. 
        switch stateClass {
            case is ServeState.Type, is RefillingState.Type:
                return true

            default:
                return false
        }
    }
}
```

[Next](Dispenser-States-ServeState.swift.md)[Previous](Dispenser-States-EmptyState.swift.md)

