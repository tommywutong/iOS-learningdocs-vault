---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_WatchKit_Extension_DesignatorController_swift.html
archived_at: '2026-07-18T03:21:46.285559Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](Document%20Revision%20History.md)[Previous](QuickSwitch%20WatchKit%20Extension-MorseController.swift.md)

# QuickSwitch WatchKit Extension/DesignatorController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `DesignatorController` allows selection of a designator from the NATO phonetic alphabet. `DesignatorController` has a delegate used to provide the user's selection back to the parent controller. Additionally, a `DesignatorContext` class is provided for use by segues transitioning to this controller.
*/

import WatchKit
import WatchConnectivity

protocol DesignatorControllerDelegate: class {
    func designatorController(_ controller: DesignatorController, didSelect designator: String)
}

class DesignatorController: WKInterfaceController {
    // MARK: Properties

    @IBOutlet var designatorPicker: WKInterfacePicker!

    let designators = [
        "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "x-ray", "yankee", "zulu"
    ]

    var currentDesignator: String?

    weak var delegate: DesignatorControllerDelegate?

    override init() {
        super.init()

        let items: [WKPickerItem] = designators.map {
            let item = WKPickerItem()
            item.title = $0
            return item
        }

        designatorPicker.setItems(items)
    }

    override func awake(withContext context: Any?) {
        precondition(context is DesignatorContext, "Expected class of `context` to be `DesignatorContext`.")

        let designatorContext = context as! DesignatorContext

        delegate = designatorContext.delegate

        currentDesignator = designatorContext.currentDesignator

        if let currentIndex = designators.index(of: designatorContext.currentDesignator) {
            designatorPicker.setSelectedItemIndex(currentIndex)
        }
    }

    @IBAction func designationSelected(index: Int) {
        let designator = designators[index]

        currentDesignator = designator
    }

    @IBAction func saveDesignator() {
        delegate?.designatorController(self, didSelect: currentDesignator!)
    }
}

class DesignatorContext {
    weak var delegate: DesignatorControllerDelegate?
    let currentDesignator: String

    init(currentDesignator: String, delegate: DesignatorControllerDelegate) {
        self.currentDesignator = currentDesignator
        self.delegate = delegate
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](QuickSwitch%20WatchKit%20Extension-MorseController.swift.md)

