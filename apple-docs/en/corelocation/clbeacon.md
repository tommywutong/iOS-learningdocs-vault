---
title: CLBeacon
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeacon
source_url: 'https://developer.apple.com/documentation/corelocation/clbeacon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeacon.json'
content_hash: 'sha256:d4c339228452a4b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBeacon

<sub>Class</sub>

Information about an observed iBeacon device and its relative distance to a person’s device.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class CLBeacon
```

## Overview

The [CLBeacon](clbeacon.md) class represents a beacon that was observed during beacon ranging. You do not create instances of this class directly. The location manager ([CLLocationManager](cllocationmanager.md)) object reports observed beacons to its associated delegate object.

The identity of a beacon is defined by its [UUID](clbeacon/uuid.md), [major](clbeacon/major.md), and [minor](clbeacon/minor.md) properties. These values are coded into the beacon itself. For a more thorough description of the meaning of those values, see [CLBeaconRegion](clbeaconregion.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the beacon identity

- [UUID](clbeacon/uuid.md) — The UUID that the observed beacon transmitted.
- [major](clbeacon/major.md) — The major value that the observed beacon transmitted.
- [minor](clbeacon/minor.md) — The minor value that the observed beacon transmitted.
- [proximityUUID](clbeacon/proximityuuid.md) — The proximity ID of the beacon. _(deprecated)_

### Determining the distance to the beacon

- [proximity](clbeacon/proximity.md) — The relative distance to the beacon.
- [CLProximity](clproximity.md) — Constants that reflect the relative distance to a beacon.
- [accuracy](clbeacon/accuracy.md) — The accuracy of the proximity value, measured in meters from the beacon.
- [rssi](clbeacon/rssi.md) — The received signal strength of the beacon, measured in decibels.

### Getting the observation timestamp

- [timestamp](clbeacon/timestamp.md) — A timestamp representing when the beacon was observed.

### Initializers

- [init(coder:)](<clbeacon/init(coder_).md>)

## See Also

### iBeacon

- [Ranging for Beacons](ranging-for-beacons.md) — Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md) — Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md) — Broadcast iBeacon signals from an iOS device.
- [CLCondition](clcondition-swift.protocol.md) — The abstract base class for all other monitor conditions.
