---
title: timestamp
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/timestamp
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/timestamp.json'
content_hash: 'sha256:cb6a8fe8c722b99f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# timestamp

<sub>Instance Property</sub>

The time at which this location was determined.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timestamp: Date { get }
```

## Discussion

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting the location attributes

- [coordinate](coordinate.md) — The geographical coordinate information.
- [altitude](altitude.md) — The altitude above mean sea level associated with a location, measured in meters.
- [ellipsoidalAltitude](ellipsoidalaltitude.md) — The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [CLLocationDistance](../cllocationdistance.md) — A distance in meters from an existing location.
- [floor](floor.md) — The logical floor of the building in which the user is located.
- [sourceInformation](sourceinformation.md) — Information about the source that provides the location.
