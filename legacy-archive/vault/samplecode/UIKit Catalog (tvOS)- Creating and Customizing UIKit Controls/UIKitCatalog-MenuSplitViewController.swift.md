---
title: 'UIKit Catalog (tvOS): Creating and Customizing UIKit Controls'
apple_id: TP40016433
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: UIKit
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Listings/UIKitCatalog_MenuSplitViewController_swift.html
archived_at: '2026-07-18T03:27:29.080255Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UIKit Catalog (tvOS): Creating and Customizing UIKit Controls](UIKit%20Catalog%20%28tvOS%29-%20Creating%20and%20Customizing%20UIKit%20Controls.md)


[Next](UIKitCatalog-GradientMaskView.swift.md)[Previous](UIKitCatalog-FocusGuidesViewController.swift.md)

# UIKitCatalog/MenuSplitViewController.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `UISplitViewController` subclass that is used throughout the sample. Adds a method to allow its child view controllers to move focus from its master view controller to the detail view controller.
*/

import UIKit

class MenuSplitViewController: UISplitViewController {
    // MARK: Properties

    /**
        Set to true from `updateFocusToDetailViewController()` to indicate that
        the detail view controller should be the preferred focused view when
        this view controller is next queried.
    */
    private var preferDetailViewControllerOnNextFocusUpdate = false

    // MARK: UIFocusEnvironment

    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        let environments: [UIFocusEnvironment]

        /*
            Check if a request has been made to move the focus to the detail
            view controller.
        */
        if preferDetailViewControllerOnNextFocusUpdate, let detailViewController = viewControllers.last {
            environments = detailViewController.preferredFocusEnvironments
            preferDetailViewControllerOnNextFocusUpdate = false
        }
        else {
            environments = super.preferredFocusEnvironments
        }

        return environments
    }

    // MARK: Focus helpers

    /**
        Called from a containing `MenuTableViewController` whenever the user
        selects a table view row in a master view controller.
    */
    func updateFocusToDetailViewController() {
        preferDetailViewControllerOnNextFocusUpdate = true

        /*
            Trigger the focus system to re-query the view hierarchy for preferred
            focused views.
        */
        setNeedsFocusUpdate()
        updateFocusIfNeeded()
    }
}
```

[Next](UIKitCatalog-GradientMaskView.swift.md)[Previous](UIKitCatalog-FocusGuidesViewController.swift.md)

