---
title: rssi
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeacon/rssi
source_url: 'https://developer.apple.com/documentation/corelocation/clbeacon/rssi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeacon/rssi.json'
content_hash: 'sha256:eeb901bb66b46651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeacon](../clbeacon.md)

# rssi

<sub>Instance Property</sub>

The received signal strength of the beacon, measured in decibels.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var rssi: Int { get }
```

## Discussion

This value is the average signal strength of the samples received since Core Location last reported the range of the beacon to your app.

Use this value for calibrating beacon transmission power.

## See Also

### Determining the distance to the beacon

- [proximity](proximity.md) — The relative distance to the beacon.
- [CLProximity](../clproximity.md) — Constants that reflect the relative distance to a beacon.
- [accuracy](accuracy.md) — The accuracy of the proximity value, measured in meters from the beacon.
