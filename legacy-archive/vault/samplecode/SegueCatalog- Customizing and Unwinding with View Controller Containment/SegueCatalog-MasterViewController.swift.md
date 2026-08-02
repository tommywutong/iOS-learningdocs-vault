---
title: 'SegueCatalog: Customizing and Unwinding with View Controller Containment'
apple_id: TP40016213
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SegueCatalog/Listings/SegueCatalog_MasterViewController_swift.html
archived_at: '2026-07-18T03:23:38.911719Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SegueCatalog: Customizing and Unwinding with View Controller Containment](SegueCatalog-%20Customizing%20and%20Unwinding%20with%20View%20Controller%20Containment.md)


[Next](README.md.md)[Previous](SegueCatalog-DetailViewControllers.swift.md)

# SegueCatalog/MasterViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The view controller used as the root of the split view's master-side navigation controller.
*/

import UIKit

class MasterViewController: UITableViewController {
    @IBAction func unwindInMaster(_ segue: UIStoryboardSegue)  {
        /*
            Empty. Exists solely so that "unwind in master" segues can
            find this instance as a destination.
        */
    }
}
```

[Next](README.md.md)[Previous](SegueCatalog-DetailViewControllers.swift.md)

