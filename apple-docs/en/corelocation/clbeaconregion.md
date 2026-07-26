---
title: CLBeaconRegion
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeaconregion
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion.json'
content_hash: 'sha256:975d6fe14a88a4b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBeaconRegion

<sub>Class</sub>

A region for detecting the presence of iBeacon devices.

> [!warning] Deprecated
> Use [CLBeaconIdentityCondition](clbeaconidentitycondition.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class CLBeaconRegion
```

## Overview

A [CLBeaconRegion](clbeaconregion.md) object defines a region that you use to detect Bluetooth beacons conforming to the iBeacon specification. In contrast to a [CLCircularRegion](clcircularregion.md) that centers on a geographic location, a [CLBeaconRegion](clbeaconregion.md) focuses on an iBeacon with specific identifying characteristics, which you provide. When a matching device comes in range, Core Location notifies your app.

You monitor beacon regions in two ways. To detect when a beacon is in range, use the [- startMonitoringForRegion:](<cllocationmanager/startmonitoring(for_).md>) method of your location manager object. After detecting a beacon, call the [- startRangingBeaconsInRegion:](<cllocationmanager/startrangingbeacons(in_).md>) method to determine the relative distance to that beacon.

When detecting an iBeacon, you need to specify the [proximityUUID](clbeaconregion/proximityuuid.md), [major](clbeaconregion/major.md), and [minor](clbeaconregion/minor.md) values that you programmed into the beacon hardware. You use the values to identify your beacons uniquely, and you can specify a subset of values to detect multiple beacons. The [proximityUUID](clbeaconregion/proximityuuid.md) property is typically the same for all of the beacons in your installation. Use the [major](clbeaconregion/major.md) and [minor](clbeaconregion/minor.md) values to distinguish among different beacons in your installation.

If you want to configure the current iOS device as a Bluetooth beacon, create a beacon region with the appropriate identifying information. You can then call the [- peripheralDataWithMeasuredPower:](<clbeaconregion/peripheraldata(withmeasuredpower_).md>) method of the region to get a dictionary that you can use to advertise the device with the Core Bluetooth framework. For more information about using that framework to advertise the device as a beacon, see [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md).

For information about how to detect beacons, see [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md).

## Relationships

- **Inherits From**: [CLRegion](clregion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a beacon region

- [- initWithBeaconIdentityConstraint:identifier:](<clbeaconregion/init(beaconidentityconstraint_identifier_).md>) — Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints. _(deprecated)_
- [- initWithUUID:identifier:](<clbeaconregion/init(uuid_identifier_)-6hg8v.md>) — Creates and returns a region object that targets beacons with the specified UUID. _(deprecated)_
- [- initWithUUID:major:identifier:](<clbeaconregion/init(uuid_major_identifier_)-8ur0j.md>) — Creates and returns a region object that targets beacons with the specified UUID and major value. _(deprecated)_
- [- initWithUUID:major:minor:identifier:](<clbeaconregion/init(uuid_major_minor_identifier_)-24h7w.md>) — Creates and returns a region object that targets beacons with the specified UUID, and major and minor values. _(deprecated)_
- [CLBeaconMajorValue](clbeaconmajorvalue.md) — The most significant value in a beacon.
- [CLBeaconMinorValue](clbeaconminorvalue.md) — The least significant value in a beacon.

### Getting the beacon identity

- [UUID](clbeaconregion/uuid.md) — The UUID value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [major](clbeaconregion/major.md) — The major value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [minor](clbeaconregion/minor.md) — The minor value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [beaconIdentityConstraint](clbeaconregion/beaconidentityconstraint.md) — The beacon identity constraint that defines the beacon region. _(deprecated)_

### Specifying when to send notifications

- [notifyEntryStateOnDisplay](clbeaconregion/notifyentrystateondisplay.md) — A Boolean value that indicates whether Core Location sends beacon notifications when the device’s display is on. _(deprecated)_

### Getting the beacon’s advertisement data

- [- peripheralDataWithMeasuredPower:](<clbeaconregion/peripheraldata(withmeasuredpower_).md>) — Retrieves data that you can use to advertise the current device as a beacon. _(deprecated)_

### Deprecated

- [- initWithProximityUUID:identifier:](<clbeaconregion/init(proximityuuid_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified UUID. _(deprecated)_
- [- initWithProximityUUID:major:identifier:](<clbeaconregion/init(proximityuuid_major_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified proximity ID and major value. _(deprecated)_
- [- initWithProximityUUID:major:minor:identifier:](<clbeaconregion/init(proximityuuid_major_minor_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value. _(deprecated)_
- [proximityUUID](clbeaconregion/proximityuuid.md) — The unique ID of the beacons you’re targeting. _(deprecated)_

### Initializers

- [init(UUID:identifier:)](<clbeaconregion/init(uuid_identifier_)-6114g.md>) _(deprecated)_
- [init(UUID:major:identifier:)](<clbeaconregion/init(uuid_major_identifier_)-71t0b.md>) _(deprecated)_
- [init(UUID:major:minor:identifier:)](<clbeaconregion/init(uuid_major_minor_identifier_)-9ejej.md>) _(deprecated)_

## See Also

### Classes

- [CLBeaconIdentityConstraint](clbeaconidentityconstraint.md) — Identity characteristics that can match one or more beacons. _(deprecated)_
- [CLCircularRegion](clcircularregion.md) — A circular geographic region that a center point and radius deine. _(deprecated)_
