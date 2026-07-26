---
title: notifyEntryStateOnDisplay
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeaconregion/notifyentrystateondisplay
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/notifyentrystateondisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/notifyentrystateondisplay.json'
content_hash: 'sha256:0115523d3e6effa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# notifyEntryStateOnDisplay

<sub>Instance Property</sub>

A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var notifyEntryStateOnDisplay: Bool { get set }
```

## Discussion

When you set this to [true](../../swift/true.md), the location manager sends beacon notifications when the user turns on the display and the device is already inside the region. These are notifications the framework sends even if your app isn’t running. In that situation, the system launches your app into the background so that it can handle the notifications. In both situations, the location manager calls the [- locationManager:didDetermineState:forRegion:](<../cllocationmanagerdelegate/locationmanager(__diddeterminestate_for_).md>) method of its delegate object.

The default value for this property is [false](../../swift/false.md).
