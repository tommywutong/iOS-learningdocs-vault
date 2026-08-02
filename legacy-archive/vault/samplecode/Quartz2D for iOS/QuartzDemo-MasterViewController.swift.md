---
title: Quartz2D for iOS
apple_id: DTS40007531
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzDemo/Listings/QuartzDemo_MasterViewController_swift.html
archived_at: '2026-07-18T03:21:34.572251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz2D for iOS](Quartz2D%20for%20iOS.md)


[Next](QuartzDemo-QuartzRectView.swift.md)[Previous](QuartzDemo-QuartzPolyViewController.swift.md)

# QuartzDemo/MasterViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewController for the QuartzDemo app.  Adapted from the 'Master-Detail Application' template in Xcode 8.3.2.
 */

import UIKit

class MasterViewController: UITableViewController {

    var objects = [Any]()
    static var first: Bool = true


    override func viewDidLoad() {
        super.viewDidLoad()

        // start with the lines view loaded
        if MasterViewController.first {
            performSegue(withIdentifier: "Lines", sender: self)
            MasterViewController.first = false
        }

    }

    override func viewWillAppear(_ animated: Bool) {
        clearsSelectionOnViewWillAppear = splitViewController!.isCollapsed
        super.viewWillAppear(animated)
    }


    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)


    }


}
```

[Next](QuartzDemo-QuartzRectView.swift.md)[Previous](QuartzDemo-QuartzPolyViewController.swift.md)

