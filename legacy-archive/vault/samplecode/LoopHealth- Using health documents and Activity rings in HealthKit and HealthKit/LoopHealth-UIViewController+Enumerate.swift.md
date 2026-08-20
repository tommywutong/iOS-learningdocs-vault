---
title: 'LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI'
apple_id: TP40017553
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: null
published: '2016-12-02'
source_url: https://developer.apple.com/library/archive/samplecode/LoopHealth/Listings/LoopHealth_UIViewController_Enumerate_swift.html
archived_at: '2026-07-18T03:13:50.286816Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI](LoopHealth-%20Using%20health%20documents%20and%20Activity%20rings%20in%20HealthKit%20and%20HealthKit.md)


[Next](LoopHealth-DashboardViewController.swift.md)[Previous](LoopHealth-HealthStoreContainer.swift.md)

# LoopHealth/UIViewController+Enumerate.swift

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
    /// controllers, as well as for the view controller itself.
    func enumerateHierarchy(_ closure: (UIViewController) -> Void) {
        closure(self)

        for child in childViewControllers {
            child.enumerateHierarchy(closure)
        }
    }
}
```

[Next](LoopHealth-DashboardViewController.swift.md)[Previous](LoopHealth-HealthStoreContainer.swift.md)

