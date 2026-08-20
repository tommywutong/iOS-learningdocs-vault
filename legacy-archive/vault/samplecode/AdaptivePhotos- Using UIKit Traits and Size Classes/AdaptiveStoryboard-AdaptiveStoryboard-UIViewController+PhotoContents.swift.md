---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_UIViewController_PhotoContents_swift.html
archived_at: '2026-07-18T03:00:45.174836Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveCode-AdaptiveCode-OverlayView.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-ListTableViewController.swift.md)

# AdaptiveStoryboard/AdaptiveStoryboard/UIViewController+PhotoContents.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
An extension that returns information about photos contained in view controllers.
*/

import UIKit

/*
    This extension is specific to this application. Some of the specific view
    controllers in the app override these to return the values that make sense for
    them.
*/
extension UIViewController {
    /*
        Returns the photo currently being displayed by the receiver, or `nil` if the
        receiver is not displaying a photo.
    */
    func containedPhoto() -> Photo? {
        // By default, view controllers don't contain photos.
        return nil
    }

    func containsPhoto(_ photo: Photo) -> Bool {
        // By default, view controllers don't contain photos.
        return false
    }

    func currentVisibleDetailPhotoWithSender(_ sender: AnyObject?) -> Photo? {
        // Look for a view controller that has a visible photo.
        if let target = targetViewController(forAction: #selector(UIViewController.currentVisibleDetailPhotoWithSender(_:)), sender: sender) {
            return target.currentVisibleDetailPhotoWithSender(sender)
        }
        else {
            return nil
        }
    }
}

extension UISplitViewController {
    override func currentVisibleDetailPhotoWithSender(_ sender: AnyObject?) -> Photo? {
        if isCollapsed {
            // If we're collapsed, we don't have a detail.
            return nil
        }
        else {
            // Otherwise, return our detail controller's contained photo (if any).
            let controller = viewControllers.last

            return controller?.containedPhoto()
        }
    }
}
```

[Next](AdaptiveCode-AdaptiveCode-OverlayView.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-ListTableViewController.swift.md)

