---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_LoadingViewController_swift.html
archived_at: '2026-07-18T03:03:28.584865Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordID.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKNotification.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/LoadingViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the loading view controller for showing an activity indicator and transitioning to a table of results or
                an error view.
*/

import UIKit

class LoadingViewController: UIViewController {

    @IBOutlet weak var activityIndicator: UIActivityIndicatorView!

    var results = Results()
    var codeSample: CodeSample?
    var error: NSError?

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicator.startAnimating()
    }

    // MARK: - Navigation

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if let spinner = activityIndicator {
            spinner.stopAnimating()
        }
        if segue.identifier == "ShowResult" {
            if let resultsViewController = segue.destinationViewController as? ResultsViewController {
                resultsViewController.codeSample = self.codeSample
                resultsViewController.results = self.results.items.count > 0 ? self.results : Results(items: [NoResults()])
            }
        } else if segue.identifier == "ShowError" {
            if let errorViewController = segue.destinationViewController as? ErrorViewController {
                errorViewController.error = self.error
            }
        }
    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-CKRecordID.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-CKNotification.swift.md)

