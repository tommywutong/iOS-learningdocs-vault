---
title: CLProximity
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clproximity
source_url: 'https://developer.apple.com/documentation/corelocation/clproximity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clproximity.json'
content_hash: 'sha256:01a6dd980b597e83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLProximity

<sub>Enumeration</sub>

Constants that reflect the relative distance to a beacon.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum CLProximity
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Proximity Values

- [CLProximityUnknown](clproximity/unknown.md) — The proximity of the beacon could not be determined.
- [CLProximityImmediate](clproximity/immediate.md) — The beacon is in the user’s immediate vicinity.
- [CLProximityNear](clproximity/near.md) — The beacon is relatively close to the user.
- [CLProximityFar](clproximity/far.md) — The beacon is far away.

### Initializers

- [init(rawValue:)](<clproximity/init(rawvalue_).md>)

## See Also

### Determining the distance to the beacon

- [proximity](clbeacon/proximity.md) — The relative distance to the beacon.
- [accuracy](clbeacon/accuracy.md) — The accuracy of the proximity value, measured in meters from the beacon.
- [rssi](clbeacon/rssi.md) — The received signal strength of the beacon, measured in decibels.
