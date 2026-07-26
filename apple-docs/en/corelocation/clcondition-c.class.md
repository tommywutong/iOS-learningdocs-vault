---
title: CLCondition
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clcondition-c.class
source_url: 'https://developer.apple.com/documentation/corelocation/clcondition-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcondition-c.class.json'
content_hash: 'sha256:5497f9a8203c4ba2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLCondition

<sub>Class</sub>

The abstract base class that all other conditions derive from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLCondition : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [CLBeaconIdentityCondition](clbeaconidentitycondition.md), [CLCircularGeographicCondition](clcirculargeographiccondition.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

### iBeacon

- [Ranging for Beacons](ranging-for-beacons.md) — Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md) — Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md) — Broadcast iBeacon signals from an iOS device.
- [CLBeacon](clbeacon.md) — Information about an observed iBeacon device and its relative distance to a person’s device.
- [CLBeaconIdentityCondition](clbeaconidentitycondition.md) — A condition that describes the identity characteristics of a beacon.
- [CLCircularGeographicCondition](clcirculargeographiccondition.md) — A circular geographic condition that a center point and radius define.
