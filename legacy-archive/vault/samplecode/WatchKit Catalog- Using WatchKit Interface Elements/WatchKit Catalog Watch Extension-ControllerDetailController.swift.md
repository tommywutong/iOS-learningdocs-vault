---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_ControllerDetailController_swift.html
archived_at: '2026-07-18T03:28:06.181896Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-TableDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-ImageDetailController.swift.md)

# WatchKit Catalog Watch Extension/ControllerDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller demonstrates how to present a modal controller with a page-based navigation style. By performing a Force Touch gesture on the controller (click-and-hold in the iOS Simulator), you can present a menu.
 */

import WatchKit

class ControllerDetailController: WKInterfaceController {

    @IBAction func presentPages() {
        let controllerNames = ["pageController", "pageController", "pageController", "pageController", "pageController"]
        let contexts = ["First", "Second", "Third", "Fourth", "Fifth"]

        presentController(withNames: controllerNames, contexts: contexts)
    }

    @IBAction func menuItemTapped() {
        print("A menu item was tapped.")
    }

}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-TableDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-ImageDetailController.swift.md)

