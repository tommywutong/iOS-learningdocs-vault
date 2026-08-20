---
title: User Interface 3D Transforms
apple_id: TP40017624
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/UserInterface3DTransforms/Listings/UserInterface3DTransforms_ViewController_swift.html
archived_at: '2026-07-18T03:27:38.096131Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [User Interface 3D Transforms](User%20Interface%203D%20Transforms.md)


[Next](UserInterface3DTransforms-ContainerView.swift.md)[Previous](User%20Interface%203D%20Transforms.md)

# UserInterface3DTransforms/ViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The app's view controller.
 */

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        view.addSubview( SwitcherView( frame: UIScreen.main.bounds ) )
    }

    // Rotation is disabled for the purposes of this sample.
    override var shouldAutorotate: Bool {
        get { return false }
    }

    // Status bar is hidden for maximum visibility of the demonstration.
    override var prefersStatusBarHidden: Bool {
        get { return true }
    }

    // For the purposes of this sample, the controller locks orientation to portrait mode.
    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        get { return .portrait }
    }
}
```

[Next](UserInterface3DTransforms-ContainerView.swift.md)[Previous](User%20Interface%203D%20Transforms.md)

