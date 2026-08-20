---
title: 'QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity'
apple_id: TP40016647
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: WatchConnectivity
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/QuickSwitch/Listings/QuickSwitch_WatchKit_Extension_DesignatorColorController_swift.html
archived_at: '2026-07-18T03:21:46.237417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QuickSwitch: Supporting Quick Watch Switching with WatchConnectivity](QuickSwitch-%20Supporting%20Quick%20Watch%20Switching%20with%20WatchConnectivity.md)


[Next](QuickSwitch%20WatchKit%20Extension-MorseController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-ExtensionDelegate.swift.md)

# QuickSwitch WatchKit Extension/DesignatorColorController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The `DesignatorColorController` allows selection of a designator from the NATO phonetic alphabet. `DesignatorColorController` has a delegate used to provide the user's selection back to the parent controller. The `ColorRowController` serves as the row controller for the table in the `DesignatorColorController`. Additionally, a `DesignatorColorContext` class is provided for use by segues transitioning to this controller.
*/

import WatchKit
import WatchConnectivity

class ColorRowController: NSObject {
    // MARK: Properties

    @IBOutlet weak var textLabel: WKInterfaceLabel!

    @IBOutlet weak var checkBox: WKInterfaceImage!

    // MARK: Methods

    func setText(_ text: String) {
        textLabel.setText(text)
    }

    func setCheckBoxImage(named imageName: String) {
        checkBox.setImageNamed(imageName)
    }
}

class DesignatorColorContext {
    weak var delegate: DesignatorColorControllerDelegate?
    let selectedRow: String

    init(selectedRow: String, delegate: DesignatorColorControllerDelegate) {
        self.selectedRow = selectedRow
        self.delegate = delegate
    }
}

protocol DesignatorColorControllerDelegate: class {
    func colorController(_ controller: DesignatorColorController, didSelect designatorColor: String)
}

class DesignatorColorController: WKInterfaceController {
    // MARK: Properties

    let rows = ["Blue", "Gray", "Green", "Orange", "Red", "Yellow"]

    @IBOutlet weak var colorTable: WKInterfaceTable!

    weak var delegate: DesignatorColorControllerDelegate?

    override init() {
        super.init()

        colorTable.setNumberOfRows(6, withRowType: "ColorRowType")

        rows.enumerated().forEach { (index, item) in
            let row = self.colorTable.rowController(at: index) as! ColorRowController

            row.setText(item)
            row.setCheckBoxImage(named: "\(item.lowercased())-unchecked")
        }
    }

    override func awake(withContext context: Any?) {
        precondition(context is DesignatorColorContext, "Expected class of `context` to be `ColorContext`.")

        let designatorColorContext = context as! DesignatorColorContext

        delegate = designatorColorContext.delegate

        let row = colorTable.rowController(at: rows.index(of: designatorColorContext.selectedRow)!) as! ColorRowController
        row.setCheckBoxImage(named: "\(designatorColorContext.selectedRow.lowercased())-checked")
    }

    override func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int) {
        let row = self.colorTable.rowController(at: rowIndex) as! ColorRowController

        let item = rows[rowIndex]

        row.setCheckBoxImage(named: "\(item.lowercased())-checked")
        delegate?.colorController(self, didSelect: item)
    }
}
```

[Next](QuickSwitch%20WatchKit%20Extension-MorseController.swift.md)[Previous](QuickSwitch%20WatchKit%20Extension-ExtensionDelegate.swift.md)

