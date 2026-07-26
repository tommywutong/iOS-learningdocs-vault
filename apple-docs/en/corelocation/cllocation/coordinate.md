---
title: coordinate
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/coordinate
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/coordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/coordinate.json'
content_hash: 'sha256:f365c32ce61391f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# coordinate

<sub>Instance Property</sub>

The geographical coordinate information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var coordinate: CLLocationCoordinate2D { get }
```

## Discussion

When running in the simulator, Core Location uses the values provided to it by the simulator. You must run your application on an iOS-based device to get the actual location of that device.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting the location attributes

- [altitude](altitude.md) — The altitude above mean sea level associated with a location, measured in meters.
- [ellipsoidalAltitude](ellipsoidalaltitude.md) — The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [CLLocationDistance](../cllocationdistance.md) — A distance in meters from an existing location.
- [floor](floor.md) — The logical floor of the building in which the user is located.
- [timestamp](timestamp.md) — The time at which this location was determined.
- [sourceInformation](sourceinformation.md) — Information about the source that provides the location.
