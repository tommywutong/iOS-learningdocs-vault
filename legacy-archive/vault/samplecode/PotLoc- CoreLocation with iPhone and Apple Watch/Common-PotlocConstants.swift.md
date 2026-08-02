---
title: 'PotLoc: CoreLocation with iPhone and Apple Watch'
apple_id: TP40016176
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: CoreLocation
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/PotLoc/Listings/Common_PotlocConstants_swift.html
archived_at: '2026-07-18T03:19:29.968809Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PotLoc: CoreLocation with iPhone and Apple Watch](PotLoc-%20CoreLocation%20with%20iPhone%20and%20Apple%20Watch.md)


[Next](LICENSE.txt.md)[Previous](Potloc%20WatchKit%20Extension-RequestLocationInterfaceController.swift.md)

# Common/PotlocConstants.swift

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Constants used between the Potloc target and the Potloc WatchKit Extension target.

        The constants found in this file are used as keys and values in the dictionaries
        sent when using the WatchConnectivity methods to send and receive messages.
*/

/// Keys used by the dictionaries when communicating between the watch and the phone.
enum MessageKey: String {
    case command
    case stateUpdate
    case acknowledge = "ack"
    case locationCount
}

/// Used by the dicationaries when communicating between the watch and the phone.
enum MessageCommand: String {
    case sendLocationStatus
    case startUpdatingLocation
    case stopUpdatingLocation
}
```

[Next](LICENSE.txt.md)[Previous](Potloc%20WatchKit%20Extension-RequestLocationInterfaceController.swift.md)

