---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Swift_tvOS_GameViewController_swift.html
archived_at: '2026-07-26T19:54:17.174307Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Swift-tvOS-AppDelegate.swift.md)[Previous](Objective-C-fox2%20tvOS-AAPLGameViewController.h.md)

# Swift/tvOS/GameViewController.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's main view controller.
 */

import SceneKit
import UIKit

class GameViewControllerTVOS: UIViewController {
    var gameView: SCNView! {
        return view as! SCNView
    }
    var gameController: GameController?

    override func viewDidLoad() {
        super.viewDidLoad()
        gameController = GameController(scnView: gameView)

        // Configure the view
        gameView!.backgroundColor = UIColor.black
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Release any cached data, images, etc that aren't in use.
    }
}
```

[Next](Swift-tvOS-AppDelegate.swift.md)[Previous](Objective-C-fox2%20tvOS-AAPLGameViewController.h.md)

