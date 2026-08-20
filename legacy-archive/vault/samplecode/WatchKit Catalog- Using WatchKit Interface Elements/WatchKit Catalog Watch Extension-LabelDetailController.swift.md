---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_LabelDetailController_swift.html
archived_at: '2026-07-18T03:28:06.525208Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-SeparatorDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-NotificationController.swift.md)

# WatchKit Catalog Watch Extension/LabelDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays labels and specialized labels (Date and Timer).
 */

import WatchKit

class LabelDetailController: WKInterfaceController {
    @IBOutlet var coloredLabel: WKInterfaceLabel!
    @IBOutlet var ultralightLabel: WKInterfaceLabel!
    @IBOutlet var timer: WKInterfaceTimer!

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        coloredLabel.setTextColor(UIColor.purple)

        let font = UIFont.systemFont(ofSize: 16.0, weight: UIFontWeightUltraLight)
        let attrsDictionary = [NSFontAttributeName : font]
        let attrString = NSMutableAttributedString(string: "Ultra Light Label", attributes: attrsDictionary)
        ultralightLabel.setAttributedText(attrString)

        var components = DateComponents()
        components.day = 10
        components.month = 12
        components.year = 2016
        timer.setDate(Calendar.current.date(from: components)!)
        timer.start()
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-SeparatorDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-NotificationController.swift.md)

