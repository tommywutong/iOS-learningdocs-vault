---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_GestureDetailController_swift.html
archived_at: '2026-07-18T03:28:06.366381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-ElementRowController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-MapDetailController.swift.md)

# WatchKit Catalog Watch Extension/GestureDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller demonstrates the various gesture types available in watchOS
 */
import WatchKit

class GestureDetailController : WKInterfaceController {
    @IBOutlet var tapGroup: WKInterfaceGroup!
    @IBOutlet var longPressGroup: WKInterfaceGroup!
    @IBOutlet var swipeGroup: WKInterfaceGroup!
    @IBOutlet var panGroup: WKInterfaceGroup!
    @IBOutlet var tapLabel: WKInterfaceLabel!
    @IBOutlet var longPressLabel: WKInterfaceLabel!
    @IBOutlet var swipeLabel: WKInterfaceLabel!
    @IBOutlet var panLabel: WKInterfaceLabel!
    var timer :Timer!

    @IBAction func tapRecognized(_ sender: AnyObject) {
        tapGroup.setBackgroundColor(UIColor.green)
        scheduleReset()
    }

    @IBAction func longPressRecognized(_ sender: AnyObject) {
        longPressGroup.setBackgroundColor(UIColor.green)
        scheduleReset()
    }

    @IBAction func swipeRecognized(_ sender: AnyObject) {
        swipeGroup.setBackgroundColor(UIColor.green)
        scheduleReset()
    }

    @IBAction func panRecognized(_ sender: AnyObject) {
        if let panGesture = sender as? WKPanGestureRecognizer {
            panGroup.setBackgroundColor(UIColor.green)
            panLabel.setText("offset: \(NSStringFromCGPoint(panGesture.translationInObject()))")
            scheduleReset()
        }
    }

    func scheduleReset() {
        if timer != nil {
            timer.invalidate()
        }
        timer = Timer(timeInterval: 1.0, target: self, selector: #selector(resetAllGroups), userInfo: nil, repeats: false)
        RunLoop.current.add(timer, forMode: .commonModes)
    }

    func resetAllGroups() {
        tapGroup.setBackgroundColor(UIColor.clear)
        longPressGroup.setBackgroundColor(UIColor.clear)
        swipeGroup.setBackgroundColor(UIColor.clear)
        panGroup.setBackgroundColor(UIColor.clear)
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-ElementRowController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-MapDetailController.swift.md)

