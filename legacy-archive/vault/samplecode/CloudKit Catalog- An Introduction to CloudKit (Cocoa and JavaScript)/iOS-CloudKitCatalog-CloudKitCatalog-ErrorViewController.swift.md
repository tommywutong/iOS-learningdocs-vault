---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_ErrorViewController_swift.html
archived_at: '2026-07-18T03:03:28.050563Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CodeSampleViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SaveRecordSample.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/ErrorViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An ErrorViewController displays an NSError.
*/

import UIKit

class ErrorViewController: ResultOrErrorViewController {

    // Mark: - Properties

    @IBOutlet weak var errorCode: UILabel!

    @IBOutlet weak var errorText: UITextView!

    var error: NSError?

    override func viewDidLoad() {
        super.viewDidLoad()

        if let error = error {
            errorCode.text = "Error Code: \(error.code)"
            errorText.text = error.localizedDescription
            errorText.textContainer.lineFragmentPadding = 0;
            errorText.textContainerInset = UIEdgeInsetsZero;
        } else {
            errorCode.text = "An unexpected error occurred."
        }

    }


}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CodeSampleViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-SaveRecordSample.swift.md)

