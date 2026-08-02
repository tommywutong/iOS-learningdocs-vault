---
title: 'Boxes: GameplayKit Entity-Component Basics'
apple_id: TP40016459
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Listings/Boxes__iOS__GameViewController_swift.html
archived_at: '2026-07-18T03:02:16.511303Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Boxes: GameplayKit Entity-Component Basics](Boxes-%20GameplayKit%20Entity-Component%20Basics.md)


[Next](Boxes%20%28iOS%29-AppDelegate.swift.md)[Previous](Boxes%20%28OS%20X%29-AppDelegate.swift.md)

# Boxes (iOS)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UIViewController` subclass that stores references to game-wide input sources and managers.
*/

import UIKit
import SceneKit

class GameViewController: UIViewController {
    // MARK: Properties

    let game = Game()

    // MARK: Methods

    override func viewDidLoad() {
        super.viewDidLoad()

        // Grab the controller's view as a SceneKit view.
        guard let scnView = view as? SCNView else { fatalError("Unexpected view class") }

        // Set our background color to a light gray color.
        scnView.backgroundColor = UIColor.lightGray

        // Ensure the view controller can display our game's scene.
        scnView.scene = game.scene

        // Ensure the game can manage updates for the scene.
        scnView.delegate = game
    }

    /// Causes the boxes to jump if a tap is detected.
    @IBAction func handleTap(_: UITapGestureRecognizer) {
        game.jumpBoxes()
    }
}
```

[Next](Boxes%20%28iOS%29-AppDelegate.swift.md)[Previous](Boxes%20%28OS%20X%29-AppDelegate.swift.md)

