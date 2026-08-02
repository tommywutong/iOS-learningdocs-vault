---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_ResultOrErrorViewController_swift.html
archived_at: '2026-07-18T03:03:29.168750Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithUserRecordIDSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NavigationController.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/ResultOrErrorViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This controller displays a result or an error and provides a common Done/Back action.
*/

import UIKit

class ResultOrErrorViewController: UIViewController {

    var isDrilldown = false

    var doneButton: UIBarButtonItem!

    override func viewDidLoad() {
        super.viewDidLoad()

        navigationItem.title = "Error"

        doneButton = UIBarButtonItem(title: "Done", style: .Done, target: self, action: #selector(ResultOrErrorViewController.backToCodeSample))

        if !isDrilldown {
            navigationItem.hidesBackButton = true
            navigationItem.rightBarButtonItem = doneButton
        }
    }

    func backToCodeSample() {
        dismissViewControllerAnimated(true, completion: nil)
    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-DiscoverUserInfoWithUserRecordIDSample.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-NavigationController.swift.md)

