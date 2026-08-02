---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_SliderDetailController_swift.html
archived_at: '2026-07-18T03:28:06.777602Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-GroupDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-PageController.swift.md)

# WatchKit Catalog Watch Extension/SliderDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays sliders and their various configurations.
 */

import WatchKit

class SliderDetailController: WKInterfaceController {
    @IBOutlet var coloredSlider :WKInterfaceSlider!

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)
        coloredSlider.setColor(UIColor.red)
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-GroupDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-PageController.swift.md)

