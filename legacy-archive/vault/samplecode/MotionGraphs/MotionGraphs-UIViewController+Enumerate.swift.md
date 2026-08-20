---
title: MotionGraphs
apple_id: DTS40012333
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2017-02-02'
source_url: https://developer.apple.com/library/archive/samplecode/MotionGraphs/Listings/MotionGraphs_UIViewController_Enumerate_swift.html
archived_at: '2026-07-18T03:16:02.064022Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MotionGraphs](MotionGraphs.md)


[Next](README.md.md)[Previous](MotionGraphs-CGContext%2BGraphLines.swift.md)

# MotionGraphs/UIViewController+Enumerate.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Extends `UIViewController` to add a method to enumerate through a view controller heirarchy.
 */

import UIKit

extension UIViewController {
    /// Executes the specified closure for each of the child and descendant view
    /// controller, as well as for the view controller itself.
    func enumerateHierarchy(_ closure: (UIViewController) -> Void) {
        closure(self)

        for child in childViewControllers {
            child.enumerateHierarchy(closure)
        }

    }
}
```

[Next](README.md.md)[Previous](MotionGraphs-CGContext%2BGraphLines.swift.md)

