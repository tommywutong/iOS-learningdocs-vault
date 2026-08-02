---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots__iOS__GameViewController_swift.html
archived_at: '2026-07-18T03:06:22.343243Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots%20%28iOS%29-AppDelegate.swift.md)[Previous](DemoBots%20%28tvOS%29-AppDelegate.swift.md)

# DemoBots (iOS)/GameViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UIViewController` subclass that stores references to game-wide input sources and managers.
*/

import UIKit
import SpriteKit

class GameViewController: UIViewController, SceneManagerDelegate {
    // MARK: Properties

    /// A placeholder logo view that is displayed before the home scene is loaded.
    @IBOutlet weak var logoView: UIImageView!

    /// A manager for coordinating scene resources and presentation.
    var sceneManager: SceneManager!

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        /*
            Set up the `touchControlInputNode` to cover the entire view, and
            size the controls to a reasonable value.
        */
        let viewSize = view.bounds.size
        let controlLength = min(GameplayConfiguration.TouchControl.minimumControlSize, viewSize.width * GameplayConfiguration.TouchControl.idealRelativeControlSize)
        let controlSize = CGSize(width: controlLength, height: controlLength)

        let touchControlInputNode = TouchControlInputNode(frame: view.bounds, thumbStickNodeSize: controlSize)
        let gameInput = GameInput(nativeControlInputSource: touchControlInputNode)

        // Load the initial home scene.
        let skView = view as! SKView
        sceneManager = SceneManager(presentingView: skView, gameInput: gameInput)
        sceneManager.delegate = self

        sceneManager.transitionToScene(identifier: .home)
    }

    // Hide status bar during game play.
    override var prefersStatusBarHidden: Bool {
        return true
    }

    // MARK: SceneManagerDelegate

    func sceneManager(_ sceneManager: SceneManager, didTransitionTo scene: SKScene) {
        // Fade out the app's initial loading `logoView` if it is visible.
        UIView.animate(withDuration: 0.2, delay: 0.0, options: [], animations: {
            self.logoView.alpha = 0.0
        }, completion: { _ in
            self.logoView.isHidden = true
        })
    }
}
```

[Next](DemoBots%20%28iOS%29-AppDelegate.swift.md)[Previous](DemoBots%20%28tvOS%29-AppDelegate.swift.md)

