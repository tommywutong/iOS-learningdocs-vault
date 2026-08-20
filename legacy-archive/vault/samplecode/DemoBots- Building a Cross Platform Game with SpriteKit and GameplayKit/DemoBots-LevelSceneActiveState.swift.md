---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_LevelSceneActiveState_swift.html
archived_at: '2026-07-18T03:06:19.285722Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-SceneMetadata.swift.md)[Previous](DemoBots-LevelScene.swift.md)

# DemoBots/LevelSceneActiveState.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A state used by `LevelScene` to indicate that the game is actively being played. This state updates the current time of the level's countdown timer.
*/

import SpriteKit
import GameplayKit

class LevelSceneActiveState: GKState {
    // MARK: Properties

    unowned let levelScene: LevelScene

    var timeRemaining: TimeInterval = 0.0

    /*
        A formatter for individual date components used to provide an appropriate
        display value for the timer.
    */
    let timeRemainingFormatter: DateComponentsFormatter = {
        let formatter = DateComponentsFormatter()
        formatter.zeroFormattingBehavior = .pad
        formatter.allowedUnits = [.minute, .second]

        return formatter
    }()

    // The formatted string representing the time remaining.
    var timeRemainingString: String {
        let components = NSDateComponents()
        components.second = Int(max(0.0, timeRemaining))

        return timeRemainingFormatter.string(from: components as DateComponents)!
    }

    // MARK: Initializers

    init(levelScene: LevelScene) {
        self.levelScene = levelScene

        timeRemaining = levelScene.levelConfiguration.timeLimit
    }

    // MARK: GKState Life Cycle

    override func didEnter(from previousState: GKState?) {
        super.didEnter(from: previousState)

        levelScene.timerNode.text = timeRemainingString
    }

    override func update(deltaTime seconds: TimeInterval) {
        super.update(deltaTime: seconds)

        // Subtract the elapsed time from the remaining time.
        timeRemaining -= seconds

        // Update the displayed time remaining.
        levelScene.timerNode.text = timeRemainingString

        // Check if the `levelScene` contains any bad `TaskBot`s.
        let allTaskBotsAreGood = !levelScene.entities.contains { entity in
            if let taskBot = entity as? TaskBot {
                return !taskBot.isGood
            }

            return false
        }

        if allTaskBotsAreGood {
            // If all the TaskBots are good, the player has completed the level.
            stateMachine?.enter(LevelSceneSuccessState.self)
        }
        else if timeRemaining <= 0.0 {
            // If there is no time remaining, the player has failed to complete the level.
            stateMachine?.enter(LevelSceneFailState.self)
        }
    }

    override func isValidNextState(_ stateClass: AnyClass) -> Bool {
        switch stateClass {
            case is LevelScenePauseState.Type, is LevelSceneFailState.Type, is LevelSceneSuccessState.Type:
                return true

            default:
                return false
        }
    }
}
```

[Next](DemoBots-SceneMetadata.swift.md)[Previous](DemoBots-LevelScene.swift.md)

