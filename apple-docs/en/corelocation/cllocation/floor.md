---
title: floor
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/floor
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/floor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/floor.json'
content_hash: 'sha256:5da23119f8364e4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# floor

<sub>Instance Property</sub>

The logical floor of the building in which the user is located.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var floor: CLFloor? { get }
```

## Discussion

If floor information is not available for the current location, the value of this property is `nil`.

## See Also

### Getting the location attributes

- [coordinate](coordinate.md) — The geographical coordinate information.
- [altitude](altitude.md) — The altitude above mean sea level associated with a location, measured in meters.
- [ellipsoidalAltitude](ellipsoidalaltitude.md) — The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [CLLocationDistance](../cllocationdistance.md) — A distance in meters from an existing location.
- [timestamp](timestamp.md) — The time at which this location was determined.
- [sourceInformation](sourceinformation.md) — Information about the source that provides the location.
