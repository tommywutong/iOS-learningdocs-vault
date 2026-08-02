---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_RefillingState_swift.html
archived_at: '2026-07-18T03:07:03.919293Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser-States-EmptyState.swift.md)[Previous](Dispenser-GameScene.swift.md)

# Dispenser/States/RefillingState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state for use in a dispenser's state machine. This state refills the dispenser with water. It plays a refill animation before exiting.
*/

import SpriteKit
import GameplayKit

class RefillingState: DispenserState {
    // MARK: Properties

    /// A multiplier for the speed of the refilling animation.
    static let timeScale: CGFloat = 5

    /**
        The initial height of the water sprite. Used for calculations in the 
        `playRefillAnimationThenExit(_:)` method.
    */
    static let waterNodeHeight: CGFloat = 280

    // MARK: Initialization

    required init(game: GameScene) {
        super.init(game: game, associatedNodeName: "RefillingState")
    }

    // MARK: GKState overrides

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        playRefillAnimationThenExit()
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        // This state can only transition to the full state. 
        return stateClass is FullState.Type
    }

    // MARK: Other Game Logic

    /**
        Plays the refill animation, then transitions the state machine into the 
        Full state.
    */
    func playRefillAnimationThenExit() {
        // Grab the sprite node for the dispenser's water from the scene.
        let waterNode = game.childNode(withName: "//water") as! SKSpriteNode

        // Calculate the duration of the refilling animation.
        let waterRatio = (RefillingState.waterNodeHeight - waterNode.size.height) / RefillingState.waterNodeHeight
        let refillTime = TimeInterval(RefillingState.timeScale * waterRatio)

        /*
            Create and play the animation, then tell the state machine to enter 
            the full state.
        */
        let refillAction = SKAction(named: "refillDispenser", duration: refillTime)!

        waterNode.run(refillAction, completion: {
            self.stateMachine?.enter(FullState.self)
        }) 
    }
}
```

[Next](Dispenser-States-EmptyState.swift.md)[Previous](Dispenser-GameScene.swift.md)

