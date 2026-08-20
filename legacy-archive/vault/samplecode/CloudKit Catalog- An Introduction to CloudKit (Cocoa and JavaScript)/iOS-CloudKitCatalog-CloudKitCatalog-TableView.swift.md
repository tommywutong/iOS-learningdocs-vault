---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_TableView_swift.html
archived_at: '2026-07-18T03:03:29.632908Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-ResultsViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-BooleanFieldTableViewCell.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/TableView.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This customizes UITableView by removing the empty cells of a plain table and adjusting the background color
                of a grouped table.
*/

import UIKit

class TableView: UITableView {

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        if style == .Grouped {
            backgroundView = nil
            backgroundColor = UIColor(red: 0.95, green: 0.95, blue: 0.95, alpha: 1.0)
        } else if style == .Plain {
            tableFooterView = UIView()
        }
    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-ResultsViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-BooleanFieldTableViewCell.swift.md)

