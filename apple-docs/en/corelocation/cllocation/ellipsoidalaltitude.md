---
title: ellipsoidalAltitude
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/ellipsoidalaltitude
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/ellipsoidalaltitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/ellipsoidalaltitude.json'
content_hash: 'sha256:c421fd1a0002f6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# ellipsoidalAltitude

<sub>Instance Property</sub>

The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ellipsoidalAltitude: CLLocationDistance { get }
```

## Discussion

The [ellipsoidalAltitude](ellipsoidalaltitude.md) property represents the altitude above the WGS84 ellipsoid associated with a location. Use the [ellipsoidalAltitude](ellipsoidalaltitude.md) property when your geodetic application needs an altitude with respect to a standard reference frame. Use [altitude](altitude.md) if your application needs an altitude with respect to the approximate mean sea level.

The [ellipsoidalAltitude](ellipsoidalaltitude.md) value is valid if [verticalAccuracy](verticalaccuracy.md) is greater than `0`, and invalid if [verticalAccuracy](verticalaccuracy.md) is `0` or below. If [verticalAccuracy](verticalaccuracy.md) is `0` or below, [ellipsoidalAltitude](ellipsoidalaltitude.md) is invalid and contains the value `0.0`.

Valid values for [ellipsoidalAltitude](ellipsoidalaltitude.md) can be positive or negative. Positive values indicate altitudes above the ellipsoid. Negative values indicate altitudes below the ellipsoid.

## See Also

### Getting the location attributes

- [coordinate](coordinate.md) — The geographical coordinate information.
- [altitude](altitude.md) — The altitude above mean sea level associated with a location, measured in meters.
- [CLLocationDistance](../cllocationdistance.md) — A distance in meters from an existing location.
- [floor](floor.md) — The logical floor of the building in which the user is located.
- [timestamp](timestamp.md) — The time at which this location was determined.
- [sourceInformation](sourceinformation.md) — Information about the source that provides the location.
