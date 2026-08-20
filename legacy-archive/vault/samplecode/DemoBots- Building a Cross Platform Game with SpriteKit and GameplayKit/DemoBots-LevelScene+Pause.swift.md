---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_LevelScene_Pause_swift.html
archived_at: '2026-07-18T03:06:19.619865Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-IntelligenceComponent.swift.md)[Previous](DemoBots-Protocols-ContactNotifiableType.swift.md)

# DemoBots/LevelScene+Pause.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension on `LevelScene` which ensures that game play is paused when the app enters the background for a number of user initiated events.
*/

#if os(OSX)
import AppKit
#else
import UIKit
#endif

extension LevelScene {
    // MARK: Properties

    /**
        The scene's `paused` property is set automatically when the
        app enters the background. Override to check if an `overlay` node is
        being presented to determine if the game should be paused.
    */
    override var isPaused: Bool {
        didSet {
            if overlay != nil {
                worldNode.isPaused = true
            }
        }
    }

    /// Platform specific notifications about the app becoming inactive.
    private var pauseNotificationNames: [NSNotification.Name] {
        #if os(OSX)
        return [
           .NSApplicationWillResignActive,
           .NSWindowDidMiniaturize
        ]
        #else
        return [
            NSNotification.Name.UIApplicationWillResignActive
        ]
        #endif
    }

    // MARK: Convenience

    /**
        Register for notifications about the app becoming inactive in
        order to pause the game. 
    */
    func registerForPauseNotifications() {
        for notificationName in pauseNotificationNames {
            NotificationCenter.default.addObserver(self, selector: #selector(LevelScene.pauseGame), name: notificationName, object: nil)
        }
    }

    func pauseGame() {
        stateMachine.enter(LevelScenePauseState.self)
    }

    func unregisterForPauseNotifications() {
        for notificationName in pauseNotificationNames {
            NotificationCenter.default.removeObserver(self, name: notificationName, object: nil)
        }
    }
}
```

[Next](DemoBots-Components-IntelligenceComponent.swift.md)[Previous](DemoBots-Protocols-ContactNotifiableType.swift.md)

