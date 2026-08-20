---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_ButtonDetailController_swift.html
archived_at: '2026-07-18T03:28:06.138991Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-MapDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TableDetailController.swift.md)

# WatchKit Catalog Watch Extension/ButtonDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays buttons and shows use of groups within buttons. This also demonstrates how to hide and show UI elements at runtime.
 */

import WatchKit

class ButtonDetailController: WKInterfaceController {
    @IBOutlet var defaultButton :WKInterfaceButton!
    @IBOutlet var hiddenButton :WKInterfaceButton!
    @IBOutlet var placeholderButton :WKInterfaceButton!
    @IBOutlet var alphaButton :WKInterfaceButton!
    var hidden :Bool
    var placeholderAlpha :CGFloat

    override init() {
        hidden = false
        placeholderAlpha = 1.0
    }

    @IBAction func hideAndShow() {
        placeholderButton.setHidden(!hidden)
        hidden = !hidden
    }

    @IBAction func changeAlpha() {
        placeholderButton.setAlpha(placeholderAlpha == 1.0 ? 0.0 : 1.0)
        placeholderAlpha = (placeholderAlpha == 1.0 ? 0.0 : 1.0)
    }

}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-MapDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TableDetailController.swift.md)

