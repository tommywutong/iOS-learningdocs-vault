---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_InterfaceController_swift.html
archived_at: '2026-07-18T03:28:06.475039Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-ImageDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TextInputController.swift.md)

# WatchKit Catalog Watch Extension/InterfaceController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This is the initial interface controller for the WatchKit app. It loads the initial table of the app with data and responds to Handoff launching the WatchKit app.
 */

import WatchKit
import WatchConnectivity

class InterfaceController: WKInterfaceController, WCSessionDelegate {
    @IBOutlet var interfaceTable: WKInterfaceTable!
    var elementsList: NSArray!

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)
        WCSession.default().delegate = self
        WCSession.default().activate()

        // Initialize variables here.
        // Configure interface objects here.


        // Retrieve the data. This could be accessed from the iOS app via a shared container.
        elementsList = NSArray(contentsOfFile: Bundle.main.path(forResource: "AppData", ofType: "plist")!)

        loadTableRows()
    }

    func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: Error?) {

    }

    override func handleUserActivity(_ userInfo: [AnyHashable : Any]?) {
        guard let userInfo = userInfo else { return }

        // Use data from the userInfo dictionary passed in to push to the appropriate controller with detailed info.
        pushController(withName: userInfo["controllerName"] as! String, context: userInfo["detailInfo"] as! String)
    }

    override func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int) {
        let rowData = elementsList[rowIndex] as! NSDictionary

        pushController(withName: rowData["controllerIdentifier"] as! String, context: nil)
    }

    func loadTableRows() {
        interfaceTable.setNumberOfRows(self.elementsList.count, withRowType: "default")

        // Create all of the table rows.
        for idx in 0 ... elementsList.count-1 {
            let elementRow = interfaceTable.rowController(at: idx) as! ElementRowController
            let rowData = elementsList[idx] as! NSDictionary
            elementRow.elementLabel.setText(rowData["label"] as? String)
        }
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-ImageDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-TextInputController.swift.md)

