---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_DeviceDetailController_swift.html
archived_at: '2026-07-18T03:28:06.284818Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-TextInputController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-GroupDetailController.swift.md)

# WatchKit Catalog Watch Extension/DeviceDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays device specific information to use for ensuring a great experience to the wearer of the WatchKit app.
 */

import WatchKit

class DeviceDetailController: WKInterfaceController {
    @IBOutlet var boundsLabel :WKInterfaceLabel!
    @IBOutlet var scaleLabel :WKInterfaceLabel!
    @IBOutlet var preferredContentSizeLabel :WKInterfaceLabel!

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)
        let bounds = WKInterfaceDevice.current().screenBounds
        let scale = WKInterfaceDevice.current().screenScale

        boundsLabel.setText(NSStringFromCGRect(bounds))
        scaleLabel.setText(NSString(format:"%f",scale) as String)
        preferredContentSizeLabel.setText(WKInterfaceDevice.current().preferredContentSizeCategory)
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-TextInputController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-GroupDetailController.swift.md)

