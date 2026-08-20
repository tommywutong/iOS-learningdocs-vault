---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_PageController_swift.html
archived_at: '2026-07-18T03:28:06.705361Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-SliderDetailController.swift.md)[Previous](LICENSE.txt.md)

# WatchKit Catalog Watch Extension/PageController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller represents a single page of the modal page-based navigation controller, presented in ControllerDetailController.
 */

import WatchKit

class PageController: WKInterfaceController {
    @IBOutlet var pageLabel :WKInterfaceLabel!

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        pageLabel.setText(String(format:"%@ Page", context as! NSDictionary))
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-SliderDetailController.swift.md)[Previous](LICENSE.txt.md)

