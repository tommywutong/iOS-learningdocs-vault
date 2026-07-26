---
title: CLCondition
framework: Core Location
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clcondition-swift.protocol
source_url: 'https://developer.apple.com/documentation/corelocation/clcondition-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcondition-swift.protocol.json'
content_hash: 'sha256:dead6d2b637f9532'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLCondition

<sub>Protocol</sub>

The abstract base class for all other monitor conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
protocol CLCondition : Decodable, Encodable, Sendable
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [BeaconIdentityCondition](clmonitor-2r51v/beaconidentitycondition.md), [CircularGeographicCondition](clmonitor-2r51v/circulargeographiccondition.md)

## See Also

### iBeacon

- [Ranging for Beacons](ranging-for-beacons.md) — Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md) — Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md) — Broadcast iBeacon signals from an iOS device.
- [CLBeacon](clbeacon.md) — Information about an observed iBeacon device and its relative distance to a person’s device.
