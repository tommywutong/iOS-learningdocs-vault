---
title: 'Boxes: GameplayKit Entity-Component Basics'
apple_id: TP40016459
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Listings/Boxes__OS_X__GameViewController_swift.html
archived_at: '2026-07-18T03:02:16.427483Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Boxes: GameplayKit Entity-Component Basics](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)


[Next](Boxes%20%28OS%20X%29-AppDelegate.swift.md)[Previous](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)

# Boxes (OS X)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `NSViewController` subclass that stores references to game-wide input sources and managers.
*/

import SceneKit

class GameViewController: NSViewController {
    // MARK: Properties

    let game = Game()

    // MARK: Methods

    override func viewDidLoad() {
        // Grab the controller's view as a SceneKit view.
        guard let scnView = view as? SCNView else { fatalError("Unexpected view class") }

        // Set our background color to a light gray color.
        scnView.backgroundColor = NSColor.lightGray

        // Ensure the view controller can display our game's scene.
        scnView.scene = game.scene

        // Ensure the game can manage updates for the scene.
        scnView.delegate = game
    }

    override func keyDown(with _: NSEvent) {
        // Causes boxes to jump if a key press is detected.
        game.jumpBoxes()
    }

    override func mouseDown(with _: NSEvent) {
        // Causes boxes to jump if a click is detected.
        game.jumpBoxes()
    }
}
```

[Next](Boxes%20%28OS%20X%29-AppDelegate.swift.md)[Previous](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)

