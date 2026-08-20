---
title: 'AdaptivePhotos: Using UIKit Traits and Size Classes'
apple_id: TP40014636
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdaptivePhotos/Listings/AdaptiveStoryboard_AdaptiveStoryboard_UIViewController_ViewControllerShowing_swift.html
archived_at: '2026-07-18T03:00:45.226081Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AdaptivePhotos: Using UIKit Traits and Size Classes](AdaptivePhotos-%20Using%20UIKit%20Traits%20and%20Size%20Classes.md)


[Next](AdaptiveStoryboard-AdaptiveStoryboard-ConversationViewController.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-AppDelegate.swift.md)

# AdaptiveStoryboard/AdaptiveStoryboard/UIViewController+ViewControllerShowing.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
An extension that gives information about how view controllers will be shown, for determining disclosure indicator visibility and row deselection.
*/

import UIKit

extension UIViewController {
    /**
        Returns whether calling `showViewController(_:sender:)` would cause a
        navigation "push" to occur.
    */
    func willShowingViewControllerPushWithSender(_ sender: AnyObject?) -> Bool {
        // Find and ask the right view controller about showing.
        if let target = targetViewController(forAction: #selector(UIViewController.willShowingViewControllerPushWithSender(_:)), sender: sender) {
            return target.willShowingViewControllerPushWithSender(sender)
        }

        // Or if we can't find one, we won't be pushing.
        return false
    }

    /**
        Returns whether calling `showDetailViewController(_:sender:)` would cause a
        navigation "push" to occur.
    */
    func willShowingDetailViewControllerPushWithSender(_ sender: AnyObject?) -> Bool {
        // Find and ask the right view controller about showing.
        if let target = targetViewController(forAction: #selector(UIViewController.willShowingDetailViewControllerPushWithSender(_:)), sender: sender) {
            return target.willShowingDetailViewControllerPushWithSender(sender)
        }

        // Or if we can't find one, we won't be pushing.
        return false
    }
}

extension UINavigationController {
    override func willShowingViewControllerPushWithSender(_ sender: AnyObject?) -> Bool {
        // Navigation Controllers always push for `showViewController(_:sender:)`.
        return true
    }
}

extension UISplitViewController {
    override func willShowingViewControllerPushWithSender(_ sender: AnyObject?) -> Bool {
        // Split View Controllers never push for `showViewController(_:sender:)`.
        return false
    }

    override func willShowingDetailViewControllerPushWithSender(_ sender: AnyObject?) -> Bool {
        if isCollapsed {
            /*
                If we're collapsed, re-ask this question as `showViewController(_:sender:)`
                to our primary view controller.
            */
            let target = viewControllers.last

            return target?.willShowingViewControllerPushWithSender(sender) ?? false
        }

        // Otherwise, we don't push for `showDetailViewController(_:sender:)`.
        return false
    }
}
```

[Next](AdaptiveStoryboard-AdaptiveStoryboard-ConversationViewController.swift.md)[Previous](AdaptiveStoryboard-AdaptiveStoryboard-AppDelegate.swift.md)

