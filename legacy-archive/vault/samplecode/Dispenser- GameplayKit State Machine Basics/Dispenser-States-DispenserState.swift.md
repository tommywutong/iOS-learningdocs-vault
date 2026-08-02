---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_DispenserState_swift.html
archived_at: '2026-07-18T03:07:03.645012Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Document%20Revision%20History.md)[Previous](Dispenser-States-FullState.swift.md)

# Dispenser/States/DispenserState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A superclass for states powering the dispenser.
*/

import SpriteKit
import GameplayKit

class DispenserState: GKState {
    // MARK: Properties

    /// A reference to the game scene, used to alter sprites.
    let game: GameScene

    /// The name of the node in the game scene that is associated with this state.
    let associatedNodeName: String

    /// Convenience property to get the state's associated sprite node.
    var associatedNode: SKSpriteNode? {
        return game.childNode(withName: "//\(associatedNodeName)") as? SKSpriteNode
    }

    // MARK: Initialization

    init(game: GameScene, associatedNodeName: String) {
        self.game = game
        self.associatedNodeName = associatedNodeName
    }

    // MARK: GKState overrides

    /// Highlights the sprite representing the state.
    override func didEnter(from previousState: GKState?) {
        guard let associatedNode = associatedNode else { return }
        associatedNode.color = SKColor.lightGray
    }

    /// Unhighlights the sprite representing the state.
    override func willExit(to nextState: GKState) {
        guard let associatedNode = associatedNode else { return }
        associatedNode.color = SKColor.darkGray
    }

    // MARK: Methods

    /// Changes the dispenser's indicator light to the specified color.
    func changeIndicatorLightToColor(_ color: SKColor) {
        let indicator = game.childNode(withName: "//indicator") as! SKSpriteNode
        indicator.color = color
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Dispenser-States-FullState.swift.md)

