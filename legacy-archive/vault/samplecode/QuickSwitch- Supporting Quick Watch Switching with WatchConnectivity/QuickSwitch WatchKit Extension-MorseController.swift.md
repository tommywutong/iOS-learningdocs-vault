---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_WatchKit_Extension_MorseController_swift.html
archived_at: '2026-07-18T03:21:46.433557Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](QuickSwitch%20WatchKit%20Extension-DesignatorController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-DesignatorColorController.swift.md)

# QuickSwitch WatchKit Extension/MorseController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The `MorseController` shows up to the 10 most recently received morse codes from the phone.
 */

import WatchKit

class MorseRowController: NSObject {
    // MARK: Properties

    @IBOutlet weak var textLabel: WKInterfaceLabel!

    // MARK: Methods

    func setText(_ text: String) {
        textLabel.setText(text)
    }
}

class MorseController: WKInterfaceController {
    // MARK: Properties

    @IBOutlet weak var morseTable: WKInterfaceTable!

    override func awake(withContext context: Any?) {
        precondition(context is MorseContext, "Expected class of `context` to be `MorseContext`.")

        let morseContext = context as! MorseContext

        // pick up to the first 10 entries in the array
        let morseCodes = morseContext.morseCodes[0..<min(10, morseContext.morseCodes.count)]
        morseTable.setNumberOfRows(morseCodes.count, withRowType: "MorseRowType")

        morseCodes.enumerated().forEach { (index, item) in
            let row = self.morseTable.rowController(at: index) as! MorseRowController
            row.setText(item)
        }
    }
}

class MorseContext {
    let morseCodes: [String]

    init(morseCodes: [String]) {
        self.morseCodes = morseCodes
    }
}
```

[Next](QuickSwitch%20WatchKit%20Extension-DesignatorController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-DesignatorColorController.swift.md)

