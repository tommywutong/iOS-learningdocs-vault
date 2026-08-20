---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/iOS_CloudKitCatalog_CloudKitCatalog_NavigationController_swift.html
archived_at: '2026-07-18T03:03:28.915054Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](iOS-CloudKitCatalog-CloudKitCatalog-ResultOrErrorViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-AppDelegate.swift.md)

# iOS/CloudKitCatalog/CloudKitCatalog/NavigationController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This navigation controller overrides prepareForSegue to run a code sample and show the results or an error.
*/

import UIKit

class NavigationController: UINavigationController {


    // MARK: - Navigation

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "ShowLoadingView", let selectedCodeSample = sender as? CodeSample {
            selectedCodeSample.run {
                (results,error) in
                if let navigationController = segue.destinationViewController as? UINavigationController, let loadingViewController = navigationController.topViewController as? LoadingViewController {
                    var segueIdenfier = "ShowResult"
                    if error != nil {
                        loadingViewController.error = error
                        segueIdenfier = "ShowError"
                    } else {
                        loadingViewController.results = results
                        loadingViewController.codeSample = selectedCodeSample
                    }
                    dispatch_async(dispatch_get_main_queue()) {
                        loadingViewController.performSegueWithIdentifier(segueIdenfier, sender: loadingViewController)
                    }
                }
            }
        }
    }

}
```

[Next](iOS-CloudKitCatalog-CloudKitCatalog-ResultOrErrorViewController.swift.md)[Previous](iOS-CloudKitCatalog-CloudKitCatalog-AppDelegate.swift.md)

