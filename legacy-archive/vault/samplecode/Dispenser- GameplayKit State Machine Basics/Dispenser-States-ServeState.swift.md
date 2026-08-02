---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser_States_ServeState_swift.html
archived_at: '2026-07-18T03:07:03.978377Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser-States-FullState.swift.md)[Previous](Dispenser-States-PartiallyFullState.swift.md)

# Dispenser/States/ServeState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state for use in a dispenser's state machine. This state dispenses water from the dispenser. It plays a brief dispensing animation before exiting.
*/

import SpriteKit
import GameplayKit

class ServeState: DispenserState {
    // MARK: Properties

    /// A multiplier for the speed of the dispensing animation.
    static let timeScale = 0.5

    // MARK: Initialization

    required init(game: GameScene) {
        super.init(game: game, associatedNodeName: "ServeState")
    }

    // MARK: GKState overrides

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        playDispensingAnimationThenExit()
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        /*
            This state can only transition to the partially full and empty 
            states.
        */
        switch stateClass {
            case is PartiallyFullState.Type, is EmptyState.Type:
                return true

            default:
                return false
        }
    }

    // MARK: Other Game Logic

    /**
        Creates and plays the dispensing animation, then tells the state
        machine to enter the empty or partially full state, depending on the
        resultant water level.
    */
    func playDispensingAnimationThenExit() {
        // These nodes create base actions to be run on nodes in the scene.
        let slideCupAction    = SKAction(named: "slideCup", duration: 3 * ServeState.timeScale)!
        let fillCupAction     = SKAction(named: "fillCup", duration: 2 * ServeState.timeScale)!
        let resetStreamAction = SKAction(named: "resetStream", duration: 0)!
        let resetCupAction    = SKAction(named: "resetCup", duration: 0)!
        let drainWaterAction  = SKAction(named: "drainWater", duration: ServeState.timeScale)!

        // These nodes run an action on a node.
        let slideCupActionOnNode    = SKAction.run(slideCupAction, onChildWithName: "//bottle")
        let fillCupActionOnNode     = SKAction.run(fillCupAction, onChildWithName: "//stream")
        let resetStreamActionOnNode = SKAction.run(resetStreamAction, onChildWithName: "//stream")
        let resetCupActionOnNode    = SKAction.run(resetCupAction, onChildWithName: "//bottle")
        let drainWaterActionOnNode  = SKAction.run(drainWaterAction, onChildWithName: "//water")

        // This action inserts a delay into a sequence.
        let waitAction = SKAction.wait(forDuration: ServeState.timeScale)

        // This action defines a timed sequence of events.
        let innerSequence = [
            waitAction,
            drainWaterActionOnNode,
            waitAction,
            resetStreamActionOnNode,
            waitAction,
            resetCupActionOnNode
        ]
        let innerSequenceAction = SKAction.sequence(innerSequence)

        // This action defines a group of actions to play simultaneously. 
        let group = [slideCupActionOnNode, fillCupActionOnNode, innerSequenceAction]
        let groupAction = SKAction.group(group)

        // Play the dispensing animation, then exit conditionally. 
        game.scene?.run(groupAction, completion: {
            let waterNode = self.game.childNode(withName: "//water") as! SKSpriteNode
            if waterNode.size.height < 1 {
                self.stateMachine?.enter(EmptyState.self)
            }
            else {
                self.stateMachine?.enter(PartiallyFullState.self)
            }
        }) 
    }
}
```

[Next](Dispenser-States-FullState.swift.md)[Previous](Dispenser-States-PartiallyFullState.swift.md)

