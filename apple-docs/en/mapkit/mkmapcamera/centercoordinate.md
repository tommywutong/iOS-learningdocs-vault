---
title: centerCoordinate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapcamera/centercoordinate
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapcamera/centercoordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapcamera/centercoordinate.json'
content_hash: 'sha256:073920e956060119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapCamera](../mkmapcamera.md)

# centerCoordinate

<sub>Instance Property</sub>

The map coordinate at the center of the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var centerCoordinate: CLLocationCoordinate2D { get set }
```

## Discussion

This point represents the coordinate on which the framework centers the map. When the camera pitch is `0`, this property also corresponds to the geographic position of the camera. Changing the pitch to a nonzero value moves the camera, but doesn’t affect this property.

## See Also

### Configuring the viewing angle

- [heading](heading.md) — The heading of the camera (in degrees) relative to true north.
- [centerCoordinateDistance](centercoordinatedistance.md) — The distance from the center point of the map to the camera, in meters.
- [pitch](pitch.md) — The viewing angle of the camera, in degrees.
- [altitude](altitude.md) — The altitude above the ground, in meters. _(deprecated)_
