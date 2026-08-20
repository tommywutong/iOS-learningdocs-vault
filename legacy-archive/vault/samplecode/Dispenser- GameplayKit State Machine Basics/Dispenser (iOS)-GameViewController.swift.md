---
title: 'Dispenser: GameplayKit State Machine Basics'
apple_id: TP40016460
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Listings/Dispenser__iOS__GameViewController_swift.html
archived_at: '2026-07-18T03:07:04.218423Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Dispenser: GameplayKit State Machine Basics](Dispenser-%20GameplayKit%20State%20Machine%20Basics.md)


[Next](Dispenser%20%28iOS%29-AppDelegate.swift.md)[Previous](Dispenser%20%28OS%20X%29-AppDelegate.swift.md)

# Dispenser (iOS)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UIViewController` subclass that stores references to game-wide input sources and managers.
*/

import UIKit
import SpriteKit

class GameViewController: UIViewController {
    // MARK: Properties

    let scene = GameScene(fileNamed: "GameScene")!

    // MARK: Methods

    override func viewDidLoad() {
        super.viewDidLoad()

        let skView = view as! SKView

        // Resize the scene to better use the device aspect ratio.
        let scaleFactor = scene.size.height / view.bounds.height
        // This app runs only in landscape, so height always determines scale.
        scene.scaleMode = .aspectFit
        scene.size.width = view.bounds.width * scaleFactor

        skView.presentScene(scene)

        // SpriteKit applies additional optimizations to improve rendering performance.
        skView.ignoresSiblingOrder = true
    }

    #if os(tvOS)
    /// SpriteKit doesn't automatically forward press events, so do that manually.
    override func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
        scene.pressesEnded(presses, with: event)
    }
    #endif
}
```

[Next](Dispenser%20%28iOS%29-AppDelegate.swift.md)[Previous](Dispenser%20%28OS%20X%29-AppDelegate.swift.md)

