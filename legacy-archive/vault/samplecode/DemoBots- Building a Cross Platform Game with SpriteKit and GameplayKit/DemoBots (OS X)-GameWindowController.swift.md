---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots__OS_X__GameWindowController_swift.html
archived_at: '2026-07-18T03:06:22.184863Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots%20%28OS%20X%29-AppDelegate.swift.md)[Previous](DemoBots%20%28OS%20X%29-GameViewController.swift.md)

# DemoBots (OS X)/GameWindowController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `NSWindowController` subclass to simplify the game's interaction with window resizing on OS X.
*/

import Cocoa
import SpriteKit

class GameWindowController: NSWindowController, NSWindowDelegate {
    // MARK: Properties

    var view: SKView {
        let gameViewController = window!.contentViewController as! GameViewController
        return gameViewController.view as! SKView
    }

    override func awakeFromNib() {
        super.awakeFromNib()

        window?.delegate = self
    }

    // MARK: NSWindowDelegate
    func windowWillStartLiveResize(_ notification: Notification) {
        // Pause the scene while the window resizes if the game is active.
        if let levelScene = view.scene as? LevelScene, levelScene.stateMachine.currentState is LevelSceneActiveState {
            levelScene.isPaused = true
        }
    }

    func windowDidEndLiveResize(_ notification: Notification) {
        // Un-pause the scene when the window stops resizing if the game is active.
        if let levelScene = view.scene as? LevelScene, levelScene.stateMachine.currentState is LevelSceneActiveState {
            levelScene.isPaused = false
        }
    }

    // OS X games that use a single window for the entire game should quit when that window is closed.
    func applicationShouldTerminateAfterLastWindowClosed(sender: NSApplication) -> Bool {
        return true
    }
}
```

[Next](DemoBots%20%28OS%20X%29-AppDelegate.swift.md)[Previous](DemoBots%20%28OS%20X%29-GameViewController.swift.md)

