---
title: proximity
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeacon/proximity
source_url: 'https://developer.apple.com/documentation/corelocation/clbeacon/proximity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeacon/proximity.json'
content_hash: 'sha256:f7f63140bc012e69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeacon](../clbeacon.md)

# proximity

<sub>Instance Property</sub>

The relative distance to the beacon.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var proximity: CLProximity { get }
```

## Discussion

The value in this property gives a general sense of the relative distance to the beacon. Use it to quickly identify beacons that are nearer to the user rather than farther away.

## See Also

### Determining the distance to the beacon

- [CLProximity](../clproximity.md) — Constants that reflect the relative distance to a beacon.
- [accuracy](accuracy.md) — The accuracy of the proximity value, measured in meters from the beacon.
- [rssi](rssi.md) — The received signal strength of the beacon, measured in decibels.
