---
title: 'ShapeEdit: Building a Simple iCloud Document App'
apple_id: TP40016100
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ShapeEdit/Listings/ShapeEdit_AppDelegate_swift.html
archived_at: '2026-07-18T03:23:43.100951Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ShapeEdit: Building a Simple iCloud Document App](ShapeEdit-%20Building%20a%20Simple%20iCloud%20Document%20App.md)


[Next](ShapeEdit-DocumentBrowser-DocumentBrowserViews.swift.md)[Previous](ShapeEdit-DocumentEditor-ShapeView.swift.md)

# ShapeEdit/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the application delegate and main entry point. It supports open in place to allow opening documents directly from other applications.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, UISplitViewControllerDelegate {
    // MARK: - Properties

    var window: UIWindow?

    // MARK: - UIApplicationDelegate

    func application(application: UIApplication, openURL url: NSURL, options: [String: AnyObject]) -> Bool {
        /*
            `options[UIApplicationOpenURLOptionsOpenInPlaceKey]` will be set if 
            the app doesn't need to make a copy of the document to open or edit it.
            For example, the document could be in the ubiquitous container of the
            application.
        */
        guard let shouldOpenInPlace = options[UIApplicationOpenURLOptionsOpenInPlaceKey] as? Bool else {
            return false
        }

        guard let navigation = window?.rootViewController as? UINavigationController else { 
            return false
        }

        guard let documentBrowserController = navigation.viewControllers.first as? DocumentBrowserController else { 
            return false
        }

        documentBrowserController.openDocumentAtURL(url, copyBeforeOpening: !shouldOpenInPlace.boolValue)

        return true
    }
}
```

[Next](ShapeEdit-DocumentBrowser-DocumentBrowserViews.swift.md)[Previous](ShapeEdit-DocumentEditor-ShapeView.swift.md)

