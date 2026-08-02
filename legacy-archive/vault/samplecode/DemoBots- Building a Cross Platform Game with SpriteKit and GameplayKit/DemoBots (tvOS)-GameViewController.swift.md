---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots__tvOS__GameViewController_swift.html
archived_at: '2026-07-18T03:06:22.537241Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots%20%28tvOS%29-AppDelegate.swift.md)[Previous](README.md.md)

# DemoBots (tvOS)/GameViewController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A `GCEventViewController` subclass that allows the user to exit the app via the menu button by setting `controllerUserInteractionEnabled` to `true` when transitioning to the `HomeEndScene`.
*/

import SpriteKit
import GameController

class GameViewController: GCEventViewController, SceneManagerDelegate {
    // MARK: Properties

    /// A manager for coordinating scene resources and presentation.
    var sceneManager: SceneManager!

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        // `GameInput` will be updated with notifications from paired game controllers.
        let gameInput = GameInput()

        // Load the initial home scene.
        let skView = view as! SKView
        sceneManager = SceneManager(presentingView: skView, gameInput: gameInput)
        sceneManager.delegate = self

        sceneManager.transitionToScene(identifier: .home)
    }

    // MARK: SceneManagerDelegate

    func sceneManager(_ sceneManager: SceneManager, didTransitionTo scene: SKScene) {
        /*
            When transitioning to the `HomeEndScene` set
            `controllerUserInteractionEnabled` to `true` to allow the
            user to exit the app with the menu button. 

            Otherwise, setting `controllerUserInteractionEnabled` to false 
            will not direct game controller events through the UIEvent & UIResponder chain.

            @see GCEventViewController
        */
        controllerUserInteractionEnabled = (scene is HomeEndScene)
    }
}
```

[Next](DemoBots%20%28tvOS%29-AppDelegate.swift.md)[Previous](README.md.md)

