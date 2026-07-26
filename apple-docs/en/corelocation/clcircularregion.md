---
title: CLCircularRegion
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clcircularregion
source_url: 'https://developer.apple.com/documentation/corelocation/clcircularregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcircularregion.json'
content_hash: 'sha256:cf45eb233a9ba31f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLCircularRegion

<sub>Class</sub>

A circular geographic region that a center point and radius deine.

> [!warning] Deprecated
> Use [CLCircularGeographicCondition](clcirculargeographiccondition.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class CLCircularRegion
```

## Overview

The [CLCircularRegion](clcircularregion.md) class defines the location and boundaries for a circular geographic region. You can use instances of this class to define geofences for a specific location. The crossing of a geofence’s boundary causes the location manager to notify its delegate.

## Relationships

- **Inherits From**: [CLRegion](clregion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a circular region

- [- initWithCenter:radius:identifier:](<clcircularregion/init(center_radius_identifier_).md>) — Creates and returns a region object defining a circular geographic area. _(deprecated)_

### Getting the circle’s center and radius

- [center](clcircularregion/center.md) — The center point of the geographic area. _(deprecated)_
- [radius](clcircularregion/radius.md) — The radius (measured in meters) that defines the geographic area’s outer boundary. _(deprecated)_

### Performing hit testing in the region

- [- containsCoordinate:](<clcircularregion/contains(__).md>) — Returns a Boolean value indicating whether the geographic area contains the specified coordinate. _(deprecated)_

## See Also

### Classes

- [CLBeaconRegion](clbeaconregion.md) — A region for detecting the presence of iBeacon devices. _(deprecated)_
- [CLBeaconIdentityConstraint](clbeaconidentityconstraint.md) — Identity characteristics that can match one or more beacons. _(deprecated)_
