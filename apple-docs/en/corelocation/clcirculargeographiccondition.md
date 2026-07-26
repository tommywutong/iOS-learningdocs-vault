---
title: CLCircularGeographicCondition
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clcirculargeographiccondition
source_url: 'https://developer.apple.com/documentation/corelocation/clcirculargeographiccondition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcirculargeographiccondition.json'
content_hash: 'sha256:c4f94ab40df3bd73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLCircularGeographicCondition

<sub>Class</sub>

A circular geographic condition that a center point and radius define.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLCircularGeographicCondition : CLCondition
```

## Overview

Use `CLCircularGeographicCondition` to monitor events that occur in a circular geographic condition that you describe.

## Relationships

- **Inherits From**: [CLCondition](clcondition-c.class.md)

- **Conforms To**: [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a circular geographic condition

- [initWithCenter:radius:](clcirculargeographiccondition/initwithcenter_radius_.md) — Creates a new circular geographic condition with the center point and radius you provide.

### Instance properties

- [center](clcirculargeographiccondition/center.md) — The center of the circular geographic condition.
- [radius](clcirculargeographiccondition/radius.md) — The radius of the circular geographic condition.

## See Also

### iBeacon

- [Ranging for Beacons](ranging-for-beacons.md) — Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md) — Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md) — Broadcast iBeacon signals from an iOS device.
- [CLBeacon](clbeacon.md) — Information about an observed iBeacon device and its relative distance to a person’s device.
- [CLCondition](clcondition-c.class.md) — The abstract base class that all other conditions derive from.
- [CLBeaconIdentityCondition](clbeaconidentitycondition.md) — A condition that describes the identity characteristics of a beacon.
