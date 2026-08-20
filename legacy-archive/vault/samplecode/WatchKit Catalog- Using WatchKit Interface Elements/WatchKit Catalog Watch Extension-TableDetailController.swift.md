---
title: 'WatchKit Catalog: Using WatchKit Interface Elements'
apple_id: TP40015046
resource_type: Sample Code
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/WKInterfaceCatalog/Listings/WatchKit_Catalog_Watch_Extension_TableDetailController_swift.html
archived_at: '2026-07-18T03:28:06.863294Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WatchKit Catalog: Using WatchKit Interface Elements](WatchKit%20Catalog-%20Using%20WatchKit%20Interface%20Elements.md)


[Next](WatchKit%20Catalog%20Watch%20Extension-ButtonDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-ControllerDetailController.swift.md)

# WatchKit Catalog Watch Extension/TableDetailController.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This controller displays a table with rows. This controller demonstrates how to insert rows after the intial set of rows has been added and displayed.
 */

import WatchKit

class TableDetailController: WKInterfaceController {
    @IBOutlet var interfaceTable :WKInterfaceTable!
    var cityNames :NSArray = ["Cupertino", "Sunnyvale", "Campbell", "Morgan Hill", "Mountain View"]

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        interfaceTable.setNumberOfRows(cityNames.count, withRowType:"default")

        for idx in 0 ... cityNames.count-1 {
            let row = interfaceTable.rowController(at: idx) as! TableRowController
            let cityName = cityNames[idx] as? String
            row.rowLabel.setText(cityName)
        }
    }

    override func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int) {
        let newCityNames = ["Saratoga", "San Jose"]

        let newCityIndexes = NSIndexSet(indexesIn: NSMakeRange(rowIndex + 1, newCityNames.count))

        // Insert new rows into the table.
        interfaceTable.insertRows(at: newCityIndexes as IndexSet, withRowType: "default")

        // Update the rows that were just inserted with the appropriate data.
        var newCityNumber = 0

        for idx in 0 ... newCityIndexes.count-1 {
            let newCityName = newCityNames[newCityNumber]
            let row = interfaceTable.rowController(at: idx) as! TableRowController
            row.rowLabel.setText(newCityName)
            newCityNumber += 1
        }
    }
}
```

[Next](WatchKit%20Catalog%20Watch%20Extension-ButtonDetailController.swift.md)[Previous](WatchKit%20Catalog%20Watch%20Extension-ControllerDetailController.swift.md)

