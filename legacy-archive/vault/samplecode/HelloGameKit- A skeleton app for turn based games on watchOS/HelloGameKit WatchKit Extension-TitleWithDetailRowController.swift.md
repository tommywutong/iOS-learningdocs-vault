---
title: 'HelloGameKit: A skeleton app for turn based games on watchOS'
apple_id: TP40017337
resource_type: Sample Code
platform: watchOS
topic: null
technology: GameCenter
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGameKit/Listings/HelloGameKit_WatchKit_Extension_TitleWithDetailRowController_swift.html
archived_at: '2026-07-18T03:11:49.193835Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGameKit: A skeleton app for turn based games on watchOS](HelloGameKit-%20A%20skeleton%20app%20for%20turn%20based%20games%20on%20watchOS.md)


[Next](HelloGameKit%20WatchKit%20Extension-Move.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-PlayersInterfaceController.swift.md)

# HelloGameKit WatchKit Extension/TitleWithDetailRowController.swift

```swift
/*
     Copyright (C) 2016 Apple Inc. All Rights Reserved.
     See LICENSE.txt for this sample’s licensing information

     Abstract:
     Row controller for showing a simple title and detail table row.
 */

import WatchKit

@objc class TitleWithDetailRowController: NSObject {
    // MARK: IB Outlets

    @IBOutlet weak var titleLabel: WKInterfaceLabel!
    @IBOutlet weak var detailLabel: WKInterfaceLabel!
}
```

[Next](HelloGameKit%20WatchKit%20Extension-Move.swift.md)[Previous](HelloGameKit%20WatchKit%20Extension-PlayersInterfaceController.swift.md)

