---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_TextEntryMenuViewController_swift.html
archived_at: '2026-07-18T03:27:29.417607Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-DataItem.swift.md)[Previous](UIKitCatalog-AppDelegate.swift.md)

# UIKitCatalog/TextEntryMenuViewController.swift

```
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `MenuTableViewController` subclass for the "Text Entry" section of the app.
*/

import UIKit

class TextEntryMenuViewController: MenuTableViewController {
    // MARK: Properties

    override var segueIdentifierMap: [[String]] {
        return [
            [
                "ShowSimpleForm",
                "ShowAlertForm"
            ]
        ]
    }
}
```

[Next](UIKitCatalog-DataItem.swift.md)[Previous](UIKitCatalog-AppDelegate.swift.md)

