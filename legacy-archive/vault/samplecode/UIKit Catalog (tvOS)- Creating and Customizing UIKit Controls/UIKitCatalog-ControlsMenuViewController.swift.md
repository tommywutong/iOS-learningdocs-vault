---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_ControlsMenuViewController_swift.html
archived_at: '2026-07-18T03:27:28.543793Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-DataItem%2BImageName.swift.md)[Previous](UIKitCatalog-CollectionViewController.swift.md)

# UIKitCatalog/ControlsMenuViewController.swift

```
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `MenuTableViewController` subclass for the "Controls" section of the app.
*/

import UIKit

class ControlsMenuViewController: MenuTableViewController {
    // MARK: Properties

    override var segueIdentifierMap: [[String]] {
        return [
            [
                "ShowButtons",
                "ShowProgressViews",
                "ShowSegmentedControls"
            ]
        ]
    }
}
```

[Next](UIKitCatalog-DataItem%2BImageName.swift.md)[Previous](UIKitCatalog-CollectionViewController.swift.md)

