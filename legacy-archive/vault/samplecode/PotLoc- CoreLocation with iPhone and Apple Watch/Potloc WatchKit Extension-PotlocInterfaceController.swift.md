---
title: 'PotLoc: CoreLocation with iPhone and Apple Watch'
apple_id: TP40016176
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: CoreLocation
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/PotLoc/Listings/Potloc_WatchKit_Extension_PotlocInterfaceController_swift.html
archived_at: '2026-07-18T03:19:30.323494Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PotLoc: CoreLocation with iPhone and Apple Watch](PotLoc-%20CoreLocation%20with%20iPhone%20and%20Apple%20Watch.md)


[Next](Potloc%20WatchKit%20Extension-RequestLocationInterfaceController.swift.md)[Previous](Potloc%20WatchKit%20Extension-PotlocComplicationController.swift.md)

# Potloc WatchKit Extension/PotlocInterfaceController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Default interface controller provided by the project. The interface associated with this controller
        has two buttons, each of which use push segues to transition to action interfaces.
*/

import WatchKit
import Foundation

class PotlocInterfaceController: WKInterfaceController {

    /// Label indicating that the following button correspond to actions that are performed on the apple watch
    @IBOutlet var appleWatchLabel: WKInterfaceLabel!

    /// Label indicating that the following button corresponds to actions that require sending WatchConnectivity messages to the phone to trigger actions
    @IBOutlet var iPhoneLabel: WKInterfaceLabel!

    /// Button that leads to the Request interface
    @IBOutlet var requestButton: WKInterfaceButton!

    /// Button that leads to the Stream interface
    @IBOutlet var streamButton: WKInterfaceButton!

    // MARK: Localized String Convenience

    var appleWatchText: String {
        return NSLocalizedString("Watch", comment: "Apple Watch official name")
    }

    var iPhoneText: String {
        return NSLocalizedString("iPhone", comment: "iPhone official name")
    }

    var requestTitle: String {
        return NSLocalizedString("Request", comment: "Indicates that pressing this button transitions to the Request interface")
    }

    var streamTitle: String {
        return NSLocalizedString("Stream", comment: "Indicates that pressing this button transitions to the Stream interface")
    }

    // MARK: Interface Controller

    override func awake(withContext context: Any?) {
        super.awake(withContext: context)

        appleWatchLabel.setText(appleWatchText)
        iPhoneLabel.setText(iPhoneText)

        requestButton.setTitle(requestTitle)
        streamButton.setTitle(streamTitle)
    }
}
```

[Next](Potloc%20WatchKit%20Extension-RequestLocationInterfaceController.swift.md)[Previous](Potloc%20WatchKit%20Extension-PotlocComplicationController.swift.md)

