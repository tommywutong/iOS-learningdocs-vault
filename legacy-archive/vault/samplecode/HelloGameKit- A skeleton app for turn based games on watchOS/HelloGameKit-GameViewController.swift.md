---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_GameViewController_swift.html
archived_at: '2026-07-18T03:11:48.360333Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit-GameScene.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-GameModel.swift.md)

# HelloGameKit/GameViewController.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     Top level view controller that sets of the scene
 */

import UIKit
import SpriteKit
import GameplayKit

class GameViewController: UIViewController {
    // MARK: UIViewController Overrides

    override func viewDidLoad() {
        super.viewDidLoad()

        let scene = GKScene(fileNamed: "GameScene")!
        let sceneNode = scene.rootNode as! GameScene

        sceneNode.scaleMode = .aspectFill
        sceneNode.entities = scene.entities
        sceneNode.graphs = scene.graphs.map { return $0.value }

        let skView = view as! SKView
        skView.presentScene(sceneNode)

        skView.ignoresSiblingOrder = true

        skView.showsFPS = true
        skView.showsNodeCount = true
    }

    override var shouldAutorotate: Bool {
        return true
    }

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        if UIDevice.current.userInterfaceIdiom == .phone {
            return .allButUpsideDown
        }
        else {
            return .all
        }
    }

    override var prefersStatusBarHidden: Bool {
        return true
    }
}
```

[Next](HelloGameKit-GameScene.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-GameModel.swift.md)

