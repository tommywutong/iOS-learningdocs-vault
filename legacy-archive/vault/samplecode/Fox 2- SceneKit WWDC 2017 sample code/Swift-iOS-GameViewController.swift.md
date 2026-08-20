---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_iOS_GameViewController_swift.html
archived_at: '2026-07-26T19:54:17.221373Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-iOS-AppDelegate.swift.md)[Previous](Swift-iOS-ButtonOverlay.swift.md)

# Swift/iOS/GameViewController.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's main view controller.
 */

import SceneKit
import UIKit

class GameViewControllerIOS: UIViewController {

    var gameView: SCNView {
        return view as! SCNView
    }

    var gameController: GameController?

    override func viewDidLoad() {
        super.viewDidLoad()

        // 1.3x on iPads
        if UIDevice.current.userInterfaceIdiom == .pad {
            self.gameView.contentScaleFactor = min(1.3, self.gameView.contentScaleFactor)
            self.gameView.preferredFramesPerSecond = 60
        }

        gameController = GameController(scnView: gameView)

        // Configure the view
        gameView.backgroundColor = UIColor.black
    }

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        if UIDevice.current.userInterfaceIdiom == .phone {
            return .allButUpsideDown
        } else {
            return .all
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

    override var prefersStatusBarHidden: Bool { return true }
    override var shouldAutorotate: Bool { return true }
}
```

[Next](Swift-iOS-AppDelegate.swift.md)[Previous](Swift-iOS-ButtonOverlay.swift.md)

