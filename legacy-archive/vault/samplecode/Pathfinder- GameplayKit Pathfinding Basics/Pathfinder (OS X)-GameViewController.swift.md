---
title: 'Pathfinder: GameplayKit Pathfinding Basics'
apple_id: TP40016461
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: GameplayKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/Pathfinder_GameplayKit/Listings/Pathfinder__OS_X__GameViewController_swift.html
archived_at: '2026-07-18T03:18:48.214464Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Pathfinder: GameplayKit Pathfinding Basics](Pathfinder-%20GameplayKit%20Pathfinding%20Basics.md)


[Next](Pathfinder%20%28OS%20X%29-AppDelegate.swift.md)[Previous](README.md.md)

# Pathfinder (OS X)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `NSViewController` subclass that stores references to game-wide input sources and managers.
*/

import SpriteKit

class GameViewController: NSViewController {
    // MARK: Properties

    let scene = GameScene(fileNamed: "GameScene")!

    // MARK: Methods

    override func viewDidLoad() {
        super.viewDidLoad()

        let skView = view as! SKView

        // Set the scale mode to scale to fit the window.
        scene.scaleMode = .aspectFit

        skView.presentScene(scene)

        // SpriteKit applies additional optimizations to improve rendering performance.
        skView.ignoresSiblingOrder = true
    }
}
```

[Next](Pathfinder%20%28OS%20X%29-AppDelegate.swift.md)[Previous](README.md.md)

