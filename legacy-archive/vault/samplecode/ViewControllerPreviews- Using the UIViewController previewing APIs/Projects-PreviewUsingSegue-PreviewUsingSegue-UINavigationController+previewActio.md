---
title: 'ViewControllerPreviews: Using the UIViewController previewing APIs'
apple_id: TP40016546
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ViewControllerPreviews/Listings/Projects_PreviewUsingSegue_PreviewUsingSegue_UINavigationController_previewActionItems_swift.html
archived_at: '2026-07-18T03:27:57.665865Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewControllerPreviews: Using the UIViewController previewing APIs](ViewControllerPreviews-%20Using%20the%20UIViewController%20previewing%20APIs.md)


[Next](Projects-PreviewUsingSegue-PreviewUsingSegue-DetailViewController.swift.md)[Previous](Projects-PreviewUsingSegue-PreviewUsingSegue-MainViewController.swift.md)

# Projects/PreviewUsingSegue/PreviewUsingSegue/UINavigationController+previewActionItems.swift

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An extension on UINavigationController to return the top view controller's previewActionItems by default.
*/

import UIKit

extension UINavigationController {
    /*
        Override the default implementation of `previewActionItems` to return the
        preview items for the controller's `topViewController`.
    */
    open override var previewActionItems : [UIPreviewActionItem] {
        if let items = self.topViewController?.previewActionItems {
            return items
        }
        else {
            return super.previewActionItems
        }
    }
}
```

[Next](Projects-PreviewUsingSegue-PreviewUsingSegue-DetailViewController.swift.md)[Previous](Projects-PreviewUsingSegue-PreviewUsingSegue-MainViewController.swift.md)

