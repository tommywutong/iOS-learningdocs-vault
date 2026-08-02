---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_CustomBackButton_CustomBackButtonDetailViewController_swift.html
archived_at: '2026-07-18T03:16:52.927491Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](Document%20Revision%20History.md)[Previous](NavBar-CustomBackButton-CustomBackButtonNavController.swift.md)

# NavBar/CustomBackButton/CustomBackButtonDetailViewController.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The detail view controller in the Custom Back Button example.
 */

import UIKit

class CustomBackButtonDetailViewController: UIViewController {

    @IBOutlet var cityLabel: UILabel!
    @objc var city: String?

    override func viewDidLoad() {
        super.viewDidLoad()

        cityLabel.text = city
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](NavBar-CustomBackButton-CustomBackButtonNavController.swift.md)

