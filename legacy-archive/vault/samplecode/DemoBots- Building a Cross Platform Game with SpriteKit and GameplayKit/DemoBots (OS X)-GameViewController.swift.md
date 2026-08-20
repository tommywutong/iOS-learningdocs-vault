---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots__OS_X__GameViewController_swift.html
archived_at: '2026-07-18T03:06:22.083278Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots%20%28OS%20X%29-GameWindowController.swift.md)[Previous](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)

# DemoBots (OS X)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An `NSViewController` subclass that stores references to game-wide input sources and managers.
*/

import Cocoa
import SpriteKit

class GameViewController: NSViewController {
    // MARK: Properties

    /// A manager for coordinating scene resources and presentation.
    var sceneManager: SceneManager!

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        let keyboardControlInputSource = KeyboardControlInputSource()
        let gameInput = GameInput(nativeControlInputSource: keyboardControlInputSource)

        // Load the initial home scene.
        let skView = view as! SKView
        sceneManager = SceneManager(presentingView: skView, gameInput: gameInput)

        sceneManager.transitionToScene(identifier: .home)
    }
}
```

[Next](DemoBots%20%28OS%20X%29-GameWindowController.swift.md)[Previous](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)

