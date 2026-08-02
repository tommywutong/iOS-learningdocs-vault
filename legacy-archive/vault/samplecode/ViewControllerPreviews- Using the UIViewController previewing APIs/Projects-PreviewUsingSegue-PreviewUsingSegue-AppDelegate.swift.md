---
title: 'ViewControllerPreviews: Using the UIViewController previewing APIs'
apple_id: TP40016546
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ViewControllerPreviews/Listings/Projects_PreviewUsingSegue_PreviewUsingSegue_AppDelegate_swift.html
archived_at: '2026-07-18T03:27:57.521763Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewControllerPreviews: Using the UIViewController previewing APIs](ViewControllerPreviews-%20Using%20the%20UIViewController%20previewing%20APIs.md)


[Next](Projects-PreviewUsingSegue-PreviewUsingSegue-MainViewController.swift.md)[Previous](Projects-PreviewUsingSegue-README.md.md)

# Projects/PreviewUsingSegue/PreviewUsingSegue/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate. Creates and holds onto the main window, and implements the split view controller delegate.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UISplitViewControllerDelegate {
    // MARK: Properties

    var window: UIWindow?

    // MARK: App Delegate

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        guard let splitViewController = self.window!.rootViewController as? UISplitViewController else { fatalError("Unexpected view controller setup") }

        splitViewController.delegate = self

        return true
    }

    // MARK: Split View Delegate

    func splitViewController(_ splitViewController: UISplitViewController, collapseSecondary secondaryViewController: UIViewController, onto primaryViewController: UIViewController) -> Bool {

        guard let secondaryAsNavController = secondaryViewController as? UINavigationController else { return false }
        guard let topAsDetailController = secondaryAsNavController.topViewController as? DetailViewController else { return false }

        // Return true if the `sampleTitle` has not been set, collapsing the secondary controller.
        return topAsDetailController.sampleTitle == nil
    }

}
```

[Next](Projects-PreviewUsingSegue-PreviewUsingSegue-MainViewController.swift.md)[Previous](Projects-PreviewUsingSegue-README.md.md)

