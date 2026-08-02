---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_DataItemViewController_swift.html
archived_at: '2026-07-18T03:27:28.728326Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-ViewControllersMenuViewController.swift.md)[Previous](UIKitCatalog-MenuTableViewController.swift.md)

# UIKitCatalog/DataItemViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A view controller that displays the image for a `DataItem`. An instance of this class is created for each page of `PageViewController`.
*/

import UIKit

class DataItemViewController: UIViewController {
    // MARK: Properties

    static let storyboardIdentifier = "DataItemViewController"

    @IBOutlet var imageView: UIImageView!

    private(set) var dataItem: DataItem!

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        if let image = UIImage(named: dataItem.largeImageName) {
            imageView.image = image
        }
        else {
            imageView.image = UIImage(named: dataItem.imageName)
        }
    }

    // MARK: Convenience

    func configure(with dataItem: DataItem) {
        self.dataItem = dataItem
    }
}
```

[Next](UIKitCatalog-ViewControllersMenuViewController.swift.md)[Previous](UIKitCatalog-MenuTableViewController.swift.md)

